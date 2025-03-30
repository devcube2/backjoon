import sys

read = sys.stdin.readline

grade_dict = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
    "F": 0.0, "P": 0.0
}

score_sum = 0
subject_sum = 0
for _ in range(20):
    line = read().rstrip()
    if line == '':
        break
    subject, score, grade = line.split()
    if grade == 'P': # grade 가 P 면 계산 제외
        continue
    score_sum += float(score)
    subject_sum += float(score) * grade_dict[grade]
print(subject_sum / score_sum)
