from PIL import Image
import numpy as np
import ast
from compress import compress
from decompress import decompress, decode
def save_compressed_files(compressed_data, codebook,
                          height, width, vector_x, vector_y):

    original_length = len(compressed_data)

    bits = compressed_data

    bits += '0' * ((8 - len(bits) % 8) % 8)

    byte_data = bytearray()

    for i in range(0, len(bits), 8):

        byte = bits[i:i+8]

        num = int(byte, 2)

        byte_data.append(num)

    with open("compressed.bin", "wb") as file:
        file.write(byte_data)

    with open("padding.txt", "w") as file:
        file.write(str(original_length))

    with open("codebook.txt", "w") as f:
        f.write(repr(codebook))

    with open("size_of_image.txt", "w") as f:

        f.write(f"{height}\n")
        f.write(f"{width}\n")
        f.write(f"{vector_x}\n")
        f.write(f"{vector_y}\n")
def choice1():

    image_path = input("Enter image path: ")

    x_of_vector = int(input("Enter the size (x) of the blocks: "))

    y_of_vector = int(input("Enter the size (y) of the blocks: "))

    num_of_vectors = int(input("Enter the number of blocks (vectors) in the codebook: "))

    img = Image.open(image_path)
    img = img.convert("L")

    matrix = np.array(img)

    height, width = matrix.shape

    compressed_data, codebook, ratio = compress(
        matrix,
        x_of_vector,
        y_of_vector,
        num_of_vectors
    )

    save_compressed_files(
        compressed_data,
        codebook,
        height,
        width,
        x_of_vector,
        y_of_vector
    )

    print("Compression completed successfully!")
    print("Compression ratio:", ratio)
    print("Files saved successfully!")

def decompress_image():

   
    with open("compressed.bin", "rb") as file:
        data = file.read()

    bits = ''.join(format(byte, '08b') for byte in data)

    
    with open("padding.txt", "r") as file:
        original_length = int(file.read())

    bits = bits[:original_length]

    
    with open("codebook.txt", "r") as file:
        codebook = ast.literal_eval(file.read())

    
    with open("size_of_image.txt", "r") as file:
        height = int(file.readline())
        width = int(file.readline())
        vector_x = int(file.readline())
        vector_y = int(file.readline())

    # 5. Decompress binary data into vectors
    vectors = decompress(bits, codebook)

    
    decode(vectors, height, width, vector_x, vector_y)

    print("Decompression completed successfully!")
    print("Image saved as decompressed.png")

def main():
    while True:
        print("\n===== Vector Quantization =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            choice1()

        elif choice == "2":
            decompress_image()

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()