import random


class RockPaperScissors:

    def __init__(self):
        self.rating = 0
        self.name = input('Enter your name:')
        self.default_options = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        self.win_list = {}

    def play(self):
        print(f'Hello, {self.name}')
        with open('rating.txt') as ratings:
            for line in ratings:
                if self.name in line:
                    self.rating = int(line.split()[1])
        self.game_rules()
        return self.action()

    def game_rules(self):
        elements = input().strip()
        if elements:
            elements = elements.split(',')
            i = 0
            while i < len(elements):
                el = elements[i]
                new_list = elements[i + 1:] + elements[:i + 1]
                self.win_list[el] = {x for x in new_list[int((len(elements)/2)):]}
                i += 1
        else:
            self.win_list = self.default_options
        print(self.win_list)
        print("Okay, let's start")

    def action(self):
        user_act = input()
        if user_act in self.win_list:
            return self.judge(user_act)
        elif user_act == '!rating':
            print(f'Your rating: {self.rating}')
        elif user_act == '!exit':
            print('Bye!')
            exit()
        else:
            print('Invalid input')
        return self.action()

    def judge(self, action):
        cpu_turn = random.choice([*self.win_list])
        if cpu_turn == action:
            print(f'There is a draw ({action})')
            self.rating += 50
        elif cpu_turn in self.win_list[action]:
            print(f'Well done. The computer chose {cpu_turn} and failed')
            self.rating += 100
        else:
            print(f'Sorry, but the computer chose {cpu_turn}')
        return self.action()

if __name__ == '__main__':
  c = RockPaperScissors()
  c.play()
