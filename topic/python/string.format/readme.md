## Using custom placeholder tokens with python string.format()

### Context

* python 2.7
* string.format() method
* PROBLEM: string.format() is very powerful, but it does not natively support placeholder delimiter modification
    * string.format() uses curly-brace
    * curly-brace is a very common delimiter and causes [Delimiter collision](https://en.wikipedia.org/wiki/Delimiter#Delimiter_collision)
    * string.format() workaround is to double-up the delimiters, this is not tenable if you have a lot of source files
* SOLUTION: 
   * configure string.format() to support arbitrary delimiter placeholder syntax
   * this feature is supported in other contexts, such as the jinja templating system
       * http://jinja.pocoo.org/docs/dev/api/#high-level-api

### Example001: subtclassing python str()

* https://github.com/dreftymac/public.lab/blob/master/topic/python/string.format/demo.subclass.string.001.py

### Usage: easy placeholder entry using snippets with an IDE or text editor

* https://github.com/dreftymac/public.lab/blob/master/topic/python/string.format/placeholder-substitution.gif
