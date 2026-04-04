import heifer_generator

class Cow:
#Initializes a cow object with the given name and sets image to be None.
    def __init__(self, name):
        self.name = name
        self.image = None

    #Returns the name of the cow. Note: the name property should NOT have a setter.
    def get_name(self):
        return self.name

    #Returns the image used to display the cow (this should be called after the message has been displayed).
    def get_image(self):
        return self.image

    #Sets the image used to display the cow.
    def set_image(self, image):
        self.image = image

    def __eq__(self, other):
        return self.get_name() == other.get_name()