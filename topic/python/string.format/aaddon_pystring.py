# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### document_metadata:
###   - caption: "__blank__"
###     dmid: "pyaddon_strformat_faucetqptysan"
###     date: created="2017-04-05"
###     last: lastmod="2017-04-05"
###     author: created="dreftymac"
###     filetype: "yaml"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * __desc__
###     seealso: |
###         * __seealso__
### <end-file_info>
"""
if('init_python'):
  import re
  import string
  import textwrap

if('init_custom_formatter'):
  class CuFo004(string.Formatter):
    def __init__(self):
      super(CuFo004, self).__init__()
    def format_field(self, value, spec):
      if    str(spec).startswith("xiden"):  return str(value)
      elif  str(spec).endswith("xrev"):   return str(value)[::-1]
      elif  str(spec).endswith("xupp"):   return str(value).upper()
      elif  str(spec).endswith("xnosp"):  return str(value).replace(' ','')
      elif  str(spec).endswith("xcaps"):  return (''.join(word.title()
              if vxx else word for vxx, word in enumerate(str(value).split('_'))))
      elif  str(spec).endswith("xundr"):  return (re.sub(
              '([a-z0-9])([A-Z])', r'\1_\2',
              re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str(value))).lower())
      else:
        try:
          vout = super(CuFo004,self).format_field(value, spec)
        except:
          vout = super(CuFo004,self).format_field(value, '')
        return vout
  ##;;

if('init_py_heredoc'):
  class PyHeredoc(str):
    def __new__(cls, value, srcdata={}):
      return str.__new__(cls,value)
    def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
      self.srcdata  =   srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
      self.fmt      =   CuFo004()
    def loop(self,items=[],): return "".join([ self.fmt.format(self.tokenize(),**vxx)for vxx in items])
    def tokenize(self): return(self.__str__()
      .replace('{','{{')
      .replace('}','}}')
      .replace(self.tkbeg,'{').replace(self.tkend,'}'))
    def render(self): return(self.fmt.format(self.tokenize(),**self.srcdata))
    def dedent(self): return textwrap.dedent(self.render())
  ##;;

  