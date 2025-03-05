import os

def checker(path):
    if os.path.exists(path):
        print("Путь существует.")
        
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        
        print("Имя файла:", filename)
        print("Директория:", directory)
    else:
        print("Путь не существует.")

path = input("Введите путь: ")

checker(path)