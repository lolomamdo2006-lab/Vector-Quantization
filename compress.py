vectors = []
def create_vectors(vector_x,vector_y,matrix):
    height, width =  len(matrix), len(matrix[0])   
    for i in range(0, height, vector_x):
        for j in range(0, width,vector_y):
            vector = []
            for x in range(vector_x):
                for y in range(vector_y):
                    vector.append(matrix[i+x][j+y])
            vectors.append(vector)
    return vectors
def calc_avg(vector_x,vector_y,vectors):
    rows=vector_x
    cols=vector_y
    avg=[]
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        avg.append(row)
    for vector in vectors:
        for i in range(rows):
            for j in range(cols):
                avg[i][j]+=vector[i * cols + j]
    for i in range(rows):
        for j in range(cols):
            avg[i][j]= round(avg[i][j]/len(vectors),1)
    return avg
  
def split(vector_x,vector_y,matrix):
    avg=[]
    for vector in vectors:  
      pass
    
matrix=[
    [1,2,7,9,4,11],
    [3,4,6,6,12,12],
    [4,9,15,14,9,9],
    [10,10,20,18,8,8],
    [4,3,17,16,1,4],
    [4,5,18,18,5,6]
]
m=create_vectors(2,2,matrix)
for i in m: print (i)
print(calc_avg(2,2,m))
#avg
#asso
#split