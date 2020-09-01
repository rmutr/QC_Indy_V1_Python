infile = open("C:/temp/data.txt","r")
min_score = 1000
max_score = 0
ID = ""

for line in infile:
    score = float(line [10:] )
    if score > 0 :  
        if score < min_score:
            min_score = score
            ID_min = line[:10]
            
        elif score > max_score:
            max_score = score
            ID_max = line[:10]
    
infile.close()
print("min >> ","ID = ",ID_min,"Score =", min_score)
print("max >> ","ID = ",ID_max,"Score =", max_score)
