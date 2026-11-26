from PIL import Image
import numpy as np
from compress import *
def choice1():
    image_path = input("Enter image path: ")
    x_of_vector = int(input("Enter the size (x) of the blocks: "))
    y_of_vector = int(input("Enter the size (y) of the blocks: "))
    num_of_vectors = int(input("Enter the number of vectors in the codebook: "))

    img = Image.open(image_path)
    img = img.convert("L")
    matrix = np.array(img)
    matrix = matrix.astype(int)
    m = create_vectors(x_of_vector, y_of_vector, matrix)
    result = compress(m, num_of_vectors)
    print (result)
    



def main():
    while True:
        print("\n===== Vector Quantization =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            choice1();

        elif choice == "2":
            pass

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()