def create_dict_from_list(input_list):
    result_dict = {}
    for item in input_list:
        # Utilisation de la date comme clé et du nom du musicien comme valeur
        result_dict[item[1]] = result_dict.get(item[1], []) + [item[0]]
    return result_dict

# Liste de couples d
d = [
    ('Hendrix', '1942'),
    ('Allman', '1946'),
    ('King', '1925'),
    ('Clapton', '1945'),
    ('Johnson', '1911'),
    ('Berry', '1926'),
    ('Vaughan', '1954'),
    ('Cooder', '1947'),
    ('Page', '1944'),
    ('Richards', '1943'),
    ('Hammett', '1962'),
    ('Cobain', '1967'),
    ('Garcia', '1942'),
    ('Beck', '1944'),
    ('Santana', '1947'),
    ('Ramone', '1948'),
    ('White', '1975'),
    ('Frusciante', '1970'),
    ('Thompson', '1949'),
    ('Burton', '1939')
]

# Création du dictionnaire à partir de la liste
result_dict = create_dict_from_list(d)

# Affichage selon le format demandé
for key in sorted(result_dict.keys()):
    names = ' '.join(result_dict[key])
    print(f"{key} : {names}")
