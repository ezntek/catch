import rlapi.rlapi as rl
from sprites.sprite import Sprite
from colors.colors import Colors
from sprites.fruit import *

class Bowl(Sprite):
    def __init__(self, x: float, y: float) -> None:
        # set up
        super().__init__(x, y, 150, 60)
        self.hitbox_color = Colors.shit
        self.should_delete = False
    
    def kb_input(self) -> None:
        if rl.is_key_down(rl.KEY_LEFT) and self.hitbox.x - 10 >= 0:
            self.hitbox.x -= 10
        if rl.is_key_down(rl.KEY_RIGHT) and self.hitbox.x + 650 >= 0:
            self.hitbox.x += 10
    
    def update(self):
        self.kb_input()
    
    def render(self):
        rl.draw_rectangle_rec(self.hitbox, self.hitbox_color)

    def collision(self, sprite) -> int:
        if rl.check_collision_recs(self.hitbox, sprite.hitbox):
            sprite.should_delete = True # prepare for deletion
            try:
                # check the number of points to add via a hashmap
                return {
                    Apple: 1,
                    Orange: 2,
                    Grape: 3
                }[type(sprite)]
            except KeyError:
                return 0
        return 0
    
    def __repr__(self) -> str:
        return "Bowl Sprite"