# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### document_metadata:
###   - caption: "demo python heredoc"
###     dmid: "demo_pyheredoc_patriot11provo"
###     date: created="Fri 2017-05-12 11:53:10"
###     last: lastmod="2017-04-05"
###     lastupdate: ""
###     desc: |
###         * demonstrate python-style heredoc with variables loops and fluent interface
###     seealso: |
###         * http://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
### <end-file_info>
"""

if('init_python'):
  import re
  import string
  import textwrap
  import yaml
  import PyHereDoc ## href="./PyHereDoc.py"

if( not 'demo::simpletest extended formatting::drivable04palpable'):
  ##
  odoc    =  PyHereDoc.Document
  ddinfo  = {'fname':'Alice','lname':'Baker'
            ,'msgfrom':'our friends'
            ,'msgto':'your friends'}

  ##
  vout    =  odoc().tos("Hello {fname} {lname}!",data=ddinfo)

  ##
  print(vout)

if( not not 'region::alternate delimiters::drivable05palpable'):
  ##
  odoc    =   PyHereDoc.Document
  dconfig =   { '{':'<%', '}':'%>', }
  dconfig =   { 'tkbeg':'<%', 'tkend':'%>', }
  ddinfo  =   {'fname':'Alice','lname':'Baker'
              ,'msgfrom':'our friends'
              ,'msgto':'your friends'}

  ##
  vout    =  odoc(dconfig).tos("Hello <%fname%> <%lname%>!",data=ddinfo)

  ##
  print(vout)

