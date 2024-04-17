byte = int(input())
result = ""
for i in range(1, int(byte/4)+1):
    result+="long "
print(result + "int")