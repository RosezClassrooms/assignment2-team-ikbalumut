from abc import ABC, abstractmethod  # For Builder classes

# THE PRODUCT
class Robot:
  def __init__(self):
    '''
      Instead of having bipedal, quadripedal, flying, or on wheel seperately here,
      we re-defined them as 'Product Type'.
      Also, instead of user-defined parameters (or empty lists) in our __init__, 
      we re-defined our traversals and detection systems as objects (can be seen at
      concrete classes for components part below). 
    '''

    self.product_type = None
    self.traversal = Traversal()
    self.detection_systems = DetectionSystems()

  def set_type(self, p_type):
    ''' Product type setter to determine if the robot is 
    bipedal, quadripedal, flying or on wheels. '''
    
    self.product_type = p_type

  def __str__(self):
    string = "\n" + self.product_type.upper()

    string += "\nTraversal modules:"
    string += "\n-{0} arm(s)\n-{1} leg(s)\n-{2} wheel(s)\n-{3} wing(s)"\
      .format(self.traversal.arm, self.traversal.leg, self.traversal.wheel, self.traversal.wing)

    string += "\nDetection systems:"
    string += "\n-{0} camera(s)\n-{1} infrared(s)"\
      .format("There are" if self.detection_systems.camera else "There aren't any",
              "There are" if self.detection_systems.infrared else "There aren't any")
    
    return string


# CONCRETE CLASSES FOR COMPONENTS
'''
  Instead of creating individual classes for each component, we decided to merge related
  attributes in one class. In this way, the code will be more readable and organized even
  if there will millions of attributes in the future.
'''
class ProductType:
  p_type = None

class Traversal:
  leg = None
  arm = None
  wing = None
  wheel = None

class DetectionSystems:
  camera = None
  infrared = None


# ABSTRACT SUPERCLASS FOR BUILDERS
class RobotBuilder(ABC):
  '''
    Specify an abstract interface for creating parts of a Product
    object.
  '''

  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  def get_product(self):
    return self.product

  @abstractmethod
  def get_type(self):
    pass

  @abstractmethod
  def build_traversal(self):
    pass

  @abstractmethod
  def build_detection_system(self):
    pass


# CONCRETE BUILDER CLASSES
'''
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
'''

class AndroidBuilder(RobotBuilder):
  def get_type(self):
    ''' Product type getter to determine if the robot is
    bipedal, quadripedal, flying or on wheels. '''
    
    self.product.product_type = "Bipedal Robot"

  def build_traversal(self):
    # traversal = Traversal()
    self.product.traversal.arm = 2
    self.product.traversal.leg = 2
    return self.product.traversal

  def build_detection_system(self):
    # detection = DetectionSystems()
    self.product.detection_systems.camera = True
    return self.product.detection_systems

class AutonomousCarBuilder(RobotBuilder):
  def get_type(self):
    ''' Product type getter to determine if the robot is 
    bipedal, quadripedal, flying or on wheels. '''
    
    self.product.product_type = "Robot on Wheels"

  def build_traversal(self):
    # traversal = Traversal()
    self.product.traversal.arm = 2
    self.product.traversal.leg = 2
    self.product.traversal.wheel = 4
    return self.product.traversal

  def build_detection_system(self):
    # detection = DetectionSystems()
    self.product.detection_systems.camera = True
    self.product.detection_systems.infrared = True
    return self.product.detection_systems

# THE DIRECTOR
class Director:
  ''' Construct an object using the Builder interface. '''
  
  def construct(self, builder):
    robot = Robot()
    
    # getting the product type (bipedal, quadripedal, flying, or wheeled)
    construct_type = builder.get_type()
    robot.set_type(construct_type)
    
    # building traversals and detection systems
    builder.build_traversal()
    builder.build_detection_system()
    
    return builder.get_product()

def main():
  director = Director()

  android = AndroidBuilder()
  print(director.construct(android))

  autonomous = AutonomousCarBuilder()
  print(director.construct(autonomous))

if __name__ == "__main__":
  main()
