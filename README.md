# EpiPortal's Resource Repository

You can [Pull-Request](https://help.github.com/articles/creating-a-pull-request/) this repository with:
* new/updated/compressed resources
* updated/normalized resources name
* new/updated folders
* updated/normalized folders name

You can send (large) files to EpiPortal's mail address (with a link in the mail, because attached files larger than 10MB are not supported).

## Instructions

1. If possible, new files must be in PDF format (excepted for specific files such as code...)
2. If possible, Compress your files before commiting them
3. Big files larger than 50MB are not allowed in this repository due to [GitHub file size restrictions](https://help.github.com/articles/working-with-large-files/). If you add lots of files, you can add big files to the `.gitignore` with the following command:

```
find . -size +50MB | sed 's|^\./||g' | cat >> .gitignore; awk '!NF || !seen[$0]++' .gitignore
```

4. 

## One more word

Contribute! :)
