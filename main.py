from PIL import Image
import numpy as np
def choice1():
    image_path = input("Enter image path: ")
    # x_of_vector=input("Enter the size (x) of the blocks: ")
    # y_of_vector=input("Enter the size (y) of the blocks: ")
    # num_of_vectors=input("Enter the number of blocks (vectors) in the codebook ")

    img = Image.open(image_path)
    img = img.convert("L")
    matrix = np.array(img)
    
    #for test
    print(img.size)
    print(matrix)



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