import random
import pygame

class Atacar:
    def ataque(self):
        print("Hizo daño")


class Defender:
    def defender(self):
        print("Se defendió")


class AtaqueSp:
    def ataqueSp(self):
        print("Hizo un ataque especial")


class Persona(Atacar, Defender, AtaqueSp):
    def __init__(self, nombre, atk, defensa, spatk, vida):
        self.nombre = nombre
        self.atk = atk
        self.defensa = defensa
        self.spatk = spatk
        self.vida = vida


class Sombra:
    def __init__(self, atk, defensa, spatk, insta, vida):
        self.atk = atk
        self.defensa = defensa
        self.spatk = spatk
        self.insta = insta
        self.vida = vida


# Menú de juego

print("------------------------")
print("-----MENU PRINCIPAL-----")
print("------------------------")
eleccion = input("¿Jugar? [Y/N]: ").lower()
pygame.init()  # Inicializa todos los módulos de pygame
pygame.mixer.init()  # Inicializa específicamente el módulo de audio

# Cargar música
pygame.mixer.music.load("assets/musica.mp3")  # Cambia la ruta según tu carpeta
pygame.mixer.music.play(-1)  # Reproduce la música en bucle
atk_aleatorio = random.randint(1,50)
defensa_aleatorio = random.randint(1,50)
spatk_aleatorio = random.randint(1,50)
vida_aleatorio = random.randint(50,200)

if eleccion == 'y':
    thanatos = Persona("Thanatos", 45, 41, 49, 100)
    hellel = Persona("Hellel", 56, 56, 57, 100)
    jack_frost = Persona("Jack Frost", 10, 12, 14, 100)
        
    # Crear personajes

    sombra = Sombra(atk_aleatorio, defensa_aleatorio, spatk_aleatorio, 999, vida_aleatorio)

    # Lista de personajes
    personas = [thanatos, hellel, jack_frost]

    # Mostrar opciones
    print("Elige tu Persona:")
    for i, p in enumerate(personas):
        print(f"{i + 1}. {p.nombre} (ATK: {p.atk}, DEF: {p.defensa}, SPATK: {p.spatk}, VIDA: {p.vida})")

    eleccionP = int(input("Elija su PERSONA (1-3): ")) - 1  # Restamos 1 para acceder correctamente al índice

    if 0 <= eleccionP < len(personas):
        persona_seleccionada = personas[eleccionP]
        print(f"Eligió a: {persona_seleccionada.nombre}")
    else:
        print("Selección inválida.")

turno = 0

while persona_seleccionada.vida > 0 and sombra.vida > 0:
        
        turno += 1
        print(f"{persona_seleccionada.nombre}: {persona_seleccionada.vida} HP")
        print(f"Sombra {sombra.vida} HP")
        print(f"Turno: {turno}")
        print("-----------------")
        print("1. Atacar")
        print("2. Defender")
        print("3. Ataque especial")
        print("------------------")

        ataque_defendido = persona_seleccionada.defensa * .1

        accion = int(input("Que quiere hacer?: "))

        #JUEGO INCIO 

        #ATQUE
        if accion == 1:
            if random.randint(0, 1) < 0.5:
                print("---EL ATAQUE FALLO---")
            else:
                sombra.vida -= persona_seleccionada.atk * .1
                persona_seleccionada.vida -= sombra.atk * .1

        #DEFENSA
        if accion == 2:
            print("Te has defendido")
            if random.randint(0, 1) < 0.5:
                print("---EL ATAQUE FALLO---")
            else:
                persona_seleccionada.vida -= sombra.atk * ataque_defendido


        #ATQUE ESPECIAL
        if accion == 3:
            if random.randint(0, 1) < 0.9:
                print("---EL ATAQUE FALLO---")
            else:
                sombra.vida -= persona_seleccionada.atk * .8
                persona_seleccionada.vida -= sombra.atk * .1
            


