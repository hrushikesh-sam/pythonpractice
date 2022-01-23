# generator functions are , python function that use the concepts of yield function to maintain the state of the function
#for example i am using a function thatprints the fibonacci sequence of range n using yeild()
def fibo():
    first_num = 0
    sec_num = 1
    yield sec_num
    while True:
        next_val = first_num + sec_num
        first_num,sec_num = sec_num,next_val
        yield next_val
# printing a fibonacci sequence of length 10
g = fibo()
for i in range(10):
    
    print(next(g))
# running the underlying program using generator functions will automatically print the next,
#  20 fibonacci sequence instead of re starting the sequence from first digit
for i in range(20):
    print(next(g))