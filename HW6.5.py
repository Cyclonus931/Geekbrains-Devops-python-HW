# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Sport:
    name = str
    season = str
    teamplayers = int
    teamquantity = int

    def __init__(self, name: str, season: str, teamplayers: int, teamquantity: int):
        self.name = name
        self.season = season
        self.teamplayers = teamplayers
        self.teamquantity = teamquantity

    def get_total_players(self):
        print(f'There could be a {self.teamquantity * self.teamplayers} players at the same time in {self.name} game ')


sport = Sport("tennis", "Summer", 1, 2)
print(f'"{sport.season} olympics"')
sport.get_total_players()

sport = Sport("ice hockey", "Winter", 6, 2)
print(f'"{sport.season} olympics"')
sport.get_total_players()
