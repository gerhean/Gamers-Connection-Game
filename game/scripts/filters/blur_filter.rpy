init python:
    def get_size(d):
        w, h = renpy.render(renpy.easy.displayable(d), 0, 0, 0, 0).get_size()
        return int(round(w)), int(round(h))
    def show_blur(img, degree = 5):
        w, h = get_size(img)
        factor = im.Scale(renpy.easy_displayable(img), w / degree, h / degree)
        factor = Transform(factor, size = (w, h))
        renpy.show(img, what=factor)

# Usage
# label start:
#     show bg1
#     pause
#     $ show_blur("bg1")
#     pause
#     return