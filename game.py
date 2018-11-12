import game_text as gt
from sys import exit

class Task:
    def __init__(self, lib):
        # saves library as self.lib
        self.lib = lib
        # saves the description
        self.description = self.lib['description']
        # saves the goal prompt
        self.goal = self.lib['goal']
        # prints description and goal to the user
        print(self.description)
        print(self.goal)
        # saves the next library
        self.next = self.lib['next_lib']
        # gets the choices and the number of choices
        self.choices, self.ran = self.get_choices()
        # gets the list of results
        self.right, self.alive, self.dead, self.results = self.get_results()

        self.run_task()

    def run_task(self):
        self.print_choices()
        self.answer = int(input("> "))
        self.result = self.find_choice()
        print(self.result)
        if self.result == self.right:
            print("You did it!")
            next_task = Task(self.next)
        elif self.result in self.alive:
            print("At least you're still alive.")
            self.run_task()
        elif self.result in self.dead:
            self.dead_menu()
        else:
            print("Incorrect Input.")
            self.run_task()

    def dead_menu(self):
        print("You're dead would you like to try again?")
        answ = input("Yes or no? ")
        if answ.lower() == 'yes':
            find_light = Task(gt.libtsk1)
        elif answ.lower() == 'no':
            print("Game Over.")
            exit(0)
        else:
            print("Game Over.")
            exit(0)

    def find_choice(self):
            num_dict = {}
            for x in self.ran:
                num_dict[x+1] = self.choices[x]
            if self.answer in num_dict:
                self.answer = num_dict[self.answer]
                return(self.lib['results'][self.answer])
            else:
                print("Incorrect Input!")
                self.run_task()

    def get_results(self):
        results = []
        for choice in self.choices:
            results.append(self.lib['results'][choice])
        alive = []
        dead = []
        for x in self.lib["alive"]:
            alive.append(results[x])
        for y in self.lib['dead']:
            dead.append(results[y])
        right = results[self.lib['right']]
        return right, alive, dead, results

    def get_choices(self):
        length = len(self.lib['choices'])
        ran = range(0,(length))
        choices = []
        for x in ran:
            choices.append(self.lib['choices'][x])
        return choices, ran

    def print_choices(self):
        for x in self.ran:
            print(f"Choice {x+1} is {self.lib['choices'][x]}")

find_light = Task(gt.libtsk1)
