import math
vectors = []
def create_vectors(vector_x,vector_y,matrix):
    height, width =  len(matrix), len(matrix[0])   
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
def distance(vector_x,vector_y,vectors,split_left,split_right):
    rows=vector_x
    cols=vector_y
    left_list=[]
    right_list=[]

    for vector in vectors:
        left_sum=0
        right_sum=0
        for i in range(rows):
            for j in range(cols):
                left_sum+= pow((vector[i * cols + j]-split_left[i][j]),2)
                right_sum+= pow((vector[i * cols + j]-split_right[i][j]),2)
        if left_sum<right_sum:
            left_list.append(vector)
        else:
            right_list.append(vector)
    return left_list,right_list

        
  
class Node:
    def __init__(self, avg,vectors):
        self.avg = avg
        self.left = None
        self.right = None
        self.vectors = vectors
def split(vectors, vector_x, vector_y):
    avg = calc_avg(vector_x, vector_y, vectors)
    node = Node(avg, vectors)
    left_vectors = []
    right_vectors = []
    

    for i in range(vector_x):
        left_rows = []
        right_rows = []
        for j in range(vector_y):
            left_rows.append(math.floor(avg[i][j]+1))
            right_rows.append(math.ceil(avg[i][j]-1))
        left_vectors.append(left_rows)
        right_vectors.append(right_rows)
    left_list, right_list = distance(vector_x, vector_y, vectors, left_vectors, right_vectors)
    if len(left_list) > 0 :
        node.left = Node(calc_avg(vector_x, vector_y, left_list), left_list)
    if len(right_list) > 0 :
     node.right = Node(calc_avg(vector_x, vector_y, right_list), right_list)
    
    return node
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)
def split_all_leaves(node, root,vector_x, vector_y, codewords):
    if count_leaves(root) >= codewords:
        return node
    if node.left is None and node.right is None:
        new_node = split(node.vectors, vector_x, vector_y)
        node.left = new_node.left
        node.right = new_node.right
    else:
        split_all_leaves(node.left, root, vector_x, vector_y, codewords)
        split_all_leaves(node.right, root, vector_x, vector_y, codewords)
    return node
def get_codewords(node, codewords):
    if node is None:
        return
    if node.left is None and node.right is None:
        codewords.append(node.avg)
    else:
        get_codewords(node.left, codewords)
        get_codewords(node.right, codewords)
    return codewords
def compress(matrix, vector_x, vector_y, codewords):
    vectors= create_vectors(vector_x, vector_y, matrix)
    avg = calc_avg(vector_x, vector_y, vectors)
    root=Node(avg, vectors)
    split_all_leaves(root, root, vector_x, vector_y, codewords)
    codewords_list=[]
    get_codewords(root, codewords_list)
    num_bits=(len(codewords_list)-1).bit_length()
    code_binary=[]
    for i in range(len(codewords_list)):
        code_binary.append(format(i, '0' + str(num_bits) + 'b'))
    compressed_data=""
    for vector in vectors:
        min_distance=float('inf')
        closest_codeword=None
        for codeword in codewords_list:
            distance=0
            for i in range(vector_x):
                for j in range(vector_y):
                    distance+=pow((vector[i * vector_y + j]-codeword[i][j]),2)
            if distance<min_distance:
                min_distance=distance
                closest_codeword=codeword
                code_index=codewords_list.index(closest_codeword)
        compressed_data+=code_binary[code_index]

    return compressed_data


    
    
    
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





              
def split(vector_x,vector_y,matrix):
    avg=[]
    for vector in vectors:  
      sum=0
      for i in vector_x:
        for j in vector_y:
            sum+=matrix[i][j]
    avg.append(sum/len(vector))



#avg
#asso
#split