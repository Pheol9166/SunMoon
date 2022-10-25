from gamepack import *
import time

class SunMoon(Gamepack):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def intro(self) -> None:
        self.startscene("intro")
        self.choice(self.route_a, self.leave_end, third= self.route_c)
    
    def route_a(self) -> None:
        self.startscene("route_A")
        self.choice(self.tree_end, self.guilty_end)
    
    def leave_end(self) -> None:
        self.startscene("leave_ending")
        quit()
    
    def route_c(self) -> None:
        self.startscene("route_C")
        self.choice(self.hug_end, self.route_c2)
    
    def tree_end(self) -> None:
        self.startscene("tree_ending")
        quit()
    
    def guilty_end(self) -> None:
        self.startscene("guilty_ending")
        
        for i in range(1, 101):
            print("왜 도망갔어?", end = ' ', flush= True)
            if i % 10 == 0:
                print()
                time.sleep(0.4)

        ending = "><><><><><><>>tHe EnD<><><<><><>><<>"
    
        for i in ending:
            print(i, end='', flush=True)
            time.sleep(0.1)
        quit()
    
    def hug_end(self) -> None:
        self.startscene("hug_ending")
        quit()
    
    def route_c2(self) -> None:
        self.startscene("route_C2")
        self.choice(self.well_end, self.dream_end)

    def well_end(self) -> None:
        self.startscene("well_ending")
        quit()
    
    def dream_end(self) -> None:
        self.startscene("dream_ending")
        quit()
