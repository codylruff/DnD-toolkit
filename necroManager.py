import sys, os
import curses

class minion(object):
    
    def __init__(self, hit_points, damage, type):
        self.hit_points = hit_points
        self.damage = damage
        self.type = type

    def attack(self, creature):
        print(“{}, attacks {}”.format(self.type, creature.name)
        if(hits):
            creature.take_hit(self.damage)
        
