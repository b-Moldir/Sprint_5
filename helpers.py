import random
import string

def generate_random_string(length):
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_courier_payload():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }