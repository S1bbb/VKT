def count_upper_lower(s):
    up = 0
    low = 0
    for c in s:
        if "A" <= c <= "Z":
            up += 1
        elif "a" <= c <= "z":
            low += 1
    return up, low


s = input()
print(count_upper_lower(s))
