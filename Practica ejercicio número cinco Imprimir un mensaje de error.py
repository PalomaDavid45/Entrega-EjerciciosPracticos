"""
def test_var_args(f_arg,o_arg = 0,*argv): #args
    print("primer argumento normal",f_arg)
    print("segundo argumento opcional",o_arg)
    print(*argv) #esto regresa una tupla
    for arg in *argv:
        print("argumentos de *argv:",arg)
    print("error,no se pasaron suficientes argumentos")
"""