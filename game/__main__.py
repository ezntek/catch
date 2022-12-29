import rlapi.rlapi as rl
from colors.colors import Colors
from types import NoneType
from sprites.bowl import Bowl
from sprites.sprite import SpriteGroup
import random
from variabledisplay.variable_display import VariableDisplay
import sprites.fruit as fruits


class Game():
    def event_loop(self) -> None:
        self._window_init()
        while not rl.window_should_close():
            self.update()
            with rl.drawing():
                self.render()

    def __init__(self) -> None:
        # set up critical variables
        self.global_timer = 0
        self.window_width = 800
        self.window_height = 600

        # sprites
        self.sprites = SpriteGroup(
            {
                0: fruits.Apple(random.randint(0, 750)),
                1: fruits.Orange(random.randint(0, 750)),
                2: fruits.Grape(random.randint(0, 750))
            }[random.randint(0, 30) % 3] # select an initial sprite to spawn
            
        )
        self.sprites.sprites[0].content.init_texture()
        self.bowl = Bowl(20, 500)

        # misc
        self.score: int = 0
        self.score_count = VariableDisplay(20, 20, "Score", self.score, Colors.electric_orange, Colors.orange)

        # call the event loop
        self.event_loop()

    def render(self) -> None:
        # render core components
        rl.clear_background(Colors.raywhite)
        self.score_count.render()

        # render bowl
        self.bowl.render()

        # render sprites
        for sprite in self.sprites:
            sprite.content.render() if sprite.content is not None else None
    
    def spawn_fruit(self):
        if self.global_timer % random.randint(45, 90) == 0:
            rngval = random.randint(0, 240)
            index = 0
            if rngval in range(0, 40):
                index = self.sprites.register_sprite(fruits.Grape(random.randint(0, 750)))
            elif rngval in range(40, 120): 
                index = self.sprites.register_sprite(fruits.Orange(random.randint(0,750)))
            elif rngval in range(120, 240):
                index = self.sprites.register_sprite(fruits.Apple(random.randint(0, 750)))
            self.sprites.sprites[index].content.init_texture()

    def update(self) -> None:
        # core actions
        self.global_timer += 1
        self.score_count.setval(self.score)
        self.spawn_fruit()
        self.bowl.update()

        # loop over sprite slots
        for sprite in self.sprites:
            sprite.content.update() if sprite.content is not None else None
            sprite.set_content(None) if (sprite.content is not None) and (sprite.content.should_delete) else None 
            if sprite.content is not None:
                self.score += self.bowl.collision(sprite.content)         
        self.sprites.squeeze()

    def _window_init(self) -> None:
        # initialize OpenGL context
        rl.init_window(self.window_width, self.window_height, "catch")
        rl.set_target_fps(60)

    

if __name__ == "__main__":
    Game()