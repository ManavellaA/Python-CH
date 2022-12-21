class Cliente:

    def __init__(self, nombre, apellido, edad, direccion, ciudad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.direccion=direccion
        self.ciudad=ciudad

    def __str__(self):
        return self.nombre + " " + self.apellido 

    def dir_Fact(self):
        return "Direccion de Facturacion:  " + self.direccion + ", " + self.ciudad

# Cliente1=Cliente("Andres", "Manavella", 32, "Falucho 550", "Capitan Bermudez")    

# print(Cliente1)
# print(Cliente1.dir_Fact())