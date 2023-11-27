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

# Fonction pour obtenir l'État par la capitale
def get_state_by_capital(capital):
    for state, state_code in states.items():
        if state_code in capital_cities and capital_cities[state_code] == capital:
            return state
    return "Unknown state"

# Exemple d'utilisation avec des arguments en ligne de commande
if __name__ == "__main__":
    import sys

    # Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage: python3 state.py <capital>")
    else:
        capital_to_check = sys.argv[1]
        state_result = get_state_by_capital(capital_to_check)
        print(state_result)
sssssss