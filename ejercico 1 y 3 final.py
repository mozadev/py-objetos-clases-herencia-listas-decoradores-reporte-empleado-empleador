# COMPLETE LA SIGUIENTE CLASE
class Persona:
    def __init__(self, nombre, telefono, email):
        self.nombr = nombre
        self.telefon = telefono
        self.emai = email

    @property
    def nombre(self):
        return self.nombr

    @property
    def telefono(self):
        return self.telefon

    @property
    def email(self):
        return self.emai

    @nombre.setter
    def nombre(self,value):
        if isinstance(value, str):
            self.nombr = value
        else:
            raise ValueError(str(value) + " TIPO NO ES STR")



    @telefono.setter
    def telefono(self, value):
        subcadena = value[3]
        subcadena2= value[7]

        if subcadena=='-' and subcadena2=='-':
            self.telefon = value
        else:
            raise ValueError(str(value) + " TIPO NO TIENE EL FORMATO TELEFONICO")

    @email.setter
    def email(self, value):
        subcadena = value[-9:]
        if subcadena == '@mail.com':
            self.emai = value
        else:
            raise ValueError(str(value) + " TIPO NO TIENE EL FORMATO DE EMAIL")

    def __repr__(self):
        return "Persona[nombre={}, telefono={}, email={}]".format(
            self.nombr, self.telefon, self.emai)


# PRUEBA DE LA CLASE - ESTA CELDA DEBE DE EJECUTAR CORRECTAMENTE (3 ptos)
p1 = Persona('Alan', '986-725-125', 'alan@mail.com')

print(p1.nombre)

# p1.nombre=1243
# print(p1.nombre)


# ESTA LINEA DEBE GENERAR UNA EXCEPCION TYPE ERROR (TIPO NO TIENE EL FORMATO TELEFONICO) (1 pto)
# p1.telefono = '987635253'
# print(p1.telefono)

# ESTA LINEA DEBE DE GENERAR UNA EXCEPCION TYPE ERROR (TIPO NO TIENE EL FORMATO DE EMAIL) (1 pto)
p1.email = "cesar@mail.com"
print(p1.email)




# DEFINA LAS CLASES JEFE Y EMPLEADO COMO CLASES HIJA DE LA CLASE PERSONA (2 ptos)
class Jefe(Persona):
    def __init__(self,nombre, telefono,email,equipo):
        super().__init__(nombre, telefono,email)
        self.equipo=equipo


class Empleado(Persona):
    def __init__(self, nombre, telefono, email, equipo):
        super().__init__(nombre, telefono, email)
        self.equipo = equipo


# EN ESTA CELDA SE DEFINEN LOS OBJETOS Y LA LISTA DE PERSONAL DE LA ORGANIZACIÖN. NO LA MODIFIQUE!
# NOTE QUE EL ULTIMO CAMPO EN AMBAS CLASES ES EL EQUIPO AL QUE PERTENECEN
personal = []
personal.append(Jefe("Juan Bellido", "876-726-112", "supervisor1@mail.com", 1))
personal.append(Jefe("Sandra Bustamante", "981-233-991", "supervisor2@mail.com", 2))
personal.append(Jefe("Andres Cervantes", "972-158-935", "supervisor3@mail.com", 3))
personal.append(Empleado("Maria Perez", "928-222-123", "empleado1@mail.com", 1))
personal.append(Empleado("Pedro Garcia", "912-281-383", "empleado2@mail.com", 2))
personal.append(Empleado("Marco Benavente", "998-293-921", "empleado3@mail.com", 2))
personal.append(Empleado("Alejandro Flores", "934-194-990", "empleado4@mail.com", 1))
personal.append(Empleado("Ernesto Gamarra", "918-017-121", "empleado5@mail.com", 1))
personal.append(Empleado("Sofia Fuentes", "908-024-101", "empleado6@mail.com", 2))
personal.append(Empleado("Diana Santos", "962-682-164", "empleado7@mail.com", 1))
personal.append(Empleado("Anibal Lopez", "912-198-852", "empleado8@mail.com", 1))
personal.append(Empleado("Daniel Peredo", "912-567-159", "empleado9@mail.com", 3))
personal.append(Empleado("Christian Rojas", "933-228-753", "empleado10@mail.com", 3))
personal.append(Empleado("Marcela Tavara", "976-670-761", "empleado11@mail.com", 1))
personal.append(Empleado("Patricia Chavez", "902-098-468", "empleado12@mail.com", 3))
print("\n")
# DEFINA LAS FUNCIONES SEGUN LAS ESPECIFICACION EN EL DOCSTRING (3 ptos)
def listar_jefes(personal):
    # Retorna una lista con los objetos Jefe de la lista de personal


    for x in personal:
        subcadena = x.emai[0:10]
        if(subcadena=='supervisor'):
            print(x.nombr)

listar_jefes(personal)
print("\n")


def listar_empleados(personal):
    # Retorna una lista con los objeto Empleado de la lista de personal

    for x in personal:
        subcadena = x.emai[0:8]
        if (subcadena == 'empleado'):
            print(x.nombr)


listar_empleados(personal)
print("\n")
empleados=[]
for x in personal:
    subcadena = x.emai[0:8]
    if (subcadena == 'empleado'):
        empleados.append(x)


def lista_empleados_jefe(jefe, empleados):
    # Retorna una lista con los empleados supervisados por un jefe
    # a partir de un objeto jefe y una lista de empleados
    if(jefe=="Juan Bellido"):equipo=1
    if (jefe == "Sandra Bustamante"): equipo = 2
    if (jefe == "Andres Cervantes"): equipo = 3
    for x in empleados:

        if (x.equipo == equipo):
            print("nombre: "+ x.nombr+" "+"telefono: "+x.telefon+" "+"email: "+x.emai)


lista_empleados_jefe("Juan Bellido", empleados)

# informe global
print("\n")

def reporteGLobal():
    print("jefe: "+"Juan Bellido")
    print("equipo: "+ "1")
    print("lista a supervisar:")
    lista_empleados_jefe("Juan Bellido", empleados)
    print("\n")
    print("jefe: " +  "Sandra Bustamante")
    print("equipo: " + "2")
    print("lista a supervisar:")
    lista_empleados_jefe("Sandra Bustamante", empleados)
    print("\n")
    print("jefe: " +  "Andres Cervantes")
    print("equipo: " + "3")
    print("lista a supervisar:")
    lista_empleados_jefe( "Andres Cervantes", empleados)


reporteGLobal()