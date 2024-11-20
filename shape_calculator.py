class Rectangle():

  def __init__(self,w,h):
    self.height=h
    self.width=w
    return

  def __str__(self):
    return ("Rectangle(width="+str(self.width)+", height="+str(self.height)+")")
    
  
  def set_width(self,w):
    self.width=w
    return w

  def set_height(self,h):
    self.height=h
    return h

  def get_area(self):
    area=self.width*self.height
    return (area)

  def get_perimeter(self):
    perimeter=2*self.width+2*self.height
    return (perimeter)

  def get_diagonal(self):
    diagonal=((self.width ** 2 + self.height ** 2) ** .5)
    return (diagonal)
  
  def get_picture(self):
    if (self.height)>50 or (self.width)>50:
      return("Too big for picture.")
    string = (("*" * self.width) + "\n") * self.height
    return(string)

  def get_amount_inside(self,shape):
    self.shape = shape
    if self.shape == shape:
      num_times = self.get_area()/(shape.get_area())
      return int(num_times)
    else:
      num_times = self.get_area()/(self.width * self.height)

    
    return int(num_times)

  

class Square(Rectangle):
  
  def __init__(self,s):
    self.height=s
    self.width=s
    return

  def __str__(self):
    return ("Square(side="+str(self.width)+")")

  def set_side(self,s):
    self.height=s
    self.width=s
    
    return s

  


