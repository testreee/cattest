#beta
import time
class Cat:
    print("Meow")
    def __init__(self, name, play, sleep, food, life, speach):
        self.food = food
        self.name = name
        self.play = play
        self.sleep = sleep
        self.life = life
        self.speach = speach
        print("meow")
    def Health(self):
        return f"{self.food} {self.play} {self.sleep} {self}"
    def ResultOfLife(self):
        if self.food <=0 or self.sleep < 5:
            self.life() -= 1
            time.sleep(1)
            print("cat is not safe")

cat_wake = Cat()