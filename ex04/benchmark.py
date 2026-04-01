import random
from collections import Counter
import timeit

data = [random.randint(1, 100) for _ in range(1000000)]

def count_func(lst):    
    res = {}
    for items in lst:
        if items in res:
            res[items] += 1
        else:
            res[items] = 1
    return res

def top_ten_func(lst):
    counts = count_func(lst)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:10]

    


def counter(lst):
    return Counter(lst)

def counter_top(lst):
    counter = Counter(lst)
    return counter.most_common(10)


def main():

    time1 = timeit.timeit(lambda: count_func(data), number=1)
    print(f"my function: {time1:.7f}")

    time2 = timeit.timeit(lambda: counter(data), number=1)
    print(f"Counter: {time2:.7f}")

    time3 = timeit.timeit(lambda: top_ten_func(data), number=1)
    print(f"my top: {time3:.7f}")

    time4 = timeit.timeit(lambda: counter_top(data), number=1)
    print(f"Counter: {time4:.7f}")


if __name__ == "__main__":
    main()  