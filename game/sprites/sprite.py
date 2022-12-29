from re import S
import rlapi.rlapi as rl
from colors.colors import Colors

class Sprite():
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        # critical variables
        self.hitbox = rl.Rectangle(x, y, width, height)
        self.hitbox_color = Colors.nothing
        self.should_delete = False

        # textures
        self.texture: rl.Texture
        self.frame: rl.Vector2 
        self.source_rec: rl.Rectangle
        
    # function definitions

    def init_texture(self): return
    def kb_input(self) -> None: return
    def collision(self, sprite) -> int : return 0
    def update(self) -> None: return
    def render(self) -> None: return
    def __repr__(self) -> str: return "Sprite Base Class"

class SpriteSlot():
    def __init__(self, content: Sprite, index=0):
        self.content = content
        self.index = index
    
    # setters
    def set_index(self, index: int): self.index = index
    def set_content(self, sprite): self.content = sprite

    # repr
    def __repr__(self) -> str:
        return f"{self.content.__repr__()} at index {self.index}"

class SpriteGroup():
    def __init__(self, *sprites):
        self.sprites = [SpriteSlot(s, index=count) for count, s in enumerate(sprites)]
        self.current_index = 0

    def squeeze(self):
        try:
            if self.sprites[-1].content == None:
                self.sprites.pop(-1)
                try:
                    self.squeeze() # use recursion
                except IndexError:
                    return
        except IndexError:
            return
 
    def register_sprite(self, new_sprite: Sprite) -> int | bool:
        try:
            for count, sprite_slot in enumerate(self.sprites):
                if sprite_slot.content == None:
                    sprite_slot.set_content(new_sprite)
                    return count
            self.sprites.append(SpriteSlot(new_sprite, index=len(self.sprites)))
            return len(self.sprites) - 1
        except:
            return False

    def delete_sprite(self, at_index: int) -> None | bool:
        try:
            self.sprites[at_index].set_content(None)
        except IndexError:
            return False

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index >= len(self.sprites):
            self.current_index = 0
            raise StopIteration
        retval = self.sprites[self.current_index]
        self.current_index += 1
        return retval
    
    def __repr__(self):
        retval = ""
        for s in self.sprites:
            retval += f"{s.__repr__()}, " 
        return retval
    
    def __getitem__(self, index):
        return self.sprites[index]