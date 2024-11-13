from models.animal_exotico import AnimalExotico


class Boa(AnimalExotico):

    def __init__(self, name, weight, age, country_origin, tax):
        super().__init__(name, weight, age, country_origin, tax)
        self.comer_raton = 0

    def make_sound(self):
        return "¡Tsss!"
    
    def add_mouse(self):
        if self.comer_raton == 10:
            raise ValueError("Demasiados Ratones!!!")
        self.comer_raton += 1


    def feed_boa(self) -> str:
        if self.comer_raton == 10:
            return "La boa está llena!"
        self.comer_raton += 1
        return "Exito"
    
    
    
    def get_comer_raton(self):
        return self.comer_raton