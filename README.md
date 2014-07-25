primelookup
=======

A quick document retrieval system built on the technique of mapping words within a corpus into 4n+3 prime based vectors. 

###Rationale:
We represent each word in the corpus by a unique vector identity i.e. vector containing mapping of the word's characters
to the primes of the form 4n+3. Any finite subset of these primes have elements which if multiplied together, can produce unique results, which help us identifying the closest or corresponding keywords.

###Usage:
```python
>>> from primelookup import primelookup
>>> data = [(id_1, 'document_1'), (id_2, 'document_2'), .. , (id_n, 'document_n')]
>>> pl = primelookup(data)
>>> pl.map_primes()
```
This will generate mappings and the time depends on the size of the corpus. Once the mappings are generated, a document can be queried via a `keyword` like:
```python
>>> pl.search(keyword)
>>> [(doc_id, score), (doc_id, score)..]
```
Note: Currently, only a single keyword based lookup is supported. Very soon, multiple keywords based and sentence based lookups will be added in.
