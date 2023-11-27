def read_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = file.read().split(',')
            return numbers
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")
        return None

def display_numbers(numbers):
    if numbers:
        for number in numbers:
            print(number.strip())

if __name__ == "__main__":
    file_path = "ex01/numbers.txt"  # Spécifiez le chemin complet si nécessaire
    numbers = read_numbers(file_path)
    display_numbers(numbers)
