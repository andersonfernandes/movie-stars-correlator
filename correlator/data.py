dict_origin = {"Hanks, Tom": ["Madonna", "Marshall, Penny", "O'Donnell, Rosie", "Bacon, Kevin", "Paxton, Bill", "Sinise, Gary"],
   "Madonna": ["Hanks, Tom", "Marshall, Penny", "O'Donnell, Rosie"],
   "Marshall, Penny": ["Hanks, Tom", "Madonna", "O'Donnell, Rosie"],
   "O'Donnell, Rosie": ["Hanks, Tom", "Madonna", "Marshall, Penny"],
   "Bacon, Kevin": ["Hanks, Tom", "Belushi, John", "Sutherland, Donald", "Paxton, Bill", "Sinise, Gary"],
   "Belushi, John": ["Bacon, Kevin", "Sutherland, Donald"],
   "Sutherland, Donald": ["Bacon, Kevin", "Belushi, John"],
   "Paxton, Bill": ["Hanks, Tom", "Bacon, Kevin", "Sinise, Gary"],
   "Sinise, Gary": ["Hanks, Tom", "Bacon, Kevin", "Paxton, Bill"]}

dict_movies = {"A League": ["Madonna", "Penny Marshall", "Rosie O'Donnell", "Tom Hanks"],
                "Apollo 13": ["Tom Hanks", "Gary Sinise", "Bill Paxton", "Kevin Bacon"],
                "Animal House": ["Kevin Bacon", "Donald Sutherland", "John Belushi"]}

dict_result = {}
dict_complet = {}
list_values = []

#Trata o dicionario original 
def dict_handling():
    #invertendo o nome pelo sobrenome nos valores
    for list_value in dict_origin.values():
        list_aux = []
        for value in list_value:
            if value != 'Madonna':
                surname, name = value.split(', ')
                value = name + ' ' + surname
            list_aux.append(value)
        list_values.append(list_aux)
    #invertendo o nome pelo sobrenome nas chaves e gerando o novo dicionario
    for key in dict_origin.keys():
        if key != 'Madonna':
            surname, name = key.split(', ')
            key = name + ' ' + surname
        dict_result[key] = list_values.pop(0)

    #print(dict_result)
    #return dict_result

#Insere os filmes como relação entre os atores 
def dict_add_relationship():
    dict_handling()

    for itens in dict_result.items():
        list_aux = []
        for name in itens[1]:
            dict_aux = {}
            for movies in dict_movies.items():
                if name in movies[1] and itens[0] in movies[1]:
                    dict_aux["name"] = name
                    dict_aux["movie"] = movies[0]
                    #name = [movies[0],name] 
                    list_aux.append(dict_aux)
        dict_complet[itens[0]] = list_aux

    return dict_complet

#Grava um arquivo de texto com dados do grafo
def write_file():
    path = 'stars.txt'
    arq = open(path,'w+')

    for i in dict_result.items():
        for name in i[1]:
            arq.write(i[0]+','+name)
            arq.write('\n')

    arq.close()
