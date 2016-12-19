# Using custom placeholder tokens with python string.format()

## Context

  * python 2.7
  * string.format()
  * alternative approach that allows custom placeholder syntax

## Problem

We want to use custom placeholder delimiters with python str.format()

  * string.format() is very powerful, but it does not natively support placeholder delimiter modification.
  * string.format() uses curly-brace which is very common and and causes [Delimiter collision](https://en.wikipedia.org/wiki/Delimiter#Delimiter_collision)
  * string.format() default workaround is to double-up the delimiters, which can be cumbersome.

## Solution

We write a custom class that extends native python str.format()

  * extend native python str.format with custom class
  * configure string.format() to support arbitrary delimiter placeholder syntax
  * permit other enhancements such as custom formatters and filters

## Example001: Demo use of a custom ReFormat class

  * we wrote a custom ReFormat class that extends python str.format()

<pre>
## import custom class
import ReFormat

## prepare source data
odata = { "fname" : "Planet",
          "lname" : "Earth",
          "age"   : "4b years",
         }

## format output using .render() method of custom ReFormat class
vout = ReFormat.String("Hello <%fname%> <%lname%>!",odata).render()
print vout
</pre>

## Pitfalls

  * requires extension class to str.format()
  * not intended as a substitute for full-blown sandbox-compatible templating solution

## See also

* nice_documentation       ;; https://pyformat.info/
* nice_blog_post           ;; https://tobywf.com/2015/12/custom-formatters/
* nice_blog_post           ;; https://tobywf.com/2015/12/sane-pluralisation/
* stackoverflow_question   ;; http://stackoverflow.com/questions/34214945/advanced-python-string-formatting-with-custom-placeholders
* stackoverflow_question   ;; http://stackoverflow.com/questions/35574349/python-format-string-with-custom-delimiters
* stackoverflow_question   ;; http://stackoverflow.com/questions/5466451/how-can-i-print-a-literal-characters-in-python-string-and-also-use-format
* stackoverflow_question   ;; http://stackoverflow.com/questions/6748559/generating-html-documents-in-python/6748854
* github_repo_similar_idea ;; https://github.com/childsish/dynamic-yaml
* github gist              ;; https://gist.github.com/jamescasbon/1461441
