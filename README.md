# EpiPortal's Resource Repository

You can Pull-Request this repository with:
* new/updated resources
* new/updated folders/folders name

## Limitations

Big files larger than 50Mb are not allowed in this repository due to [GitHub file size restrictions](https://help.github.com/articles/working-with-large-files/)

If you add lots of files, you can add big files to the `.gitignore` with the following command:

```
find . -size +1G | sed 's|^\./||g' | cat >> .gitignore; awk '!NF || !seen[$0]++' .gitignore
```

## One more word

Contribute! :)
