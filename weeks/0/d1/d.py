def gcd(a: int, b: int) -> int:
    """
    Взятый из гугла алгоритм Евклида для поиска НОД.

    """
    while b:
        a, b = b, a % b
    return a

# Я не знаю threading или multiprocessing, но результат должен быть тот же, ресурсы то не пересекаются
