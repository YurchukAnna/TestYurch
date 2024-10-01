def create_cipher_table(slogan):
    # Удаляем дубликаты и приводим к нижнему регистру
    unique_letters = []
    for char in slogan:
        if char not in unique_letters and char.isalpha():
            unique_letters.append(char.lower())

    # Русский алфавит
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Получаем оставшиеся буквы алфавита
    remaining_letters = [char for char in russian_alphabet if char not in unique_letters]

    # Формируем таблицу
    cipher_table = unique_letters + remaining_letters
    return cipher_table

def encrypt(text, cipher_table):
    # Шифруем текст
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            index = ord(char.lower()) - ord('а')
            encrypted_text += cipher_table[index]
        else:
            encrypted_text += char  # Не шифруем не буквенные символы
    return encrypted_text

# Лозунг
slogan = "заявление"

# Создаем таблицу шифрования
cipher_table = create_cipher_table(slogan)

# Читаем текст для шифрования из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text_to_encrypt = file.read()

# Шифруем текст
encrypted_text = encrypt(text_to_encrypt, cipher_table)

# Выводим результаты
print("Таблица шифрования:", cipher_table)
print("Зашифрованный текст:", encrypted_text)