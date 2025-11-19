import pickle



class Team:
    def __init__(self):
        self.team_id = ""
        self.team_name = ""
        self.roster = []

    def create_team(self):
        self.team_id = input("Enter team ID: ")
        self.team_name = input("Enter team name: ")

    def add_player(self):
        try:
            with open("player_pool.dat", "rb") as f:  ## adds player to saved file for further use
                players = []
                while True:
                    try:
                        player = pickle.load(f)
                        players.append(player)
                    except EOFError:
                        break
        except EOFError:
            return

        print("\n--- Available Players ---") ## prints all available players in the league
        for i, p in enumerate(players):
            print(f"{i + 1}. {p.player_name} ({p.position}, {p.players_NFL_team})")

        choose_player = input("Select player number to add: ") ## selects player by player_ID
        selected_player = players[int(choose_player) - 1]

        # Add to roster
        self.roster.append(selected_player)
        print(f"{selected_player.player_name} added to {self.team_name}!")

    def display_team(self):
        print(self.team_id)
        print(self.team_name)
        for x in self.roster:
            print("Roster: ", x.player_id, x.player_name, x.position)


class Player:
    player_pool = []

    def __init__(self):
        self.player_id = ""
        self.player_name = ""
        self.player_height = ""
        self.player_weight = ""
        self.players_NFL_team = ""
        self.position = ""

    def create_player(self):
        self.player_id = input("Enter player ID: ")
        self.player_name = input("Enter player name: ")
        self.player_height = input("Enter player height: ")
        self.player_weight = input("Enter player weight: ")
        self.players_NFL_team = input("Enter player's NFL team: ")
        self.position = input("Enter player's position: ")

    @classmethod ## lets me add to the pool as a whole, not as a singular object
    def add_to_pool(cls, player):
        cls.player_pool.append(player)

    @classmethod
    def display_pool(cls):
        for x in cls.player_pool:
            print(x.player_id, x.player_name, x.position)


import pickle

def player_menu():
    new_player_pool=[]

    while True:
        print("--- Player Menu ---")
        print("1. Create player ")
        print("2. Display pool ")
        print("3. Save the player pool ")
        print("4. Display saved pool ")
        print("5. Return to main menu ")
        option = input("Select a function: ")

        if option == "1":
            new_player = Player()
            new_player.create_player()
            Player.add_to_pool(new_player)
            print("Player added to pool! ")

        elif option == "2":
            new_player = Player()
            Player.display_pool()

        elif option == "3":
            with open("player_pool.dat", "ab") as f1:
                for p in Player.player_pool:
                    pickle.dump(p, f1)
            print("Player pool saved!")

        elif option == "4":
            try:
                with open("player_pool.dat", "rb") as f2:
                    print("\n--- Saved Players ---")
                    while True:
                        try:
                            data = pickle.load(f2)
                            print(data.player_id, data.player_name, data.position, data.players_NFL_team)
                        except EOFError:
                            break
            except FileNotFoundError:
                print("No saved players yet.")

        elif option == "5":
            break

        elif option == "5":
            break


def team_menu():
    new_team = Team()

    while True:
        print("--- Team Menu --- ")
        print("1. Create a team ")
        print("2. Add player to the team ")
        print("3. Save the team changes ")
        print("4. Display league teams ")
        print("5. Return to main menu ")
        option = input("Select a function: ")

        if option == "1":
            new_team = Team()
            new_team.create_team()
            print("New team created!")

        elif option == "2":
            new_team.add_player()

        elif option == "3":
            f1 = open("league.dat", "ab")
            pickle.dump(new_team, f1)
            f1.close()

        elif option == "4":
            f2 = open("league.dat", "rb")
            while True:
                try:
                    data = pickle.load(f2)
                    data.display_team()
                except EOFError:
                    break

        elif option == "5":
            break


## Main Menu ##

while True:
    print("--- Main Menu ---")
    print("1. Player Menu ")
    print("2. Team Menu ")
    print("3. Quit ")
    option = input("Select a function: ")

    if option == "1":
        player_menu()

    elif option == "2":
        team_menu()

    elif option == "3":
        break