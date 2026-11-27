from PIL import Image
import numpy as np
import ast

def decompress(compressed_data, codebook):

    decompressed_vectors = []

    num_bits = max(1, (len(codebook) - 1).bit_length())

    for i in range(0, len(compressed_data), num_bits):

        binary = compressed_data[i:i + num_bits]

        decompressed_vectors.append(codebook[binary])

    return decompressed_vectors


def decode(vectors, height, width, vector_x, vector_y):

    img = np.zeros((height, width), dtype=np.uint8)

    k = 0

    for i in range(0, height, vector_x):
        for j in range(0, width, vector_y):

            vector = vectors[k]
            k += 1

            for x in range(vector_x):
                for y in range(vector_y):

                    if i+x < height and j+y < width:
                        img[i+x][j+y] = round(vector[x][y])

    Image.fromarray(img).save("decompressed.png")