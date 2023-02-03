class Things:
    pass


class Inanimate:
    pass


class Animate:
    pass


class SideWalks(Inanimate):
    pass


class Animals(Animate):
    def breathe(self):
        print("Breathing")

    def move(self):
        print("Moving")

    def eat_food(self):
        print("Eating")


class Mammals(Animals):
    def feed_young_with_milk(self):
        print("Feeding young")


class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots

    def eat_leaves_from_trees(self):
        print("Eating leaves")

    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

    def left_Foot_Forward(self):
        print("left foot forward")

    def left_Foot_Back(self):
        print("left foot back")

    def right_Foot_Forward(self):
        print("right foot forward")

    def right_Foot_Back(self):
        print("right foot back")

    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Forward()

    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()


reginald = Giraffes(100)
print(reginald.giraffe_spots)
reginald.move()
reginald.eat_leaves_from_trees()
reginald.find_food()
reginald.dance()
