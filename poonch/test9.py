infile = open ("C:/temp/data2.txt","r" )

for line in infile:
    sum1 = 0
    x = line.split("\n")
    y = float(line)
    sum1 += y

print("sum =",sum1)

