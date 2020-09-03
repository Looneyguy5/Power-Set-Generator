n = int(input("Enter length of set:\n"))
userList = [input(">>>") for i in range(n)]
powerSet = [None]*(2**n)
for i in range(2**n):
    binaryI = (format(i, 'b'))[::-1]
    subsetI = []
    for j in range(len(binaryI)):
        if binaryI[j] == "1":
            subsetI.append(userList[j])
    powerSet[i] = subsetI
print(powerSet)