

users=[


    {"name":"Monika","location":"Mała Wieś","posts":200},
    {"name":"Michał","location":"Kraków","posts":200},
    {"name":"Ksawier","location":"Warszawa","posts":200},
    {"name":"Damian","location":"Poznań","posts":200},






]

#twój znajomy Julia z opublikował tyle i tyle postów
for user in users:
    print(f"Twój znajomy {user['name']}, z miejscowości {user['location']}, opublikował {user['posts']}")




