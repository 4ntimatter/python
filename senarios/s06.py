def p_n():

    while True:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
        yield 6


gen1 = p_n()
for i in gen1:
    print(i)