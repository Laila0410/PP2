def writesome(list_of_elements):
    # Открываем файл в режиме добавления
    with open("sometext.txt", 'a') as f:
        # Преобразуем элементы списка в строку, разделяя их пробелами
        text = ' '.join(map(str, list_of_elements))
        # Добавляем символ новой строки и записываем в файл
        f.write(text + '\n')

# Пример использования
writesome(["laila", "kazyna", "popoooo"])