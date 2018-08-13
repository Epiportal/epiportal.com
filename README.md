# EpiPortal's Resource Repository

You can [Pull-Request](https://help.github.com/articles/creating-a-pull-request/) this repository with:
* new/updated resources/resources name
* new/updated folders/folders name

You can send (large) files to EpiPortal's mail address (with a link in the mail, because attached files larger than 10MB are not supported).

## Limitations

Big files larger than 50MB are not allowed in this repository due to [GitHub file size restrictions](https://help.github.com/articles/working-with-large-files/).

If you add lots of files, you can add big files to the `.gitignore` with the following command:

```
find . -size +50MB | sed 's|^\./||g' | cat >> .gitignore; awk '!NF || !seen[$0]++' .gitignore
```

## One more word

Contribute! :)
