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
       * http://jinja.pocoo.org/docs/dev/api/#high-level-api find="block_start_string"

## See also

* regain://upheaval_elm_id
* jinja syntax             ;; href="smartpath://mydaydirs/2017/week14/devlog.txt" find="jinjadelimiter_agoqpflourish"
* nice_documentation       ;; https://pyformat.info
* nice_blog_post           ;; https://tobywf.com/2015/12/custom-formatters/
* nice_blog_post           ;; https://tobywf.com/2015/12/sane-pluralisation/
* nice_blog_post           ;; http://blog.redturtle.it/2014/09/10/python-strings
* stackoverflow_question   ;; http://stackoverflow.com/questions/34214945/advanced-python-string-formatting-with-custom-placeholders
* stackoverflow_question   ;; http://stackoverflow.com/questions/35574349/python-format-string-with-custom-delimiters
* stackoverflow_question   ;; http://stackoverflow.com/questions/5466451/how-can-i-print-a-literal-characters-in-python-string-and-also-use-format
* github_repo_similar_idea ;; https://github.com/childsish/dynamic-yaml
* dmid regain              ;; regain://pystr_victoria_creaks_vetoer
* dmid crossref            ;; dmid://pyformat_korea_darkish_share
