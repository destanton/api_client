import requests

print("Welcome to the Star Wars Database")


def Welcome():
        choice = input("What do you want to search for? people / planets / starships: ")
        if choice == "people" or choice == "starships" or choice == "planets":
            get_data(choice)
        # elif choice == "starships":
        #     ship_id =
        #     # input("Which Starship number do you want to search by? ")
        #     starships(ship_id)
        # elif choice == "planets":
        #     pass


def planets(planet_id):
    url = "http://swapi.co/api/planets/{}/".format(planet_id)
    while url:
        results = requests.get(url)
        json_result = results.json()
        print("""\nName: {}, Rotation Period: {}, Orbital Period: {}, Climate: {}, Gravity: {}, Terrain: {},
Surface Water: {}, Population: {}, Residents: {}, Films: {}""".format(json_result["name"],
            json_result["rotation_period"], json_result["orbital_period"], json_result["diameter"],
            json_result["climate"], json_result["gravity"], json_result["terrain"], json_result["surface_water"],
            json_result["population"], json_result["residents"], json_result["films"]))
        choice = input("\nDo you want to search again? Y/n ")
        if choice == "y":
            planet_id = input("\nWhich Planet ID do you want to search by? ")
        else:
            Welcome()


def starships(ship_id):
    url = "http://swapi.co/api/starships/{}/".format(ship_id)
    while url:
        results = requests.get(url)
        json_result = results.json()
        print('\nName: {}, Model: {}, Crew: {}, Passengers: {}, Starship Class: {}'.format(json_result["name"],
              json_result["model"], json_result["crew"], json_result["passengers"], json_result["starship_class"]))
        choice = input("\nDo you want to search again? Y/n ")
        if choice == "y":
            ship_id = input("\nWhich Ship ID do do you want to search by? ")
            starships(ship_id)
        else:
            Welcome()
    url = json_result["next"]


def get_character_info(character_id):
    url = "http://swapi.co/api/people/{}/".format(character_id)
    while url:
        results = requests.get(url)
        json_result = results.json()
        print('\nName: {}, Hair Color: {}, Gender: {}, Birth Year: {}, Films: {}'.format(json_result["name"],
              json_result["hair_color"], json_result["gender"], json_result["birth_year"], json_result["films"]))
        # for id in json_result["results"]:
        choice = input("\nDo you want to search again? Y/n ")
        if choice == "y":
            character_id = input("\nWhich Character number do you want to search By(1-87): ")
            get_character_info(character_id)
        else:
            Welcome()
        url = json_result["next"]


def get_data(endpoint, lookup="name"):
    url = "http://swapi.co/api/{}".format(endpoint)
    while url:
        results = requests.get(url)
        json_result = results.json()
        # print(json_result)
        for character in json_result["results"]:
            print(character[lookup])
            print(character["url"])
        choice = input("\nPress 'Enter' to continue listing or search by [C]hracter ID, [S]hip ID, or [P]lanet ID ").lower()
        if choice == "c":
            character_id = input("\nWhich Character number do you want to search By(1-87): ")
            get_character_info(character_id)
        elif choice == "s":
            ship_id = input("\nWhich Ship ID do do you want to search by? ")
            starships(ship_id)
        elif choice == "p":
            planet_id = input("\nWhich Planet ID do do you want to search by? ")
            planets(planet_id)
        url = json_result["next"]

while True:
    Welcome()
