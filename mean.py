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


#finding mean
n = len( new_data)
sum = 0
for i in new_data:
    sum = sum + i
mean = sum/n
print(mean)
print("\n")


import statistics
print( statistics.mean( new_data)  )