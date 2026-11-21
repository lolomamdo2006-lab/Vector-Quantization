vectors = []
def create_vectors(vector_x,vector_y,matrix):
    height, width = matrix.shape    
    for i in range(0, height, vector_x):
        for j in range(0, width,vector_y):
            vector = []
            for x in range(vector_x):
                for y in range(vector_y):
                    vector.append(matrix[i+x][j+y])
            vectors.append(vector)
def split(vector_x,vector_y,matrix):
    avg=[]
    for vector in vectors:  
      pass
    


#avg
#asso
#split