# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### main:
###   - date: created="Thu Dec 01 12:03:13 2016"
###     last: lastmod="Thu Dec 01 12:03:13 2016"
###     tags: python,string,format,subclass,oop,py2
###     author: created="dreftymac"
###     dmid: "upheaval_elm_id"
###     filetype: "py"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * demo code showing an alternate use of string.format()
###     seealso: |
###         * https://tobywf.com/2015/12/custom-formatters/
###         * http://stackoverflow.com/questions/21664318/subclass-string-formatter
###         * https://www.python.org/dev/peps/pep-3101/
### <end-file_info>

### BUGNAG:
### http://bugs.python.org/issue13579
### 2.7 doesn't support !a or 'ascii()' // ValueError: Unknown conversion specifier a

'''

### ----------------------------------
if('init_python'):
  import re
  import string
  import textwrap
  import yaml

### ----------------------------------
if('init_custom_formatter'):
  class CuFo003(string.Formatter): ## NO_WORKY -- not recursing all the way try chainable filters
    def __init__(self):
      super(CuFo003, self).__init__()
    def format_field(self, value, spec):
      if    str(spec.split('-')[-1]).endswith("xiden"):
        return self.format_field(str(value),"".join(spec.split('-')[0:-1]))
      elif  str(spec.split('-')[-1]).endswith("xrev"):
        return self.format_field(str(value)[::-1],"".join(spec.split('-')[0:-1]))
      elif  str(spec.split('-')[-1]).endswith("xupp"):
        return self.format_field(str(value).upper(),"".join(spec.split('-')[0:-1]))
      elif  str(spec.split('-')[-1]).endswith("xsqe"):
        return self.format_field(str(value).replace(' ',''),"".join(spec.split('-')[0:-1]))
      else:
        try:
          vout = super(CuFo003,self).format_field(value, spec)
        except:
          vout = super(CuFo003,self).format_field(value, '')
        return vout
  class PyHeredoc(str):
    def __new__(cls, value, srcdata={}):
      return str.__new__(cls,value)
    def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
      self.srcdata  =   srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
      self.fmt      =   CuFo003()
    def loop(self,items=[],): return "".join([ self.fmt.format(self.tokenize(),**vxx)for vxx in items])
    def tokenize(self): return(self.__str__().replace('{','{{').replace('}','}}')
      .replace(self.tkbeg,'{').replace(self.tkend,'}'))
    def render(self): return(self.fmt.format(self.tokenize(),**self.srcdata))
    def dedent(self): return textwrap.dedent(self.render())

### ----------------------------------
if('test_custom_formatter'):

  odata   =   yaml.safe_load('''
    project: Testing  1   2   3
    django_info:
      engine:     django.db.backends.postgresql
      dbname:     mytestdb
      dbuser:     mydbuser
      dbpass:     my/weak/password
      dbhost:     127.0.0.1
      dbport:     5432
    user_table:
      - username: alphadog
        userrowid: 1
        useremail: alpha@gg.com
      - username: bravomopp
        userrowid: 2
        useremail: bravo@gg.com
      - username: charlblobs
        userrowid: 3
        useremail: charlie@complexmail.com
    hosts_table:
      - hostname:  .coffeehouse.com
        hostaddr:  12.12.12.12
      - hostname:  .teahouse.com
        hostaddr:  14.14.14.14
  ''')

if( not 'show_demo_usage::loop'):
  odata['loop_users'] = PyHeredoc("""\
    -- <%userrowid:0>4%> ;; <%username:^12%> ;; <%useremail:>20%>@@
    """
    ,odata).loop(odata['user_table'])

if(not 'show_demo_usage::render'):
  print PyHeredoc("""
    <%project:xrev%>
    <%loop_users%>
    """,odata).render()

if(not not 'show_demo_usage::render'):
  print PyHeredoc("""
  <%project:-xsqe-xrev-xupp%>
  """,odata).dedent()



