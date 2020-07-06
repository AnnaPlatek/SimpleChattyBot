a = int(input())
b = int(input())
def min_max(a, b):
    if a != b:
        min_value = min(a, b)
        max_value = max(a, b)
        print(max_value)
        print(min_value)
        return min_value, max_value
    else:
        print(a)
        print(b)
        return a, b

min_max(a, b)