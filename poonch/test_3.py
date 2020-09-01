infile = open("C:/temp/data.txt","r")
line_count = 0
char_count = 0
for line in infile:
    line_count += 1
    char_count += len(line)
print(line_count,"lines",char_count,"chars")
infile.close()