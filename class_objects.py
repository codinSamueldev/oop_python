#Everything is an object, so classes are the things that compose that object.

#We use Pascal case when naming a class. 
class Celular(): 
    marca = "Samsung" 
    modelo = "S23" 
    camara = "48MP" 
    
#We can create many objects as we want and link them with the attributes set up before. 

celular1 = Celular() 
celular2 = Celular() 
celular3 = Celular() 
celular4 = Celular()

print(type(celular1.modelo)) 
print(celular1.marca) 
print(celular1.camara)