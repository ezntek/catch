import rlapi.rlapi as rl
from colors.colors import Colors

class Game():
    def __init__(self) -> None:
        # call the event loop
        self.event_loop()

    def render(self) -> None:
        rl.clear_background(Colors.raywhite)

    def update(self) -> None:
        pass

    def _window_init(self) -> None:
        # initialize OpenGL context
        rl.init_window(800, 600, "catch")
        rl.set_target_fps(60)

    def event_loop(self) -> None:
        self._window_init()
        while not rl.window_should_close():
            self.update()
            with rl.drawing():
                self.render()

if __name__ == "__main__":
    Game()