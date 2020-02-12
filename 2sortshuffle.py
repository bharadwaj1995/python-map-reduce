unsorted = open("chalange_01.txt", "r")
sorted = open("chalange_02.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    sorted.write(line)

unsorted.close()
sorted.close()