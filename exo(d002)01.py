class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Coffee()

# Tests
if __name__ == "__main__":
    # Création de deux instances de la classe Intern
    intern1 = Intern()  # Sans nom
    intern2 = Intern(name="Mark")

    # Affichage du nom de chaque instance
    print("Intern 1:", intern1)
    print("Intern 2:", intern2)

    # Demande à Mark de faire un café
    try:
        coffee = intern2.make_coffee()
        print("Mark made coffee:", coffee)
    except Exception as e:
        print(f"Exception while making coffee: {e}")

    # Demande à l'autre stagiaire de travailler (gérant l'exception)
    try:
        intern1.work()
    except Exception as e:
        print(f"Exception while working: {e}")