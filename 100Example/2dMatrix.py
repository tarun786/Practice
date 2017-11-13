
row_col=input("enter the rows and colum")
dimentions=[int(x) for x in row_col.split(",")]
rows=dimentions[0]
cols=dimentions[1]
multilist=[[0 for col in range(cols)] for row in range(rows)]  #to make a matirx in python
#print(multilist)

for row in range(rows):
    for col in range(cols):
        multilist[row][col]=row*col;
print(multilist)

matrix=[[5][3]]
for rr in range(5):
    for cc in range(3):
        matrix[rr][cc]=0
print(matrix)