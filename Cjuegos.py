class Cjuegos:
    def __init__(self,ID, Name, Platform, Genre, Publisher):
        self.ID=ID
        self.Name=Name
        self.Platform=Platform
        self.Genre=Genre
        self.Publisher=Publisher
        #convierte en string 
    def __str__(self):
        return "%s ID: %d Name: %s P: %s G: %s Desarrollador: %s" (self.ID, self.Name, self.Platform, self.Genre, self.Publisher)
