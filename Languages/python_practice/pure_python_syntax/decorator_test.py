def big_number1(n):
    return n ** n ** n

def make_func_alarm(func):
    def new_func(*args, **kwargs):
        print("Function starts")
        result = func(*args, **kwargs)
        print("Function ends")
        return result
    return new_func

my_fun = make_func_alarm(big_number1)
print(my_fun(6))


from time import perf_counter

def make_time_checker(func):
    def new_func(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print("Running time: ", end_time - start_time)
        return result
    return new_func

my_fun = make_time_checker(big_number1)
my_fun(6)

@make_time_checker # Passes big_number2 as a parameter of make_time_checker
def big_number2(n):
    return n ** n ** n

big_number2(6)


def fun1(a, b):
    print("fun1 실행")
    return a + b
print(fun1.__name__)
myfun1 = fun1
myfun1(10, 20)
print(myfun1.__name__)

def check_func_name(func):
    print("함수 이름: ", func.__name__)
check_func_name(myfun1)

def decorator(func):
    def new_func(*args, **kwargs):
        print("데코레이터 적용한 함수")
        result = func(*args, **kwargs)
        return result
    return new_func
@decorator
def add_a_b1(a, b):
    return a + b
print(add_a_b1(11, 22))

check_func_name(add_a_b1)


from functools import wraps

def deco_wraps1(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        print("데코레이터와, 랩스를 데코레이터로 적용한 함수")
        result = func(*args, **kwargs)
        return result
    return new_func

@deco_wraps1
def add_a_b2(a, b):
    return a + b

check_func_name(add_a_b2)

def deco_wraps2(func):
    def new_func(*args, **kwargs):
        print("데코레이터와, 랩스를 비 데코레이터로 적용한 함수")
        result = func(*args, **kwargs)
        return result
    return wraps(func)(new_func)

@deco_wraps2
def add_a_b3(a, b):
    return a + b

check_func_name(add_a_b3)
