import re

s = input()
entries = re.findall(r'student_(\d{3})(\d+)', s)

max_score = max(int(score) for _, score in entries)
winners = [num for num, score in entries if int(score) == max_score]
print('-'.join(winners))
