from sys import exit 
from random import randint
# function dedent: write our room descriptions using triple-quote strings
from textwrap import dedent 

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished') 

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this",
        "Your Mom would be proud...if she were smarter",
        "Such a luser",
        "I have a small puppy that's better at this",
        "You're worse than your Dad's jokes"
    ]   

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                    Quick on the draw you yank out your blaster and fire
                    it at the Gothon. His clown costume is flowing and
                    moving around his body, which throws off your aim.
                    Your laser hits his costume but misses him entirely.
                    This completely ruins his brand new costume his mother
                    bought him, which makes him fly into an insane rage
                    and blast you repeatedly in the face until you are
                    dead. Then he eats you."""
                    ))  
        return 'death'               
            
