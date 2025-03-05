import string

def gener_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("Рello,  world!")

if __name__ == "__main__":
    gener_files()