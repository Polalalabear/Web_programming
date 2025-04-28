class BaseballPlayer:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        self.batting_average = 0.0
        self.homerun = 0
    
    def display_info(self):
        return (
            f"{self.name} 的打擊數據：\n"
            f"背號： {self.number}\n"
            f"位置： {self.position}\n"
            f"打擊率：{self.batting_average:.3f}\n"
            f"全壘打數：{self.homerun}"
        )
    
    def increase_batting_record(self, hits, at_bats):
        if(at_bats>0):
            self.batting_average = hits / at_bats
        else:
            self.batting_average = 0.0
        return self
    
    def hit_home_run(self):
        self.homerun += 1
        return self
    
    def __str__(self):
        return (self.display_info() + "\n" + "-"*20)
    
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_team_info(self):
        print(f"\n球隊：{self.name} 全體球員資訊：")
        for player in self.players:
            print(player)

    def average_team_batting_average(self):
        if not self.players:
            return 0.0
        total = sum(p.batting_average for p in self.players)
        return total / len(self.players)


player1 = BaseballPlayer("A", 0, "投手")
player2 = BaseballPlayer("B", 1, "捕手")
player3 = BaseballPlayer("C", 2, "投手")

player3.increase_batting_record(2, 3)
print(player3.display_info() + "\n" + "-"*20)

player3.increase_batting_record(1, 4)
print(player3.display_info() + "\n" + "-"*20)

player3.hit_home_run()
print(player3.display_info() + "\n" + "-"*20)

team1 = Team("FCU")
team1.add_player(player1)
team1.add_player(player2)
team1.add_player(player3)

team1.show_team_info()