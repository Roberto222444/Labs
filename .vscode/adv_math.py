def recursive_gcd(a, b):
# Базовий випадок
    if b == 0:
        return a
# Рекурсивний крок
    else:
        return recursive_gcd(b, a % b)