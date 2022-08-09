from python_basics import run


def passing_arguments(arg1: int, arg2: int) -> int:
    return run.sum(arg1, arg2)

if __name__ == "__main__":
    print(passing_arguments(1, 2))