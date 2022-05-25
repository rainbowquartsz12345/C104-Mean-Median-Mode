import csv

with open('height-weight.csv',newline='') as f:
     r = csv.reader( f )
     file_data = list( r )

file_data.pop(0)

new_data = []
for i in range( len(file_data) ):
     num = file_data[i][1] # height column
     #type casting to float or else the value after point will not be there
     new_data.append( float(num) )


#finding median
n = len( new_data)
new_data.sort()
# % is called modulo symbol - finds the remainder

#using floor division to get the nearest whole number
# floor division is shown by //

if n% 2== 0:
    m1 = float( new_data[n//2] )
    m2 = float(new_data[n//2 - 1])
    median = (m1+m2)/2 
else:
    median = new_data[n//2]
print(median)
print("\n")


import statistics
print(statistics.median(new_data))

print(f"Median of the data is :   { statistics.median(new_data) }  ")
