num = int(input())
digits = [int(digit) for digit in str(num)]
r_digits = sorted(digits, reverse=True)
p = "".join(map(str, r_digits))
print(p)