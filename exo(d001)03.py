def create_dict_from_list(input_list):
    result_dict = {}
    for item in input_list:
        result_dict[item[1]] = result_dict.get(item[1], []) + [item[0]]
    return result_dict

def get_capital_by_state(state):
    # Vérification de la validité de l'argument
    if state in states:
        # Récupération du code d'État
        state_code = states[state]
        
        # Vérification de la présence du code dans le dictionnaire des capitales
        if state_code in capital_cities:
            return capital_cities[state_code]
        else:
            return "Unknown capital"
    else:
        return "Unknown state"

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

# Dictionnaires des États et des capitales
states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

# Création du dictionnaire à partir de la liste
result_dict = create_dict_from_list(d)

# Test de la fonction get_capital_by_state avec un exemple
state_to_check = "Oregon"
capital_result = get_capital_by_state(state_to_check)
print(f"The capital of {state_to_check} is: {capital_result}")
