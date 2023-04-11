#1. Генератор последовательностей
def my_sequence_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


Тернарный оператор

def my_ternary_operator(a, b):
    return a if a > b else b


#2. Декоратор
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator is working")
        result = func(*args, **kwargs)
        return result
    return wrapper


#3. Декоратор, замеряющий время выполнения
from time import time


def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Execution time: {}".format(end - start))
        return result
    return wrapper


#4. Сравнение времени создания генератора и списка
def generate_sequence_using_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


@time_execution
def time_list_creation(n):
    my_list = generate_sequence_using_list(n)


@time_execution
def time_generator_creation(n):
    my_generator = my_sequence_generator(n)
    for i in my_generator:
        pass


#5. Декоратор, замеряющий объем оперативной памяти
import psutil


def memory_usage(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024
        result = func(*args, **kwargs)
        memory_after = process.memory_info().rss / 1024 / 1024
        print("Memory usage: {} MB".format(memory_after - memory_before))
        return result
    return wrapper


#6. Сравнение объема оперативной памяти для функции создания генератора и списка
@memory_usage
def memory_list_creation(n):
    my_list = generate_sequence_using_list(n)


@memory_usage
def memory_generator_creation(n):
    my_generator = my_sequence_generator(n)
    for i in my_generator:
        pass

