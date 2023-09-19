class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("{self.name}is playing cricket")

class Batsman(Player):
    def play(self):
        print(f"The batsman is batting.")

class Bowler(Player):
    def play(self):
        print(f"The bowler is bowling.")


batsman = Batsman("Batsman Name")
bowler = Bowler("Bowler Name")

batsman.play()
bowler.play()
