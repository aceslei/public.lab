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
###     seealso: |
###         * http://stackoverflow.com/questions/21664318/subclass-string-formatter
### <end-file_info>
'''

### ----------------------------------
if('init_python'):
  import re
  import textwrap
  import yaml
  import string
  from math import floor, log10

### ----------------------------------
if('init_custom_formatter'):
  class CustFormatter(string.Formatter): ## YES_WORKY with autonumbering
      "Defines special formatting"
      def __init__(self):
          super(CustFormatter, self).__init__()
          self.last_number = 0

      def get_value(self, key, args, kwargs):
          if key == '':
              key = self.last_number
              self.last_number += 1
          return super(CustFormatter, self).get_value(key, args, kwargs)

      def powerise10(self, x):
          if x == 0: return 0, 0
          Neg = x < 0
          if Neg: x = -x
          a = 1.0 * x / 10**(floor(log10(x)))
          b = int(floor(log10(x)))
          if Neg: a = -a
          return a, b

      def eng(self, x):
          a, b = self.powerise10(x)
          if -3 < b < 3: return "%.4g" % x
          a = a * 10**(b%3)
          b = b - b%3
          return "%.4g*10^%s" % (a, b)

      def format_field(self, value, format_string):
        # handle an invalid format
        if format_string == "i":
            return self.eng(value)
        else:
            return super(CustFormatter,self).format_field(value, format_string)

### ----------------------------------
if('test_custom_formatter'):
  fmt = CustFormatter()
  print('{}'.format(0.055412))
  print(fmt.format("{0:i} ", 55654654231654))
  print(fmt.format("{}", 0.00254641))

