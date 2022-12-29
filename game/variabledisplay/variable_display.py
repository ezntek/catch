from typing import Union
import rlapi.rlapi as rl
from colors.colors import Colors

class VariableDisplay:
    def __init__(self, posx: int, posy: int, name: str, value: Union[int, str], bg_color: rl.Color, accent_color: rl.Color) -> None:
        # position vars
        self.posx = posx
        self.posy = posy

        # values and styling
        self.value: Union[int, str] = value
        self.name: str = name
        self.bg_color: rl.Color = bg_color
        self.name_bg_color = accent_color
        self.current_text = f"{self.name} {self.value}"
        self.text_size = rl.measure_text(self.current_text, 20)

    def setval(self, value: Union[int, str]) -> None:
        self.value = value
    
    
    def render(self) -> None:
        # sneak update code into render function
        self.current_text = f"{self.name} {self.value}"
        self.text_size = rl.measure_text(self.current_text, 20)

        # actual rendering
        rl.draw_rectangle(self.posx, self.posy, self.text_size+10, 20+10, self.bg_color)
        rl.draw_rectangle(self.posx+5, self.posy+5, rl.measure_text(self.name, 20), 20, self.name_bg_color)
        rl.draw_text(self.current_text, self.posx+5, self.posy+5, 20, Colors.raywhite)
