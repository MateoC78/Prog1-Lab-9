def encoder(password):
    for i in range(8):
         password += (3*10**i)
    return password

if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")