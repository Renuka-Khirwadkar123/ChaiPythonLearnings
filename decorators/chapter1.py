def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(args) for arg in args)
        kwargs_value=', '.join(f"{k}:{v}" for k,v in kwargs.items())
        print(f"Calling {func.__name__} with  args {args_value} and kwargs {kwargs_value} executed")
        return func(*args,**kwargs)
       
        return result
    return wrapper



@debug
def greet(name,greeting="Hello"):
    print(f"{name} {greeting} !")


greet("Hanji")