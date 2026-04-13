s = input()
check = s[:4] if len(s) >= 4 else s
upper_count = sum(1 for c in check if c.isupper())
threshold = 3 if len(s) >= 4 else len(check)
print(s.upper() if upper_count >= threshold else s)
