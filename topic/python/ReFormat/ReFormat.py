# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - date: created="2016-12-13"
###     tags: tags
###     dmid: "undulate_marvels_grape"
###     filetype: "yaml"
###     lastupdate: ""
###     desc: |
###         * python string.Formatter addon
###         * a solution that extends python str.format() method with a custom class.
###     seealso: |
###         * __seealso__
### <end-file_info>
'''

if('init_py'):
  import string
  import re
  import textwrap
  import urllib

  class CustXcmd(object):
    '''
    * define chainable filters usable in str.format()
    '''
    ## custom methods not found in python str()
    def reverse(self,ssval):  return  ssval[::-1]
    def ucfirst(self,ssval):  return  str(ssval[0].upper()) + str(ssval[1:])
    def xencurl(self,ssval):  return  urllib.quote_plus(ssval)
    def xnosp(self,ssval):    return  str(ssval).replace(' ','')
    def xcaps(self,ssval):    return  (''.join(word.title() if vxx else word for vxx, word in enumerate(str(ssval).split('_'))))
    def xunder(self,ssval):   return  (re.sub(
              '([a-z0-9])([A-Z])', r'\1_\2',
              re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str(ssval))).lower())
    ## chainable str.format() filters ;; do not throw error on undefined filter
    def chain(self,ssval,aacmd):
      for action in aacmd:
        ## try to apply native str() method
        try: ssval = getattr(str,action)(ssval)
        except: pass
        ## try to apply custom CustXcmd method
        try: ssval = getattr(CustXcmd(),action)(ssval)
        except: pass
      return ssval

  class CustFmtShort(string.Formatter):
    '''
    * process chainable filters on str.format()
        * tkn_chaindelim is the first character that appears in a list of chainable commands
    '''
    def __init__(self):
      super(CustFmtShort, self).__init__()
      self.tkn_chaindelim = '|'
    def format_field(self, value, spec):
      if str(spec).startswith(self.tkn_chaindelim):
        return CustXcmd().chain(str(value),str(spec).split(self.tkn_chaindelim)[1:])
      else:
        try:    vout = super(CustFmtShort,self).format_field(value, spec)
        except: vout = super(CustFmtShort,self).format_field(value, '')
        return vout

  class String(str):
    '''
    * custom delimiters on str.format()
    * custom loop method on str.format()
    * custom dedent method on str.format()
    '''
    def __new__(cls, value, srcdata={}):
      return str.__new__(cls,value)
    def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
      self.srcdata  =   srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
      self.fmt      =   CustFmtShort()
    def loop(self,items=[],): return "".join([ self.fmt.format(self.custom_delimiterize(),**vxx)for vxx in items])
    def custom_delimiterize(self):
      vout = self.__str__()
      vout = re.sub(re.escape(self.tkbeg)+'\s+',self.tkbeg,vout)
      vout = re.sub('\s+'+re.escape(self.tkend),self.tkend,vout)
      vout = re.sub('\s+:',':',vout)
      vout = (vout.replace('{','{{').replace('}','}}')
      .replace(self.tkbeg,'{').replace(self.tkend,'}'))
      return vout
    def render(self): return(self.fmt.format(self.custom_delimiterize(),**self.srcdata))
    def dedent(self): return textwrap.dedent(self.render())
