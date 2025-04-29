moja_lista_na_sok=[]
print(moja_lista_na_sok)

def add_user(users_data: list)-> None:

    new_name=input('Podaj imię nowego użytkownika: ')
    new_location=input('Podaj lokalizację użytkownika: ')
    new_posts=int(input('Podaj liczbę postów: '))
    users_data.append( {"name":new_name,"location":new_location,"posts":new_posts})
add_user(moja_lista_na_sok)
print(moja_lista_na_sok)
