# iterators are objects that are more efficient in space and time complexity tha a list
import itertools
l1 = [10,2,3,4,5,6,7,8]
l2 = [1,2,3,4,5,6,7,9]
l3 = [12,3,4455,67,8,95,4]
i = itertools.chain(l1,l2,l3)
# iter tools chain function creates a iterator which is the amalgamation three listes l1,l2,l3
for l in i:
    print(l)
l4 = [12,13,14,16,17]
count = 0
for val in itertools.cycle(l4):
    # itertools.cycle creates an infinite iterable with l4
    if count< 20:
        print(val)
    else:
        break
    count+=1
# iterator once it has been iterated over will be exhausted to create two iterable we use .tee
#  functions to create multiple iterable with iter functionality
i = iter(l1)
t = itertools.tee(i)
print(t)
# iterators have to be sliced using islice method as they are an exception from normal lists
for value in itertools.islice(i,0,6):
    print(value)
# itertools have the functions to generate all the premutations
l = [1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))