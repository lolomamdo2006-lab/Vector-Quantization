import ast
import math
import numpy as np
from PIL import Image
def create_vectors(vector_x,vector_y,matrix):

    vectors = []
    height, width =  len(matrix), len(matrix[0]) 
    with open("size_of_image.txt", "w") as f:
        f.write(f"{height}\n{width}\n{vector_x}\n{vector_y}\n" ) 
    for i in range(0, height, vector_x):
        for j in range(0, width,vector_y):
            vector = []
            for x in range(vector_x):
                for y in range(vector_y):
                    if i+x < height and j+y < width:
                        vector.append(matrix[i+x][j+y])
                    else:
                        vector.append(0)
            vectors.append(vector)
    return vectors
def calc_avg(vectors):
    if not vectors:
        return []
    length = len(vectors[0])
    avg = [0] * length
    for vector in vectors:
        for i in range(length):
            avg[i] += vector[i]
    for i in range(length):
       avg[i] = round(avg[i] / len(vectors), 1)
    return avg
def split_vector(vector):
    v1 = []
    v2 = []
    for i in range(len(vector)):
        val = vector[i]
        if int(val) == val:
            v1.append(int(val) - 1)
            v2.append(int(val) + 1)
        else:
            v1.append(int(val))
            v2.append(int(val) + 1)
    return v1, v2
def calc_distance(v1, v2):
    total = 0
    for i in range(len(v1)):
        diff = v1[i] - v2[i]
        if diff < 0:
            diff = -diff
        total = total + diff
    return total
def assign_and_update(vectors, codebook, codebook_size):
    data = [[] for _ in range(len(codebook))]
    for vector in vectors:
        minimum = float('inf')
        i = 0
        for idx, c in enumerate(codebook):
            distance = calc_distance(vector, c)
            if distance < minimum:
                minimum = distance
                i = idx
        data[i].append(vector)

    new_codebook = []
    for k, sub_data in enumerate(data):
        if sub_data:
         new_codebook.append(calc_avg(sub_data))
        else:
         new_codebook.append(codebook[k])
    return new_codebook
def compress(vectors, codebook_size):
    codebook = [calc_avg(vectors)]
    while len(codebook) < codebook_size:
        splitted = []
        for c in codebook:
            v1, v2 = split_vector(c)
            splitted.append(v1)
            splitted.append(v2)
        codebook = assign_and_update(vectors, splitted,codebook_size)
    while True:
        new_codebook = assign_and_update(vectors, codebook,codebook_size)
        if new_codebook == codebook:
            break
        codebook = new_codebook
    return encode(vectors,codebook, codebook_size)

def encode(vectors, codebook, codebook_size):
    dic = {}
    bits = math.ceil(math.log2( codebook_size))
    for vector in vectors:
        minimum = float('inf')
        index = -1
        for i, c in enumerate(codebook):
            distance = calc_distance(vector, c)
            if distance < minimum:
                minimum = distance
                index = i
        dic[tuple(vector)] = format(index, f'0{bits}b')


    bits=""
    for vector in vectors:
     bits+=(dic[tuple(vector)])
    original_length = len(bits)
    bits += '0' * ((8 - len(bits) % 8) % 8)
    byte_data = bytearray()
    for i in range (0,len(bits),8):
        byte=bits[i:i+8]
        num=int(byte,2)
        byte_data.append(num)
    with open("compressed.bin", "wb") as file:
        file.write(byte_data)
    with open("padding.txt", "w") as file:
        file.write(str(original_length))
    clean_codebook = [[float(v) for v in codeword] for codeword in codebook]
    with open("codebook.txt", "w") as f:
        f.write(str(clean_codebook))
    return bits
      
        
def decompress():
    with open("compressed.bin", "rb") as f:
        data = f.read()
    bits=""
    for byte in data:
        bits += format(byte, '08b')
    with open("padding.txt", "r") as f:
        original_length = int(f.read())
    bits= bits[:original_length]

    with open("codebook.txt", "r") as f:
        codebook = ast.literal_eval(f.read())
    codebook_size=len(codebook)
    n=math.ceil(math.log2(codebook_size)) 
    vectors=[]
    for i in range(0,len(bits),n):
        index = int(bits[i:i+n], 2)         
        vectors.append(codebook[index])   
    with open("size_of_image.txt", "r") as f:
        height = int(f.readline())
        width = int(f.readline())
        vector_x = int(f.readline())
        vector_y = int(f.readline())
    decode(vectors,height,width,vector_x,vector_y)
def decode(vectors,height,width,vector_x,vector_y):
    img = np.zeros((height, width), dtype=np.uint8)
    k=0
    for i in range(0, height, vector_x):
        for j in range(0, width,vector_y):
            vector = vectors[k]
            k+=1
            p=0
            for x in range(vector_x):
                for y in range(vector_y):
                    if i+x < height and j+y < width:
                        img[i+x][j+y]=round(vector[p])
                    p+=1
    Image.fromarray(img).save("decompressed.png")
matrix=[
    [1,2,7,9,4,11],
    [3,4,6,6,12,12],
    [4,9,15,14,9,9],
    [10,10,20,18,8,8],
    [4,3,17,16,1,4],
    [4,5,18,18,5,6]
]
m=create_vectors(2,2,matrix)

print(compress(m,4))
