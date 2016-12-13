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
###         * http://stackoverflow.com/questions/21664318/subclass-string-formatter
###         * https://www.python.org/dev/peps/pep-3101/
### <end-file_info>
'''

### ----------------------------------
if('init_python'):
  import re
  import string
  import textwrap
  import yaml

### ----------------------------------
if('init_custom_formatter'):
  class CuFo001(string.Formatter): ## YES_WORKY with autonumbering
      '''
      CuFo001 -- testing override of string.format()
      * here we do not care about empty brace {} autonumbering
      '''
      def __init__(self):
        super(CuFo001, self).__init__()

      def format_field(self, value, format_string):
        # handle an invalid format
        if format_string == "i":
            return self.eng(value)
        else:
            return super(CuFo001,self).format_field(value, format_string)

### ----------------------------------
if('test_custom_formatter'):

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

  fmt = CuFo001()
  print('{}'.format(0.055412))
  print(fmt.format("{0:i} ", 55654654231654))
  print(fmt.format("{}", 0.00254641))

