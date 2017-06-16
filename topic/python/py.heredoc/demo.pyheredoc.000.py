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
###     seeinstead: |
###         * href="smartpath://mytrybits/p/trypython/lab2014/pystring/barebones.format.003.py" find="strformat_extend_recall12grumble"
### <end-file_info>

## TODO: todoitems_securelyqpstash
  * DONE ;; add in CustomFormat with placeholder syntax
  * DONE ;; support for alternate delimiters
  * TODO ;; methods to add
      * tofile()
      * tozipfile()
      * eachwithindex
      * possible chainable formatters in customized str.formatter?
  * TODO ;; make option for default fmtbody args, to reduce linenoise
    * "./demo-image-000.html"
"""

if('init_python'):
  import re
  import string
  import textwrap
  import yaml
  import PyHereDoc

if( not not 'region::basic demo::musket02fully'):
  '''
  ## PyHereDoc barebones intro

  Demonstrates:
  * basic usage
  * using the `tos` (tostring) method
  * native python string method `title`
  * addon non-native python string method `reverse`
  * chainable methods to support fluent interface

  '''
  odoc = PyHereDoc.Document

  print odoc().tos("hello world")                   ##=> hello world
  print odoc().tos("hello world").reverse()         ##=> dlrow olleh
  print odoc().tos("hello world").title().reverse() ##=> dlroW olleH
  print odoc().tos("hello world").reverse().title() ##=> Dlrow Olleh

  pass

if( not 'region::basic demo::musket03fully'):
  '''
  ## PyHereDoc `concat`

  Demonstrates:
  * PyHereDoc `concat` method for combining multiple PyHereDoc strings
  '''

  odoc = PyHereDoc.Document

  print (odoc()
         .concat("alpha")
         .concat("bravo")
         .concat("charlie")
         )

  result = '''
  alphabravocharlie
  '''

  pass

if( not 'region::basic demo::musket04fully'):
  '''
  ## PyHereDoc `concat` with `puts` and `n`

  Demonstrates:
  * PyHereDoc `concat` method for combining multiple PyHereDoc strings
  * PyHereDoc `concat` is synonym method for `tos`
  * Adding newlines supported with `puts` and `n`
  * `n` is an alias for `puts` and eases the amount of typing necessary (drawback, less intutive integer-based formatter)
      * puts='<'  ;;  n=1 ;; add a leading newline
      * puts='>'  ;;  n=2 ;; add a trailing newline
      * puts='<>' ;;  n=3 ;; both leading and trailing newline
  '''

  ## ANNOYANCE ;; wish python had symbols like ruby programming language.
  ##    that way, it would not be necessary to have the cryptic syntax needed with `n`
  ##    or the verbose typing needed with `puts`
  ##    ruby symbols would allow a bare keyword

  odoc = PyHereDoc.Document

  print (odoc()
         .concat("alpha",puts='<')
         .concat("bravo",)
         .concat("charlie",puts='<>')
         .concat("delta",puts='')
         .concat("echo",puts='')
         )

  print (odoc()
         .concat("foxtrot",n=1)
         .concat("golf",)
         .concat("hotel",n=3)
         .concat("india",n=0)
         .concat("juliet",n=0)
         )

  result = '''
  alphabravo
  charlie
  deltaecho

  foxtrotgolf
  hotel
  indiajuliet
  '''

  pass

if( not 'region::basic demo::predict02halogen'):
  '''
  ## PyHereDoc barebones intro

  Demonstrates:
  * Using triple-quoted string
  * PROBLEM: the indentation of the python source code affects the string output
      * We do not the output string to be indented with leading space
      * We also do not want to have to change the indentation of the python source code in order to fix it
  '''
  odoc  = PyHereDoc.Document

  print odoc().tos("""
             Hello World!
                This is a message
                from me to you

             """)

  result = '''
             Hello World!
                This is a message
                from me to you
  '''
  pass

if( not 'region::basic demo::predict03halogen'):
  '''
  ## PyHereDoc barebones intro

  Demonstrates:
  * Using triple-quoted string
  * Using strip to remove leading whitespace owing to indentation of the python code
  * PROBLEM: although the leading whitespace is removed from the first line, the remainder of the output string still looks bad

  '''
  odoc  = PyHereDoc.Document

  print odoc().concat("""
             Hello World!
                This is a message
                from me to you

             """,strip='<')

  result = '''
  Hello World!
                  This is a message
                  from me to you
  '''

  pass

if( not 'region::basic demo::predict04halogen'):
  '''
  ## PyHereDoc barebones intro

  Demonstrates:
  * Using triple-quoted string
  * Using dedent to remove leading whitespace from all the lines
      * This avoids the problem associated with `strip` and indented python code
      * Any truthy value enables dedent
  '''
  odoc  = PyHereDoc.Document

  print odoc().concat("""
             Hello World!
                This is a message
                from me to you

             """,dedent=1)

  result = '''
  Hello World!
     This is a message
     from me to you
  '''

  pass

if( not 'region::basic demo::jackknife01dry'):
  '''
  ## PyHereDoc data intro

  Demonstrates:
  * Using python triple-quoted string
  * Using `dedent`
  * Using the `data` argument for string templating
  '''
  odoc    = PyHereDoc.Document
  ddinfo  = {'fname':'Alice','lname':'Baker'
            ,'msgfrom':'our friends'
            ,'msgto':'your friends'}

  print odoc().concat("""
             Hello {fname} {lname}!
                This is a message
                from {msgfrom} to {msgto}.

             """,dedent=1,data=ddinfo)

  result = '''
  Hello Alice Baker!
     This is a message
     from our friends to your friends.
  '''

  pass

if( not not 'region::basic demo::jackknife02dry'):
  '''
  ## PyHereDoc data intro

  Demonstrates:
  * Using python triple-quoted string
  * Using `dedent`
  * Using the `data` argument for string templating
  * Using the `each` method for looping
  * Wrapping the statement in parens to allow indenting the chainable string methods
  '''

  odoc    =   PyHereDoc.Document
  ddinfo  = {'fname':'Alice','lname':'Baker'
            ,'msgfrom':'our friends'
            ,'msgto':'your friends'}
  aatable = [
    {'item':'alpha'   ,'quantity':'1' , 'desc':'first'},
    {'item':'bravo'   ,'quantity':'2' , 'desc':'second'},
    {'item':'charlie' ,'quantity':'3' , 'desc':'third'},
    {'item':'delta'   ,'quantity':'4' , 'desc':'fourth'},
  ]

  print (odoc().concat("""
          Hello {fname} {lname}!
             This is a message
             from {msgfrom} to {msgto}.

          Here are the items for {fname}:

             """,dedent=1,data=ddinfo,strip='>')
         .each("""\n   * {item:<8}|{quantity:^3}|{desc:>7}"""
               ,data=aatable))

  result = '''
  Hello Alice Baker!
     This is a message
     from our friends to your friends.
  '''

  pass

if( not 'region::basic demo::musket02fully'):
  '''
  barebones intro to how PyHereDoc works
  '''

  ## all of these work as expected and desired
  odata = dict()
  odata['fname'] = 'Homer'
  odata['lname'] = 'Simpson'
  odoc  = PyHereDoc.Document
  print odoc("hello world")
  print odoc("hello world").reverse()
  print odoc("hello world").title().reverse()
  print odoc("hello world").reverse().title()
  print odoc("hello world").startswith('hello')
    ## this behaves differently when PyHereDoc extends object (keeps chainability)
    ## this behaves differently when PyHereDoc extends str (breaks chainability)
    ##    subclassing str breaks chainability because __getattr__ never gets called on `startswith`
    ##    since a `startswith` method exists on str
  pass

if( not 'region::demo_holdingsqlalan'):
  odata = yaml.safe_load('''
  projectinfo:
    basename: Hello World Project
    geekname: helloworldproject
  peopletable:
  - fname: Homer
    lname: Simpson
    age:   33
  - fname: Maggie
    lname: Bimpson
    age:   23
  - fname: Lisa
    lname: Dimpson
    age:   13
  ''')
  vout = ''
  vout += str(PyHereDoc.Document()
          .concat("""
            ## Hello: {basename}
            * Hola
            * Hello
            * Bonjour
            ----
            """
            ,data=odata['projectinfo'], puts='>',strip='<>',indent=0)
          .each("""
            * {fname:<12}|{lname:^20}|{age}
                """,data=odata['peopletable'],puts='>',strip='<>',dedent=1)
          .concat("""
            ----
            ## World: {basename}
            * Mundo
            * World
            * Monde
            ----
            """
            ,data=odata['projectinfo'], puts='>',strip='<>',indent=0)
          )
  print vout
  pass
