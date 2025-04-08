users=[
    {"name":"Monika","location":"Mała Wieś","posts":200},
    {"name":"Michał","location":"Kraków","posts":200},
    {"name":"Ksawier","location":"Warszawa","posts":200},
    {"name":"Damian","location":"Poznań","posts":200},

]

def get_user_info(users_data: list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości {user['location']}, opublikował {user['posts']} postów")


get_user_info(users)