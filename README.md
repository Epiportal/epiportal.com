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

### Prepa

* [Algo](https://algo-td.infoprepa.epita.fr/)
* [Algo code](https://github.com/nathalieEpita/classrooms)
* [Wiki prog](https://wiki-prog.infoprepa.epita.fr/index.php/EPITA:Programmation)
* Archi [S1](http://debug-pro.com/epita/s1/en/) | [S2](http://debug-pro.com/epita/s2/en/) | [S3](http://debug-pro.com/epita/s3/en/) | [S4](http://debug-pro.com/epita/s4/en/)

### Autres ressources

* [Mastercorp](http://mastercorp.epita.eu)
* [Ionis X](https://ionisx.com/)

### Intranets

* [IntraBocal](https://console.bocal.org/#/) (Comptes EPITA, Tickets, Lien vers MSDNAA)
* [Intra ACDC](https://acdc.cri.epita.net/)
* [Intra CRI](https://intra.cri.epita.net/)
* [Odysee](http://odyssee.epita.fr/) (Séjour à l'international)
* [Intracom](http://intracom.epita.fr/) (JPO...)
* [Relations Entreprises](https://epita.net/) (Relations entreprises)

* [EPITA Anciens](http://www.epita-anciens.fr/)


### Administratif/Notes/Planning/...

* [Chronos](http://chronos.epita.net) (Planning)
* [Epimap](http://map.epita.eu/) (Cartes des locaux)
* [Pegasus](https://prepa-epita.helvetius.net/pegasus) (Notes)

### Associations

* [BDE NOVA](https://bde-epita.fr/)
* [GConfs](https://gconfs.fr/)


### Laboratoires

* [LRDE](https://www.lrde.epita.fr)
* [LSE](https://lse.epita.fr/)


### Applications et autres

* News Reader/Notifier for EPITA news [Website](https://ng-notifier.42portal.com/) | [Android app](https://play.google.com/store/apps/details?id=com.bertet.francois.epinotifier&hl=en_US) | [iOS app](https://itunes.apple.com/us/app/epireader/id1244757421?mt=8&ign-mpt=uo%3D4)


### Old

* [FAQ EPITA](https://faq.epita.eu/)
* [EPIFAQ](http://www.zorinaq.com/epifaq/epifaq-1.1.3-2003-01-09.html)
* [Doc EPITA](http://canartichaut.kawie.fr/epita/)
