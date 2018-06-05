# datalogi.org
Den her programbank indeholder koden til at generere filerne til
https://datalogi.org.


## Opsætning

Den her kommandosekvens laver en klon af koden, sætter et virtuelt
miljø op (så andre Python installationer ikke bliver forstyret) og
installerer kodens afhængigheder.

``` bash
$ git clone https://github.com/datalogi/datalogi.org
$ cd datalogi.org
$ virtualenv -p python3.6 venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

Hvis du vil ud af det virtuelle miljø, skal du bare skrive `deactivate`
i din terminal.


## Byg filerne

OBS: Dette laver (eller overskriver) mappen `build/`!

Hvis du laver nogle ændringer, skal du generere filerne. Det gør
man med kommandoen:

``` bash
$ python datalogi.py
```


## Local server

Det er en god ide at køre en lokal server, så relative stier virker
(bl. a. menuen). Til det, kan du bruge følgende kommando:

``` bash
$ cd build
$ python -m http.server 7000
```

Du kan se filerne i din browser på dette link http://localhost:7000
