import sys
import timeit
from functools import reduce

def main():
    
    if len(sys.argv) != 4:
        return

    name_func = sys.argv[1]
    count_iteration = int(sys.argv[2])
    num = int(sys.argv[3])

    if (name_func == "loop"):
        time1 = timeit.timeit(lambda: loop(num), number=count_iteration)
        print(time1)
    elif(name_func == "reduce"):
        time2 = timeit.timeit(lambda: reduce_sum(num), number=count_iteration)
        print(time2)
    else:
        return



def loop(num):
    res = 0

    for i in range(num + 1):
        res += i * i

    return res


def reduce_sum(num):
    red = [i * i for i in range(num + 1)]
    return reduce(lambda x, y: x + y, red)

if __name__ == "__main__":
    main()