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

class PowerString(str):
    def __new__(cls, string):
        ob = super(DerivedClass, cls).__new__(cls, string)
        return ob

    def upper(self):
        caps = super(DerivedClass, self).upper()
        return DerivedClass(caps + '123')

    def __getattribute__(self, name):
        att = super(DerivedClass, self).__getattribute__(name)

        if not callable(att):
            return att

        def call_me_later(*args, **kwargs):
            result = att(*args, **kwargs)
            if isinstance(result, basestring):
                return DerivedClass(result)
            return result
        return call_me_later