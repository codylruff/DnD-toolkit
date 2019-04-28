import sys, is
import curses

class spell(object):
    
    def __init__(self, name, effect, class_list):
        self.name = name
        self.effect = effect
        self.class_list = class_list

    def to_string():
        str = “Spell : {}\n”
        for cls in self.list:
            str = str + cls + “, “
        

