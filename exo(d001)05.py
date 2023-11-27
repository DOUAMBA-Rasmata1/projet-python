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

def get_info_from_expression(expression):
    # Supprimer les espaces blancs en trop et convertir en minuscules
    clean_expression = expression.strip().lower()

    # Vérifier le nombre de virgules consécutives
    if not clean_expression:
        return None

    # Vérifier le type de l'expression
    if clean_expression in states:
        state = clean_expression
        capital = capital_cities[states[state]]
        return f"{capital} is the capital of {state}"
    elif clean_expression in capital_cities.values():
        capital = clean_expression
        state = get_state_by_capital(capital)
        if state != "Unknown state":
            return f"{capital} is the capital of {state}"
        else:
            return f"{capital} is neither a capital city nor a state"
    else:
        return f"{expression} is neither a capital city nor a state"

def get_state_by_capital(capital):
    for state, state_code in states.items():
        if state_code in capital_cities and capital_cities[state_code] == capital:
            return state
    return "Unknown state"

if __name__ == "__main__":
    import sys

    # Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        sys.exit()

    expressions = sys.argv[1].split(',')

    # Affichage des résultats
    for expression in expressions:
        result = get_info_from_expression(expression)
        if result is not None:
            print(result)
