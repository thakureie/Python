#advanced iteration functions in the itertools package

import itertools

def testFunction(x):
    if x <40:
        retrun True
    return False

def main():

    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]

    seq2 = itertools.cycle(seq1)
    print(next(seq2))
    print(next(seq2))
    print(next(seq2))
    print(next(seq2))
    print(next(seq2))

    # TODO: use count to create a simple counter

    count1 = itertools.count(1, 50)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]

    accumulate1 = itertools.accumulate(vals, max)   
    print(list(accumulate1))   
    # TODO: use chain to connect sequences together
    chain1= itertools.chain("ABCD", "1234")
    print(list(chain1))
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them

    print(list(itertools.dropwhile(testFunction, vals)))
if __name__ == "__main__":
    main()
