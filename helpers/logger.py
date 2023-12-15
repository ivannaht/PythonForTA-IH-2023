from time import perf_counter


def logger_with_arguments(outer_message, start_message, finish_message):
    """decorator for functions with any arguments"""
    def decorator(fun):
        print(f"{outer_message} {fun.__name__}")

        def wrapper_accepting_arguments(*args, **kwargs):
            start_time = perf_counter()
            print(start_message)
            print(f"The arguments are: {args}")
            print(f"result:\n{fun(*args, **kwargs)}")
            print(f"{finish_message} in {(perf_counter() - start_time): .6f} seconds")

        return wrapper_accepting_arguments

    return decorator
