def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return b - a

def multily(a: int, b: int) -> int:
    return a*b

def divide(a: int, b: int) -> int:
    return b//a

def test_add() -> None:
    assert add(1,1) == 11

def test_subtract() -> None:
    assert subtract(2,5) == 3

def test_multiply() -> None:
    assert multily(10,10) == 100

def test_divide() -> None:
    assert divide(25,100) == 4
