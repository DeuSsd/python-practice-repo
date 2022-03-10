import time


def count_time(function):
    def inner_function(*args, **kwargs):
        t_start = time.time()
        result = function(*args, **kwargs)
        t_end = time.time()
        print(f"Время выполнения функции - {round(t_end - t_start, 3)}")
        return result

    return inner_function



def delay_finish(time_sleep:int = 1):
    def inner_function_delay_finish(function):
        def inner_funct(*args, **kwargs):
            result = function(*args, **kwargs)
            time.sleep(time_sleep)
            return result
        return inner_funct
    return inner_function_delay_finish

