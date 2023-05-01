import copy

from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


def permutations(lst):
    s = ArrayStack()
    q = ArrayQueue()

    for i in lst:
        s.push(i)

    q.enqueue([s.pop()])

    while not s.is_empty():
        first_val = s.pop()

        for i in range(len(q)):
            next_val = q.dequeue()

            for i in range(len(next_val) + 1):
                temp = copy.deepcopy(next_val)
                temp.insert(i, first_val)
                q.enqueue(temp)

    res = []
    for i in range(len(q)):
        res.append(q.dequeue())
    return res


