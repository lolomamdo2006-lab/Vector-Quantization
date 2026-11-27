import math

def create_vectors(vector_x,vector_y,matrix):
    vectors = []
    height, width =  len(matrix), len(matrix[0])   
    height, width =  len(matrix), len(matrix[0])   
    for i in range(0, height, vector_x):
        for j in range(0, width,vector_y):
            vector = []
            for x in range(vector_x):
                for y in range(vector_y):
                    vector.append(int(matrix[i+x][j+y]))
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
            avg[i][j]= avg[i][j]/len(vectors)
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
            left_avg = math.floor(avg[i][j])
            right_avg = math.ceil(avg[i][j])
            if (left_avg == right_avg):
                left_avg -= 1
                right_avg += 1
            left_rows.append(left_avg)
            right_rows.append(right_avg)
        left_vectors.append(left_rows)
        right_vectors.append(right_rows)
    left_list, right_list = distance(vector_x, vector_y, vectors, left_vectors, right_vectors)
    while(True):
        old_left_list = left_list.copy()
        old_right_list = right_list.copy()
        if len(left_list) == 0 or len(right_list) == 0:
            break
        left_avg = calc_avg(vector_x, vector_y, left_list)
        right_avg = calc_avg(vector_x, vector_y, right_list)
        left_list, right_list = distance(vector_x, vector_y, left_list+right_list, left_avg, right_avg)
        if old_left_list == left_list and old_right_list == right_list:
            break
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


def split_all_leaves(node, root, vector_x, vector_y, codewords):

    if count_leaves(root) >= codewords:
        return node
 
    if node.left is None and node.right is None:

        
        if len(node.vectors) <= 1:
            return node

        new_node = split(node.vectors, vector_x, vector_y)

        if new_node.left is None or new_node.right is None:
            return node

        node.left = new_node.left
        node.right = new_node.right

        
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
    num_bits=max(1, (len(codewords_list)-1).bit_length())
    code_binary={}
    for i in range(len(codewords_list)):
        binary=(format(i, '0' + str(num_bits) + 'b'))
        code_binary[binary]=codewords_list[i]

    compressed_data=""
    for vector in vectors:
        min_distance=float('inf')
        closest_codeword=None
        for binary, codeword in code_binary.items():
            distance=0
            for i in range(vector_x):
                for j in range(vector_y):
                    distance+=pow((vector[i * vector_y + j]-codeword[i][j]),2)
            if distance<min_distance:
                min_distance=distance
                closest_binary=binary
                
        compressed_data+=closest_binary

    return compressed_data,code_binary,((vector_x * vector_y * 8) / num_bits)

   

    
    
    




            