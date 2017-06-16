# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - date: created="2016-12-14"
###     last: lastmod="2016-12-14"
###     dmid: "fate_misuse_yep"
###     filetype: "py"
###     desc: |
###         * demo use of custom ReFormat python addon
###         * extends the core functionality of str.format()
###         * barebones simple example usage
###     seealso: |
###         *
### <end-file_info>
'''

### ----------------------------------
if( 'init_python' ):
  import ReFormat   ## local import
                    ## requires PyHeredoc.py
                    ## in same directory as this python

### ----------------------------------
if( 'main' ):

  ## prepare source data
  odata = { "fname" : "Planet",
            "lname" : "Earth",
            "age"   : "4b years",
           }

  ## format output using source data
  vout = ReFormat.String("Hello <%fname%> <%lname%>!",odata).render()
  print vout

### ----------------------------------
if( 'show_result' ):
  '''
  Hello Planet Earth!
  '''
