import json
import random

class Loses:
    def __init__(self, warriors: int = 0, hunters: int = 0, wizards: int = 0):
        self.nb_warriors = warriors
        self.nb_hunters = hunters
        self.nb_wizards = wizards

class Game:
    history_file = 'game_data.json'

    def __init__(self):
        self.__game_status = 'not_started'

    # --- Gestion du stockage ---
    def save_game(self, player_name, context, loot, team):
        data = {
            'player_name': player_name,
            'context': context,
            'loot': loot,
            'team': team
        }
        with open(self.history_file, 'w') as f:
            json.dump(data, f, indent=4)
        print('Partie sauvegardée dans game_data.json')

    def load_game(self):
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    # --- Actions de jeu ---
    def config(self):
        name = input("Entrez votre nom de joueur : ")
        self.save_game(name, 'mouvement', 40, {'warrior': 0, 'hunter': 0, 'wizard': 0})

    def start(self):
        data = self.load_game()
        name = data['player_name'] if data else "Joueur"
        self.save_game(name, 'mouvement', 40, {'warrior': 0, 'hunter': 0, 'wizard': 0})
        print("Partie réinitialisée !")

    def status(self):
        data = self.load_game()
        if not data:
            print("Aucune partie en cours. Lancez config() ou start().")
            return
        
        print(f"\n--- STATUT : {data['player_name']} ---")
        print(f"Butin : {data['loot']} | Contexte : {data['context']}")
        print(f"Équipe : {data['team']}")
        
        if data['context'] == "mouvement":
            print("Actions possibles : buy, move")
        else:
            print("Actions possibles : fight, flee")

    def buy(self, unit_type):
        data = self.load_game()
        prices = {'warrior': 10, 'hunter': 12, 'wizard': 15}
        
        if data['context'] != 'mouvement':
            print("Impossible d'acheter en plein combat !")
            return False

        if unit_type in prices and data['loot'] >= prices[unit_type]:
            data['loot'] -= prices[unit_type]
            data['team'][unit_type] += 1
            self.save_game(data['player_name'], data['context'], data['loot'], data['team'])
            print(f"Achat réussi : {unit_type}")
            return True
        print("Achat impossible (pas assez d'or ou unité inconnue).")
        return False

    def move(self):
        data = self.load_game()
        if data['context'] != 'mouvement': return
        
        print('Déplacement en cours...')
        r = random.random()
        if r < 0.2:
            print("Trouvé du butin !")
            data['loot'] += 10
        elif r < 0.5:
            print("COMBAT ! Une équipe ennemie surgit !")
            data['context'] = 'combat'
        
        self.save_game(data['player_name'], data['context'], data['loot'], data['team'])
        self.status()

    def fight(self):
        data = self.load_game()
        if data['context'] != 'combat': return
        
        # Logique simplifiée : 50% de chance de gagner
        if random.random() > 0.5:
            print("Victoire ! Le combat est terminé.")
            data['context'] = 'mouvement'
        else:
            print("Défaite... GAME OVER.")
            self.start() # Reset
            return
        
        self.save_game(data['player_name'], data['context'], data['loot'], data['team'])

    def flee(self):
        data = self.load_game()
        if data['context'] != 'combat': return
        
        print('Tentative de fuite...')
        data['context'] = 'mouvement'
        self.save_game(data['player_name'], data['context'], data['loot'], data['team'])
        self.status()
