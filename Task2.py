def find_pythagorean_triplets(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):  # b >= a для уникнення дублікатів
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                triplets.append((a, b, int(c)))
    return triplets

# Задання значення n без використання input
n = 20  # Можна змінити на будь-яке інше значення
print(find_pythagorean_triplets(n))