# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### document_metadata:
###   - caption: "__blank__"
###     dmid: "demo_subclassstring_tilingqpsocket"
###     date: created="2017-04-05"
###     last: lastmod="2017-04-05"
###     tags: tags
###     author: created="__author__"
###     filetype: "yaml"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * __desc__
###     seealso: |
###         * __seealso__
### <end-file_info>
"""

if('py_init_class'):
  class PowerString(str):
    def __new__(cls, string):
        ob = super(PowerString, cls).__new__(cls, string)
        return ob

    def upper(self):
        caps = super(PowerString, self).upper()
        return PowerString(caps + '123')

    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            print "A missing method was called."
            print "The object was %r, the method was %r. " % (self, name)
            print "It was called with %r and %r as arguments" % (args, kwargs)
        return _missing

if('py_demo_process'):
  mytest =  PowerString("Hello World")
  print mytest.upper().reverse()


