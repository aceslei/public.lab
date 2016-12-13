# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### main:
###   - date: created="Thu Dec 01 12:03:13 2016"
###     last: lastmod="Thu Dec 01 12:03:13 2016"
###     tags: python,string,format,subclass,oop,py2
###     author: created="dreftymac"
###     dmid: "narceine_land_brains"
###     filetype: "py"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * demo code showing an alternate use of string.format()
###         * demo showing loop output
###     seealso: |
###         * http://stackoverflow.com/questions/35574349/python-format-string-with-custom-delimiters
###         * http://stackoverflow.com/questions/9589301/python-heredoc
###         * href="smartpath://mytrybits/p/trypython/lab2014/readme.txt" find="blends_cocos_luring"
### <end-file_info>
'''

### ----------------------------------
if('init_python'):
  import re
  import textwrap
  import yaml

### ----------------------------------
if('init_custom_formatter'):
  class PythonHeredoc(str): ## comment out stubs
    '''extend python str.format()
        * permit custom placeholder delimiters
        * support simple loops
    '''
    def __new__(cls, value, srcdata={}, tkbeg='<%',tkend='%>',):
      return str.__new__(cls,value)
    def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
      self.srcdata = srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
    def loop(self,items=[],):
      vout = ''
      for curr in items:
        vout += self.preformat().format(**curr)
      return vout
    def preformat(self): return(self.__str__()
      .replace('{','{{').replace('}','}}')
      .replace(self.tkbeg,'{').replace(self.tkend,'}'))
    def render(self): return(
      self.preformat().format(**self.srcdata))

  odata   =   yaml.safe_load('''
    project: Testing123
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
        useremail: charlie@complicatedmail.com
    hosts_table:
      - hostname:  .coffeehouse.com
        hostaddr:  12.12.12.12
      - hostname:  .teahouse.com
        hostaddr:  14.14.14.14
  ''')

### ----------------------------------

if(not not 'show_demo_usage::format'):
  print PythonHeredoc("""  {} """,odata).format(**odata)
  exit()

if(not not 'show_demo_usage::loop'):
  print PythonHeredoc("""   -- <%userrowid:0>4%> ;; <%username:^12%> ;; <%useremail:>20%>@@\n""",odata).loop(odata['user_table'])
  exit()

if('show_demo_usage::ssfmt::custom_formatter'):
  print PythonHeredoc(""" This is the <%project:h%> alpha and this is the @@bravo """,odata).render()
  exit()


if('show_demo_usage::PythonHeredoc'):


  # vout    = (''
  # + PythonHeredoc('''
  # ''',odata).render()
  vout  = (PythonHeredoc('''
  ALLOWED_HOSTS = [
  ]
  DATABASES = {
      'default': {
          'ENGINE':   '<%django_info[engine]%>',
          'NAME':     '<%django_info[dbname]%>',
          'USER':     '<%django_info[dbuser]%>',
          'PASSWORD': '<%django_info[dbpass]%>',
          'HOST':     '<%django_info[dbhost]%>',
          'PORT':     '<%django_info[dbname]%>',
      }
  }
  ''',odata).render()
  )
  print vout
  exit()



if('document_sample_output::PythonHeredoc'):
  '''
  DATABASES = {
      'default': {
          'ENGINE':   'django.db.backends.postgresql',
          'NAME':     'mytestdb',
          'USER':     'mydbuser',
          'PASSWORD': 'my/weak/password',
          'HOST':     '127.0.0.1',
          'PORT':     'mytestdb',
      }
  }
  '''
