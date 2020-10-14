def naiveLoop():
    nums = []
    for nn in range(10000000):
        nums.append(nn)

def comprehension():
    nums = [nn for nn in range(10000000)]


if __name__ == '__main__':
    from timeit import timeit
    
    t_naive = timeit(stmt='naiveLoop()', setup='from __main__ import naiveLoop', number=1)
    print("t_naive: ", t_naive)
    
    t_comp = timeit(stmt='comprehension()', setup='from __main__ import comprehension', number=1)
    print("t_comp: ", t_comp)