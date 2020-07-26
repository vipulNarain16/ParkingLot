class type_of_Vechicle:
    def __init__(self,registrationnumber,color):
        self.registrationnumber  = registrationnumber
        self.color = color
class car(type_of_Vechicle):
    def __init__(self,registrationnumber,color):
        type_of_Vechicle.__init__(self,registrationnumber,color)

    def get_vechicle_type(self):
        return "Car"
