import ast
from primelookup import primelookup

def gen_test():
    f = open('10.json', 'rb')
    y =[]
    for a in f:
        y.append(a)
    y = ast.literal_eval(y[0])
    y = map(lambda k: ' '.join(k['tags']), filter(lambda n: len(n['tags']) > 0, y))
    ids = range(0, len(y))
    data = zip(ids, y)
    fs = primelookup(data)
    fs.map_primes()
    return fs,data


fs, data = gen_test()
