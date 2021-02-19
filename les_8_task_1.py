"""1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке."""

def count_str(str):
    result = set()
    for i in range(len(str)):
        for j in range(len(str)-1 if i == 0 else len(str), i, -1):
            result.add(hash(str[i:j]))
    return len(result)

print(count_str('papa'))
print(count_str('sova'))