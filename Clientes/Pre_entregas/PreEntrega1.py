db = {'Andres' : '123'}

def Check(User, Pass, Select):
  if Select == "2":  
    if User in db: 
      print(" Usuario repetido ")
      print(" Por favor Ingrese con otro Usuario ")
      Ingreso()
    else:  
      db[User] = Pass
      print(' Gracias por registrarse ')
      Ingreso()
  else:
    if User in db:
      if Pass == db[User]:
        print(" Session iniciada ")
      else:
        print("Error contraseña no valida")  
        Ingreso()
    else:
      print("Error usuario no valido")
      Ingreso()
        
def Ingreso():
  Select = (input("ingrese [1] para iniciar Session o [2] para Registrarse "))  
  Select = str(Select)
  if Select == "2":
    print("------ Ingrese Usuario ------")
    User = input()
    print("------ Ingrese Contraseña ------")
    Pass = input()
    Check(User, Pass, Select)
  elif Select == "1":
    User = input("------ Ingrese Usuario ------ ")
    Pass = input("------ Ingrese Contraseña ------ ")
    Check(User, Pass, Select)
  else:
    print("Opcion no valida")
    Ingreso()

def ListaUsuarios():
  for k in db.keys():
      print("Usuario '" + k + "'" + "  -->  Contraseña '" + db[k] + "'")

