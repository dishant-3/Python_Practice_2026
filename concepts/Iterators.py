# class CountUp:
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high

#     def __iter__(self):
#         return self  # Returns the iterator object itself

#     def __next__(self):
#         if self.current > self.high:
#             raise StopIteration  # Tells Python the iteration is finished
#         else:
#             self.current += 1
#             return self.current - 1

# # Usage
# counter = CountUp(1, 3)
# print(next(counter))  # Outputs: 1
# print(next(counter))  # Outputs: 2
# print(next(counter))

class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Signal that we are done
        
        result = self.current
        self.current -= 1
        return result
    
count = CountdownIterator(3)

for num in count:
    print(num)

## Implementaion in for loop
# 1. Get an iterator from the iterable
_iterator = iter(numbers)  # Internally calls numbers.__iter__()

# 2. Start an infinite loop
while True:
    try:
        # 3. Fetch the next item
        num = next(_iterator)  # Internally calls _iterator.__next__()
        
        # 4. Execute the loop body
        print(num)
        
    except StopIteration:
        # 5. Cleanly catch the exception to exit the loop
        break