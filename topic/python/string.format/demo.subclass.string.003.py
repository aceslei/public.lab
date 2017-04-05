# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### main:
###   - date: created="Thu Dec 01 12:03:13 2016"
###     last: lastmod="Thu Dec 01 12:03:13 2016"
###     tags: python,str.format,subclass,oop,py2
###     author: created="dreftymac"
###     dmid: "upheaval_elm_docurd"
###     filetype: "py"
###     lastupdate: "demo subclass str.format"
###     desc: |
###         ##
###         * demo code showing an alternate use of str.format()
###         ## BUGNAG:
###         * http://bugs.python.org/issue13579
###         * 2.7 doesn't support !a or 'ascii()' // ValueError: Unknown conversion specifier a
###     seealso: |
###         ## weblinks
###         * https://tobywf.com/2015/12/custom-formatters/
###         * http://stackoverflow.com/questions/21664318/subclass-str.formatter
###         * https://www.python.org/dev/peps/pep-3101/
###         * https://en.wikipedia.org/wiki/Camel_case#Variations_and_synonyms
### <end-file_info>
'''

### ----------------------------------
if('init_python'):
  import re
  import textwrap
  import yaml
  from aaddon_pystring import CuFo004
  from aaddon_pystring import PyHeredoc

### ----------------------------------
if('init_source_data'):

  odata   =   yaml.safe_load('''
    project:        ThisCamelCaseWord
    projcaps:       This Capitalized Sentence
    projunder:      this_underscore_word
    django_info:
      engine:     django.db.backends.postgresql
      dbname:     mytestdb
      dbuser:     mydbuser
      dbpass:     my/weak/password
      dbhost:     127.0.0.1
      dbport:     5432
    user_table:
      - username:   alphadog
        userrowid:  1
        useremail:  alpha@gg.com
      - username:   bravomopp
        userrowid:  2
        useremail:  bravo@gg.com
      - username:   charloblobs
        userrowid:  3
        useremail:  charlie@complexmail.com
    hosts_table:
      - hostname:  .coffeehouse.com
        hostaddr:  12.12.12.12
      - hostname:  .teahouse.com
        hostaddr:  14.14.14.14
  ''')

### ----------------------------------
if('show_demo_output'):

  if( not not 'show_demo_usage::loop'):
    odata['loop_users'] = PyHeredoc(textwrap.dedent("""
      -- <%userrowid:0>4%> ;; <%username:^12%> ;; <%useremail:>20%>@@""")
      ,odata).loop(odata['user_table'])
    print odata['loop_users']

  if(not not 'show_demo_usage::render'):
    print PyHeredoc("""
      <%project:xrev%>
      <%loop_users%>
      """,odata).render()

  if(not not 'show_demo_usage::render'):
    print PyHeredoc("""
    $<%project:xundr%>
    $<%project:xcaps%>

    $<%projcaps:xundr%>
    $<%projcaps:xcaps%>

    $<%projunder:xundr%>
    $<%projunder:xcaps%>

    """,odata).dedent()



