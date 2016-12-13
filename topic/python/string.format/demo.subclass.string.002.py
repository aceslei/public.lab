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

  class HAL9000(object):
    # type = 'tree'
    # kinds = [{'name': 'oak'}, {'name': 'maple'}]
    def __format__(self, ssfmt=''):
      if (ssfmt == 'open-podbaydoors'):
          return "I'm afraid I can't do that."
      return 'HAL 9000'

### ----------------------------------
if('test_custom_formatter'):
  print '{:open-podbaydoors}'.format(HAL9000())
