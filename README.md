# EpiPortal's Resource Repository - Since 2012

You can [Pull-Request](https://help.github.com/articles/creating-a-pull-request/) this repository with:
* new/updated/compressed resources
* updated/normalized resources name
* new/updated folders
* updated/normalized folders name

You can send (large) files to EpiPortal's mail address (with a link in the mail, because attached files larger than 10MB are not supported).

## Instructions

1. If possible, new files must be in PDF format (excepted for specific files such as code...)
2. If possible, compress your files before commiting them
3. Big files larger than 50MB are not allowed in this repository due to [GitHub file size restrictions](https://help.github.com/articles/working-with-large-files/). If you add lots of files, you can add big files to the `.gitignore` with the following command:

```
find . -size +50MB | sed 's|^\./||g' | cat >> .gitignore; awk '!NF || !seen[$0]++' .gitignore
```

4. Copyright files should not be pushed to this repository but can be sent to EpiPortal's mail adress. 

## One more word

Contribute! :)



## EPITA related links

* [Algo (prepa)](https://algo-td.infoprepa.epita.fr/)
* [Wiki prog (prepa)](https://wiki-prog.infoprepa.epita.fr/index.php/EPITA:Programmation)
* Archi (prepa)
  * [S1](http://debug-pro.com/epita/s1/en/)
  * [S2](http://debug-pro.com/epita/s2/en/)
  * [S3](http://debug-pro.com/epita/s3/en/)
  * [S4](http://debug-pro.com/epita/s4/en/)

* [Ionis X](https://ionisx.com/)

* [Mastercorp](http://mastercorp.epita.eu)

* [Chronos](http://chronos.epita.net)
* [EpiMAP](http://map.epita.eu/)
* News Reader/Notifier for EPITA news
  * [Website, NG-Notifier](https://ng-notifier.42portal.com/)
  * [Android application](https://play.google.com/store/apps/details?id=com.bertet.francois.epinotifier&hl=en_US)
  * [iOS application](https://itunes.apple.com/us/app/epireader/id1244757421?mt=8&ign-mpt=uo%3D4)
