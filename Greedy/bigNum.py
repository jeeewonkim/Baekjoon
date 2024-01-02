#큰 수의 법칙
#n(배열의 개수) m(숫자가 더해지는 횟수), k(최대로 반복될 수 있는)
n, m , k =map(int, input().split())
num = list(map(int, input().split()))
num.sort()
print((int(m/k)*num[-1]*k) + (int(m%k)*num[-2]))