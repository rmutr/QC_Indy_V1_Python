def read_data():
  n = int(input())
  d = [ int(input()) for i in range(n) ]
  return d
#-----------------------------------------------------
def get_mean(d):
  return sum(d)/len(d)
#-----------------------------------------------------
def get_median(d):
  sorted_d = sorted(d)
  n = len(d)
  return (sorted_d[(n-1)//2]+sorted_d[n//2])/2
#---------------------------------------------------
def get_mode(d):
  c = [d.count(e) for e in  d]
  maxcount = max(c)
  return d[c.index(maxcount)]
#---------------------------------------------------
x       = read_data()
mean    = get_mean(x)
median  = get_median(x)
mode    = get_mode(x)
print("mean =", mean,"median =", median,"mode =", mode)