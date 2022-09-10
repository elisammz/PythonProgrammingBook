# Critter Caretaker
# A virtual pet to care for


class Critter(object):
    """A vritual pet"""

    # constructor
    def __init__(self, name, hunger=0, boredom=0):

        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    # a private method to pass hunger and boredom levels. It is only invoked within class methods
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):

        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "happy"
        elif 5 <= unhappines <= 10:
            m = "okay"
        elif 11 <= unhappines <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    # the eat method
    def eat(self, food=4):
        print("Brrupp. Thank U.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    # the play method
    def play(self, fun=4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


# main
# creates the critter first and then a new critter (object) is instantiated
def main():
    crit_name = input("What do you want to name your critter?:")
    crit = Critter(crit_name)

    # menu system
    choice = None
    while choice != "0":
        print(
            """Critter Caretaker
             0 - Quit 
             1 - Listen to your critter
             2 - Feed your critter
             3 - Play with your critter"""
        )

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Goodbye")

        # listen to your critter
        if choice == "1":
            crit.talk()

        # feed your critter
        if choice == "2":
            crit.eat()

        # play with your critter
        if choice == "3":
            crit.play()

        # some unknown choice
    else:
        print("\nSorry, but", choice, "is not a valid choice.")


main()
("\n\nPress the enter key to exit.")
