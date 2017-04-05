## Using custom placeholder tokens with python string.format()

### Context

* python 2.7

* string.format() method

* PROBLEM: string.format() is very powerful, but it does not natively support placeholder delimiter modification
    * string.format() uses curly-brace
    * curly-brace is a very common delimiter and causes [Delimiter collision](https://en.wikipedia.org/wiki/Delimiter#Delimiter_collision)
    * string.format() workaround is to double-up the delimiters, this is not tenable if you have a lot of source files and do NOT want to modify them

* SOLUTION:
   * configure string.format() to support arbitrary delimiter placeholder syntax
   * this feature is supported in other contexts, such as the jinja templating system
       * http://jinja.pocoo.org/docs/dev/api/#high-level-api

### Example001: subclassing python str()

* https://github.com/dreftymac/public.lab/blob/master/topic/python/string.format/demo.subclass.string.001.py

### Example002: extending string.Formatter

* https://github.com/dreftymac/public.lab/blob/master/topic/python/string.format/demo.subclass.string.002.py

### Usage: easy placeholder entry using snippets with an IDE or text editor

* https://github.com/dreftymac/public.lab/blob/master/topic/python/string.format/placeholder-substitution.gif


## See also

* nice_documentation       ;; https://pyformat.info
* nice_blog_post           ;; https://tobywf.com/2015/12/custom-formatters/
* nice_blog_post           ;; https://tobywf.com/2015/12/sane-pluralisation/
* stackoverflow_question   ;; http://stackoverflow.com/questions/34214945/advanced-python-string-formatting-with-custom-placeholders
* stackoverflow_question   ;; http://stackoverflow.com/questions/35574349/python-format-string-with-custom-delimiters
* stackoverflow_question   ;; http://stackoverflow.com/questions/5466451/how-can-i-print-a-literal-characters-in-python-string-and-also-use-format
* github_repo_similar_idea ;; https://github.com/childsish/dynamic-yaml
* dmid crossref            ;; dmid://pyformat_korea_darkish_share

