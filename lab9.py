def encoder(p):
    x = [int(y) for y in str(p)]
    y = ""
    for i in range(8):
        x[i] += 3
        if x[i] > 9:
            x[i] -= 10
        y += str(x[i])
    return y

def decoder(password: str) -> str:
    decoded = ""
    for i in password:
        num = int(i)-3
        if num < 0:
            num +=10
        decoded = decoded + str(num)
    return decoded


if __name__ == "__main__":
    x = 0
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")
        if choice == '1':
            password = int(input("Please enter your password to encode: "))
            x = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif choice == '2':
            print(f"The encoded password is {x}, and the original password is {decoder(x)}.\n")
            pass
        elif choice == '3':
            break