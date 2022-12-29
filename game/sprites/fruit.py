import random
import rlapi.rlapi as rl
from colors.colors import Colors
from sprites.sprite import Sprite

class Apple(Sprite):
    def __init__(self, x: float) -> None:
        # call superclass constructor
        super().__init__(x, 0, 50, 50)

        # define critical variables
        self.hitbox_color = Colors.red
        self.animation_counter = 0
        self.should_delete = False
        self.fall_speed = random.randint(3, 5)

    def init_texture(self): # init the textures
        self.texture = rl.load_texture("res/apple.png")
        self.frame = rl.Vector2(self.texture.width, self.texture.height)
        self.source_rec = rl.Rectangle(0, 0, self.frame.x, self.frame.y)

    def render(self):
        self.texture.draw_pro(self.source_rec, self.hitbox, rl.Vector2(0, 0), 0.0, Colors.white)

    def update(self):
        if self.animation_counter <= 300:
            self.hitbox.y += self.fall_speed
        if self.hitbox.y >= 575:
            self.should_delete = False

    def __repr__(self) -> str:
        return "Apple Sprite"

class Orange(Sprite):
    def __init__(self, x: float) -> None:
        super().__init__(x, 0, 50, 50)

        # define critical variables
        self.hitbox_color = Colors.orange
        self.animation_counter = 0
        self.should_delete = False
        self.fall_speed = random.randint(5, 8)

        # textures
        # NOTHING YET
    
    def render(self):
        rl.draw_rectangle_rec(self.hitbox, self.hitbox_color)

    def update(self):
        if self.animation_counter <= 300:
            self.hitbox.y += self.fall_speed
        if self.hitbox.y >= 575:
            self.should_delete = False

    def __repr__(self) -> str:
        return "Orange Sprite"

class Grape(Sprite):
    def __init__(self, x: float) -> None:
        super().__init__(x, 0, 50, 50)

        # define critical variables
        self.hitbox_color = Colors.lavendar
        self.animation_counter = 0
        self.should_delete = False
        self.fall_speed = random.randint(6, 10)

        # textures
        # NOTHING YET
    
    def render(self):
        rl.draw_rectangle_rec(self.hitbox, self.hitbox_color)

    def update(self):
        if self.animation_counter <= 300:
            self.hitbox.y += self.fall_speed
        if self.hitbox.y >= 575:
            self.should_delete = False

    def __repr__(self) -> str:
        return "Grape Sprite"