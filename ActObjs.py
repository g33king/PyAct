class ActSprite:
  def __init__(self, win, x, y, width, height, tex, func):
    self.win = win
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.tex = tex
    self.func = func
    
class ActBlock:
  def __init__(self, win, x, y, width, height, tex):
    self.win = win
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.tex = tex
  def setFunc(self, function):
    self.func = function

class ActWindow:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
