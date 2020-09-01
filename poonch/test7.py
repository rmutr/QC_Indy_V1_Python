n = int(input("Enter the number of data : "))
data = []
for i in range(n):
  x = float(input(">> ") )
  data.append(x)

counts = [0]*n
for i in data :
  for j in counts  :
    if data[i] == data[j] :
      counts[i] += 1

maxI = 0
for i in maxI :
  if counts[maxI] < counts[i]:
    maxI = i

print("mode =", data[maxI])