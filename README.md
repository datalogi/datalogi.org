# datalogi.org
Den her programbank indeholder koden til at generere filerne til
https://datalogi.org.


## Intallér dependencies

``` bash
$ pip install -r requirements.txt
```


## Byg filerne

``` bash
$ python datalogi.py
```


## Local server

Du kan servere filerne med den her kommando, så relative paths etc virker.

``` bash
$ cd build
$ python -m http.server [port]
```
