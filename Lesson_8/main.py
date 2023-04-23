# Генератор последовательностей
def my_generator(start, stop):
    while start < stop:
        yield start
        start += 1

# Тернарный оператор
def my_ternary(condition, true_value, false_value):
    return true_value if condition else false_value

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def my_function():
    print("Function called")

my_function()

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start, "seconds.")
        return result
    return wrapper

@timeit
def my_function():
    time.sleep(2)
    print("Function completed")

my_function()

import time

def create_list(stop):
    start = 1
    my_list = []
    while start <= stop:
        my_list.append(start)       
        start += 1
    return my_list

def create_generator(stop):
    start = 1
    while start <= stop:
        yield start
        start += 1
        start = time.time()
my_list = create_list(1000000)
end = time.time()
print("Time taken to create list:", end - start, "seconds.")

start = time.time()
my_generator = create_generator(1000000)
end = time.time()
print("Time taken to create generator:", end - start, "seconds.")
