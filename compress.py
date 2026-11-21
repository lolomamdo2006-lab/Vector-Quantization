blocks = []
def create_vectors(block_x,block_y,matrix):
    height, width = matrix.shape    
    for i in range(0, height, block_x):
        for j in range(0, width, block_y):
            vector = []
            for x in range(block_x):
                for y in range(block_y):
                    vector.append(matrix[i+x][j+y])
            blocks.append(vector)
def split():
#avg
#asso
#split