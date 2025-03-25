from clases.gato import Gato
from clases.perro import Perro
from clases.vaca import Vaca

#Polimorfismo: capacidad de los objetos de diferentes clases de responder al mismo metodo de forma distinta

def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace el sonido de: {animal.hacer_sonido()}")

perro =Perro ("Luma")
gato=Gato("Pelusa")
vaca=Vaca("Ema")

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(gato)
hacer_sonido_de_animal(vaca)



