import time
import logging

logging.basicConfig(level=logging.INFO)


def log_and_cache(func):
    cache = {}
    
    def wrapper(*args, **kwargs):
        cache_key = (args, frozenset(kwargs.items()))
        
        if cache_key in cache:
            logging.info(f'\tReturning cache value for {func.__name__} with args={args} and kwargs={kwargs}')
            return cache[cache_key]

        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
        except Exception as e:
            logging.error(f'Error on function {func.__name__} with args={args} and kwargs={kwargs}')
            raise e
        finally:
            end_time = time.time()
            elapsed_time = end_time - start_time
            logging.info(f'Function {func.__name__} executed in {elapsed_time:.4f} seconds')
            
    return wrapper


@log_and_cache
def expensive_computation(a: int, b: int):
    time.sleep(2)
    return a * b

print(expensive_computation(3, 4))
print(expensive_computation(3, 4))

try:
    print(expensive_computation(3, 'x'))
except TypeError:
    print('Type error')
            