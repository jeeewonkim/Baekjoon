#성적이 낮은 순서로 학생 출력하기

n = int(input())
student = [list(map(str,input().split())) for _ in range(n)]
student.sort(key = lambda info : int(info[1]))
for i in student:
    print(i[0], end = ' ')
