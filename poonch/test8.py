in_line = input ("Birthdate (dd/mm/yyyy) : " )
[d,m,y] = in_line.split("/")

month_names =["January", "February", "March", \
              "April", "May", "June", \
              "July", "August", "September", \
              "October", "November", "December" ]
month = month_names[int(m)-1]
print("You were born on" , d, month, y)