import random 
import pygame

class Objetos_Curativos():
    def __init__(self, ps_curados, nombre, id, info):
        self.ps_curados = ps_curados
        self.nombre = nombre
        self.id = id
        self.info = info

class Objetos_Estadisticas():
    def __init__(self, buff, nombre, id, info):
        pass
    
class Armas():
    def __init__(self, plus_ataque, nombre, id):
        self.plus_ataque = plus_ataque
        self.nombre = nombre
        self.id = id

class Armaduras():
    def __init__(self, defensa_plus, nombre, id):
        self.plus_ataque = defensa_plus
        self.nombre = nombre
        self.id = id



class Personaje():
    def __init__(self, nombre, ataque, defensa, vida, nivel, experiencia):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = nivel
        self.experiencia = experiencia
    


class Enemigo ():
    def __init__(self, nombre, ataque, defensa, vida, nivel, xp_dada):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = nivel
        self.xp_dada = xp_dada


print ("Menu Principal")
comenzar = input("¿Iniciar Juego? (Y/N): ").lower()
if comenzar == 'y':
    nombre = input("Ingrese su nombre: ")
    jugador = Personaje(nombre, 5, 1, 50, 1, 10)
    print(f"Bienvenido al juego {jugador.nombre}. \nAtaque: {jugador.ataque}. \nDefensa: {jugador.defensa}. \nHp: {jugador.vida}. \nExp Necesaria para subir de nivel: {jugador.experiencia}.")

    objetos_curativos = []
    obetos_estadisticos = []


    #funciones
    def generar_enemigo(piso):
        nombre = f"Monstruo del Piso {piso}"
        ataque = 1 + piso
        defensa = 1 + piso // 2
        vida = 40 + (10 * piso)
        nivel = piso
        xp_dada = 2 + piso

        return Enemigo(nombre, ataque, defensa, vida, nivel, xp_dada)

    piso = 0
    enemigo = generar_enemigo(piso)

    while jugador.vida > 0:
        piso += 1
        enemigo = generar_enemigo(piso)
        print(f"\n¡Un {enemigo.nombre} ha aparecido!")

        #Combate
        while enemigo.vida > 0 and jugador.vida > 0:
             
             print(f"HP Jugador: {jugador.vida}")
             print(f"HP Enemigo: {enemigo.vida}")
             print("1.- Atacar")
             print("2.- Defender")
             print("3.- Objeto")

             accion = int(input("¿Ahora que haras?: "))  #Ataque
             if accion == 1:
                personaje_fallido = random.randint(0,1)
                enemigo_fallido = random.randint(0,1)

                if personaje_fallido < 0.3:
                    print("¡¡TU ATAQUE HA FALLADO!!")
                else:
                    enemigo.vida -= jugador.ataque

                    print(f"TU ATAQUE HA IMPACTADO. \nHas quitado: {jugador.ataque} PS")
            
                if enemigo.vida <= 0:
                    print(f"Enemigo derrotado, has conseguido {enemigo.xp_dada}")

                    jugador.experiencia -= enemigo.xp_dada


                if enemigo_fallido < 0.3:
                    print("EL ATAQUE ENEMIGO HA FALLADO")
                else: 
                    print("EL ATAQUE ENEMIGO HA IMPACTADO")
                    jugador.vida -= enemigo.ataque

                    if jugador.vida <= 0:
                        print(f"Has sido derrotado, llegaste al piso {piso}")




       
            





