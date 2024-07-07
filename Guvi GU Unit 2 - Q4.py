class Player:
    def __init__(self, name, goals=0):
        self.name = name
        self._goals = self._validate_goals(goals)

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        self._goals = self._validate_goals(value)

    def _validate_goals(self, value):
        try:
            goal = int(value)
            if goal < 0:
                return 0
            return goal
        except ValueError:
            return 0

def clean_input(value):
    return str(value.strip())

name, goal = map(clean_input, input().strip().split(","))
next_goal = input()

player = Player(name, goal)
print(name)
print(player.goals)
player.goals = next_goal
print(player.goals)
