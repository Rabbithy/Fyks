from .frame import Frame


class Layout(Frame):
    def __init__(self, x, y, w, h, orientation='horizontal', parent=None):
        super().__init__(x, y, w, h, parent)
        self.orientation = orientation
    
    def resize(self, width, height):
        super().resize(width, height)
        cursor = 0
        for i, element in enumerate(self.elements):
            if self.orientation == 'horizontal':
                h = (self.height - cursor) / (len(self.elements) - i)
                element.resize(self.width, h)
                element.top = cursor + element.margin_top
                cursor = element.top + element.height
            elif self.orientation == 'vertical':
                w = (self.width - cursor) / (len(self.elements) - i)
                element.resize(w, self.height)
                element.left = cursor + element.margin_left
                cursor = element.left + element.width
