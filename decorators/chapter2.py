import time


def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def longrunningfunction(a,b):
    time.sleep(4)
    return a+b

print(longrunningfunction(2,3))
print(longrunningfunction(4,3))