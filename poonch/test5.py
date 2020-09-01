infile = open("C:/temp/data.txt","r")
min_score = 1000
max_score = 0

for line in infile:
    score = float(line [10:] )
    if score < min_score:
        min_score = score
    if score > max_score:
        max_score = score
infile.close()
print("min = ",min_score)
print("max = ",max_score)