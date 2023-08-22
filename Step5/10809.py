s = input()
for i in range(ord('a'),ord('z')+1):
    print(s.find(chr(i)) if chr(i) in s else -1, end=" ")