from pyglet import gl

from ui import elements


class Widget(elements.Element):
    def __init__(self, x, y, w, h, parent=None):
        super().__init__(x, y, w, h, parent)
        self.pressed = False
        self.hover = False
        self.is_visible = True
        self.border_radius = 4
        self.background_color = (0, 0, 0, 1)
        self._z_index = 0

    @property
    def z_index(self):
        if self.parent is not None:
            return self._z_index + self.parent.z_index + 1
        return self._z_index
    
    @z_index.setter
    def z_index(self, value):
        if self.parent is not None:
            self._z_index = value - self.parent._z_index - 1
        else:
            self._z_index = value
    
    def is_hover(self, x, y):
        left, bottom = self.global_position
        right = left + self.width
        top = bottom + self.height
        return (left <= x <= right and bottom <= y <= top)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        self.hover = self.is_hover(x, y)
        self.pressed = self.hover

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def toggle_is_visible(self):
        self.is_visible = not self.is_visible
    
    def update_viewport(self):
        x, y = self.global_position
        gl.glViewport(x, y, self.width, self.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, self.width, 0, self.height, 0, 1)
    
    def draw(self):
        pass

    def update(self, dt):
        pass
