input = open("purchases.txt", "r")
output = open("chalange_01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time,store, item, cost, paymentType = datalist
    output.write(paymentType + "\t" + cost + "\n")

input.close()
output.close()