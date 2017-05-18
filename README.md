# nlp_sockets

Playing with django's channels and word2vec

## what's it do?

This program hosts a site at `localhost:8000` that does word 'addition'

Using word2vec, it takes in a list of input words to `add`, and to `subtract`, and performs an appropriate word2vec calculation, returning the result via channels from the server.

Some of the answers are a little funny because of the data type - encyclopedia entries in Wikipedia - and the sample size.

## getting started

Install requirements from `requirements.txt` and run `python manage.py runserver` to start

The word corpuses used for `word2vec` were generated from the first 10^8 bytes of wikipedia data.

To generate your own corpus, follow instructions [here](https://radimrehurek.com/gensim/models/word2vec.html) and leave the appropriately named files in the assets folder