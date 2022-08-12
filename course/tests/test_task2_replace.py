import os

from home_tasks.task2_replace import replace


def test_replace():
    assert replace("Hello World", "World", "Universe") == "Hello Universe"
    assert replace("Hello World", "l", "L", 1) == "HeLlo World"
    assert replace("HeLLo World", "l", "L", 2) == "HeLlo World"
    assert replace("Hello World", "l", "lolo", 2) == "Helolololo World"
    assert replace("Hello World", "l", "lolo") == "Helolololo Worlolod"
    assert replace("Hello World", "l", "lolo", 0) == "Hello World"
    assert replace("Hello World", "World", f"{os.getlogin()}, Great job!") == \
        f"Hello {os.getlogin()}, Great job!"
