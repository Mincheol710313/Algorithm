total_score = 0
total_credit = 0

for _ in range(20):
    _, credit, score = input().split()
    if score == 'P':
        continue
    total_credit += float(credit)
    if score == 'A+':
        total_score += 4.5 * float(credit)
    elif score == 'A0':
        total_score += 4.0 * float(credit)
    elif score == 'B+':
        total_score += 3.5 * float(credit)
    elif score == 'B0':
        total_score += 3.0 * float(credit)
    elif score == 'C+':
        total_score += 2.5 * float(credit)
    elif score == 'C0':
        total_score += 2.0 * float(credit)
    elif score == 'D+':
        total_score += 1.5 * float(credit)
    elif score == 'D0':
        total_score += 1.0 * float(credit)
    elif score == 'F':
        total_score += 0

result = total_score / total_credit
print(f"{result:0.6f}")
