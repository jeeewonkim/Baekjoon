aToz = [chr(i) for i in range(65,91)]
tenAToZ = [j for j in range(10, 36)]
n, b = map(str, input().split())
end = 0
result =0
for i in range(len(n)-1,-1,-1):
    if n[end] in aToz:
        result += tenAToZ[aToz.index(n[end])]*int(b)**i
    else:
        result += int(n[end])*int(b)**i
    end+=1

print(result)