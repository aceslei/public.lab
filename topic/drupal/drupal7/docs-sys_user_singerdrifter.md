```
### <beg-file_info>
### document_metadata:
###   - date: created="2017-02-02"
###     last: lastmod="2017-02-02"
###     tags: drupal,d7,views,user,permissions
###     dmid: "wariest_waylaid_wind"
###     filetype: "md"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * __desc__
###     seealso: |
###         * https://gist.github.com/dreftymac/21911ec045824baec0013e132239ccfd
###         * per-display security annoyance ;; https://www.drupal.org/node/1174588
### <end-file_info>
```

## Overview
* documentation for views sys_user_singerdrifter
* Dependencies: sys_sitegrpp content type (regain://drupsitegrp_main_boater)

### page00
* display all users
* quick and easy way to see all users uids and sys_sitegrpp settings
* Access:Permission | Administer users

### page01
* same as previous, but json format
* Access:Permission | Administer users

### usercurr
* display currently logged in user only
* Access:Permission | View published content

### usercurrjson
* same as previous, but json format
* annoyance: multi-value fields are separated by newline
    * (eg) "groups": "alpha\nbravo\ncharlie\ndelta\n",
