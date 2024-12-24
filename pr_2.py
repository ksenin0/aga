import getpass
import os

# Данные о пользователях
users = {
    'admin': {'password': 'admin', 'role': 'admin'},
}

# Данные об играх
games = [
    {
        'id': 1,
        'title': 'Game of Thrones',
        'developer': 'Telltale Games',
        'genre': 'Adventure',
        'release_date': '2014-12-02'
    },
    {
        'id': 2,
        'title': 'The Witcher 3: Wild Hunt',
        'developer': 'CD Projekt Red',
        'genre': 'RPG',
        'release_date': '2015-05-19'
    }
]

# Библиотеки пользователей
libraries = {}

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    """Вход в систему"""
    username = input("Введите имя пользователя: ")
    password = getpass.getpass(prompt="Введите пароль: ")
    
    if username in users and users[username]['password'] == password:
        return username
    else:
        print("Неверный логин или пароль.")
        return None

def register():
    """Регистрация нового пользователя"""
    username = input("Введите имя пользователя: ")
    while username in users:
        print(f"Пользователь {username} уже существует. Попробуйте другое имя.")
        username = input("Введите новое имя пользователя: ")
        
    password = getpass.getpass(prompt="Введите пароль: ")
    confirm_password = getpass.getpass(prompt="Подтвердите пароль: ")
    
    if password != confirm_password:
        print("Пароли не совпадают. Пожалуйста, попробуйте снова.")
        return
    
    users[username] = {'password': password, 'role': 'user'}
    libraries[username] = []
    print(f"Учетная запись {username} успешно создана!")
    login()

def add_game():
    """Добавить новую игру"""
    title = input("Название игры: ")
    developer = input("Разработчик: ")
    genre = input("Жанр: ")
    release_date = input("Дата выпуска (YYYY-MM-DD): ")
    
    new_id = max([game['id'] for game in games]) + 1 if len(games) > 0 else 1
    new_game = {
        'id': new_id,
        'title': title,
        'developer': developer,
        'genre': genre,
        'release_date': release_date
    }
    games.append(new_game)
    print(f"Игра '{title}' была успешно добавлена.")

def delete_game(game_id):
    """Удалить игру по ID"""
    global games
    games = [game for game in games if game['id'] != game_id]
    print(f"Игра с ID {game_id} была удалена.")

def view_games(sort_by=None, filter_by=None):
    """Просмотреть список игр"""
    filtered_games = games.copy()
    
    # Фильтрация
    if filter_by is not None:
        key, value = filter_by.split(':')
        filtered_games = [game for game in filtered_games if game[key].lower() == value.lower()]
    
    # Сортировка
    if sort_by is not None:
        sorted_games = sorted(filtered_games, key=lambda x: x[sort_by])
    else:
        sorted_games = filtered_games
    
    for game in sorted_games:
        print(f"{game['id']} | {game['title']} | {game['developer']} | {game['genre']} | {game['release_date']}")

def search_game(query):
    """Поиск игры по названию, разработчику или жанру"""
    results = [game for game in games if query.lower() in game['title'].lower() or query.lower() in game['developer'].lower() or query.lower() in game['genre'].lower()]
    if results:
        print("Результаты поиска:")
        for result in results:
            print(f"{result['id']} | {result['title']} | {result['developer']} | {result['genre']} | {result['release_date']}")
    else:
        print("К сожалению, ничего не найдено.")

def add_to_library(username, game_id):
    """Добавить игру в библиотеку пользователя"""
    user_lib = libraries[username]
    for game in games:
        if game['id'] == game_id:
            user_lib.append(game)
            break
    print(f"Игра с ID {game_id} была добавлена в вашу библиотеку.")

def view_library(username):
    """Просмотреть библиотеку пользователя"""
    user_lib = libraries[username]
    if user_lib:
        print("Ваша библиотека:")
        for game in user_lib:
            print(f"{game['id']} | {game['title']} | {game['developer']} | {game['genre']} | {game['release_date']}")
    else:
        print("Ваша библиотека пуста.")

def main_menu(user):
    """Главное меню"""
    role = users[user]['role']
    options = {
        'user': {
            '1': ('Просмотреть все игры', lambda: view_games()),
            '2': ('Найти игру', lambda: search_game(input("Введите название, разработчика или жанр для поиска: "))),
            '3': ('Добавить игру в библиотеку', lambda: add_to_library(user, int(input("Введите ID игры: ")))),
            '4': ('Просмотреть мою библиотеку', lambda: view_library(user))
        },
        'admin': {
            '1': ('Добавить новую игру', add_game),
            '2': ('Удалить игру', lambda: delete_game(int(input("Введите ID игры: ")))),
            '3': ('Просмотреть все игры', lambda: view_games()),
            '4': ('Фильтровать игры', lambda: view_games(filter_by=input("Фильтровать по (ключ:значение): "))),
            '5': ('Сортировать игры', lambda: view_games(sort_by=input("Сортировать по (ключ): ")))
        }
    }
    
    while True:
        clear_screen()
        print(f"\nДобро пожаловать, {user}! Вы вошли как {role}.")
        print("\nМеню:")
        for key, value in options[role].items():
            print(f"{key}: {value[0]}")
        choice = input("\nВыберите пункт меню или введите 'q' для выхода: ")
        
        if choice == 'q':
            break
        
        try:
            action = options[role][choice][1]
            action()
            input("\nНажмите Enter для продолжения...")
        except KeyError:
            print("Неправильный выбор. Попробуйте еще раз.")
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    clear_screen()
    print("Добро пожаловать Steam!")
    print("1. Войти\n2. Зарегистрироваться\n")
    choice = input("Ваш выбор: ")
    
    if choice == '1':
        user = login()
        if user:
            main_menu(user)
    elif choice == '2':
        register()