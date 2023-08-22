score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0 , 1.5, 1.0, 0.0]
grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
total_subject = []
total=0.0
total_score =0

for i in range(20):
    subject = input().split()
    total_subject.append(subject)
for j in total_subject:
        if j[2] == "P":
            continue
        else:
            total += float(j[1])*score[grade.index(j[2])]
            total_score += float(j[1])
        
print('%.6f' % (total/total_score))