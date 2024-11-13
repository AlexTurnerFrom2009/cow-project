from cow import Cow

class Dragon(Cow):
  def __init__(self, name, image):
    super().__init__(name, image)
    
  def can_breathe_fire(self):
    return True
  
