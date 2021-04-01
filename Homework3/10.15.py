# BRYAN CHAVARRIA
# 1657040
# 10.15
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def set_team_name(self, name):
        self.team_name = name

    def set_team_wins(self, wins):
        self.team_wins = wins

    def set_team_losses(self, losses):
        self.team_losses = losses
if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.set_team_name(team_name)
    team.set_team_wins(team_wins)
    team.set_team_losses(team_losses)
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
