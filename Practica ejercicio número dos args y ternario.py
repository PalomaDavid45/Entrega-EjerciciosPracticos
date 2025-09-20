"""
def test_var_args(f_arg,o_arg = 0,*argv): #args
    print("primer argumento normal:", f_arg)
    print("argumento opcional",o_arg)
    print(argv) #esto regresa una tupla
    for arg in argv:
        print("argumentos de *argv:", arg)
    print("Finalizo")

test_var_args('python','fool', 'bar', "hola", "argumento","Sol","Leopardo","Mapache","Boss")

"""

def saludo(*args,**kwargs):
    print(args)
    print(len(args))
    print(kwargs) #esto nos regresa un diccionario
    for key, value in kwargs.items():
        print("{34} = {35}".format(key, value))

saludo("hola",nombre = "Paloma", apellido = "Loyola David", provincia = "Buenos Aires")
