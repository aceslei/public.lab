# Overview

This is a quick writeup of first-impressions and notes on [visualstudio code editor](https://code.visualstudio.com/) [version 1.12.2].

This is from the perspective of a self-described "text editor geek" who is familiar with:
* `Atom` 
* `KomodoIDE`
* `Sublime` 
* `Vim` 
* A lot of the [other tools on this list](https://insights.stackoverflow.com/survey/2017#technology-most-popular-developer-environments-by-occupation) and even others [on this list](https://en.wikipedia.org/wiki/Comparison_of_text_editors#Overview).

**Highlights:**
* General grade: solid 4.5 stars out of 5
* Most key features "just work" without hassle, surprising quirks or rigamorole.
* The devlopment team behind this product appears to be a sharp crew with savvy design sensibilities.
* This is a tool for experienced/advanced use, but is also very approachable for non-experts.

**Lookups and Research:**
* What is the debugging/development experience like for Python/Perl/Ruby
* How easy is it to extend with user-created addons
* How easy is it to do advanced editing and configuration on par with Vim

# Topics

## advanced tips and tricks
* https://github.com/Microsoft/vscode-tips-and-tricks
* TOTRY ;; json schema for intellisense on JSON files, how does this work?

## annoyances and weirdness
* resolve save conflict came up for file that was edited in outside editor ... it was a bit counter-intuitive at first

## features that "just work"

* cmd_pal          ;; user_interface  ;; works just like you expect from Sublime, Atom, KomodoIDE and others
* cmd_pal language ;; syntax          ;; Change language mode easily changes syntax coloring
* cmd_pal language ;; syntax          ;; YAML syntax (indentation-based) worked out of the box with syntax coloring
* cmd_pal folding  ;; folding         ;; code folding worked effortlessly out of the box on indentation-based syntax           
* ctrl+space       ;; word_completion ;; works well, has a slightly unique completion fuzzy-match approach
* keybindings      ;; user_interface  ;; Much more intuitive than Atom to override or disable keybindings, but appears to be just as powerful
* custom userconfig ;; configuration ;; it was easy to symlink my user settings directory away from the default path (this is something I *always* do because I never like the default config directories and I want my configs to be in version control)

## features to explore

### code lens
* this one looks like it might be a proprietary "non-freemium" thing
* https://code.visualstudio.com/blogs/2017/02/12/code-lens-roundup
* https://medium.com/hack-visual-studio-code/toggle-any-setting-in-vs-code-using-keyboard-shortcut-arguments-cdb5ddc56955

### custom settings directory
* default ;; C:\Users\smosley\AppData\Roaming\Code\User
* customized ;; C:\sm\docs\mytrybits\v\tryvisualstudiocode\addon\AppData-Roaming-Code-User

### custom tasks
* https://code.visualstudio.com/docs/editor/tasks
* https://stevenwooding.com/how-to-run-python-in-visual-studio-code/
* https://code.visualstudio.com/docs/editor/tasks-appendix
* href="smartpath://mydaydirs/2017/week21/.vscode/tasks.json" find="vscodetasks_grieving09dean"

### keybindings
* Overview
* how to remap keybindings?
* how to disable keybindings?      
* ctrl+shift+k ;;  delete line ;;  how to change this to ctrl+shift+y
* opening up cmd_pal and type in `key` immediately brings up keyboard help and a pdf download, very nice
* keybindings have a json config, similar to atom, but it is normal json, and not atom-flavored-coffeescript

### python
* https://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code
* https://www.stevefenton.co.uk/2015/05/Custom-Tasks-In-Visual-Studio-Code/

### terminal (cygwin)
* https://github.com/Microsoft/vscode/issues/14977
* href="./txt/cygwin-terminal.txt"
* c:\programs\cygwin\bin\mintty.exe --position 400,90 --size 120,40 -e /bin/xhere /bin/bash.exe "."

### vim
* https://github.com/VSCodeVim/Vim/blob/master/ROADMAP.md