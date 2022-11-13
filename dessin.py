import random

import EZ


def background():
    """ GÃ©nÃ¨re un fond """
    EZ.trace_rectangle_droit(0, 0, 800, 600, "5560af")


def montagne(x, y, zoom):
    """ Dessine une montagne en (x, y) avec un zoom """
    light_green = ["6dbe45", "41b54a", "92c83e", "6dbe45", "53ba6b"]
    dark_green = ["27b44b", "089547", "27b44e", "0fa252"]
    EZ.trace_triangle(x, y, x + 50, y, x + 50, y - 100, random.choice(light_green), zoom)
    EZ.trace_triangle(x + 50, y, x + 100, y, x + 50, y - 100, random.choice(dark_green), zoom)


def terre():
    """ Dessine la terre """
    brown = ["a97c52", "755639", "a6835b"]
    green = ["8ecc8b", "6a9968"]
    EZ.trace_rectangle_droit(0, 500, 800, 100, random.choice(brown))
    EZ.trace_rectangle_droit(0, 450, 800, 50, random.choice(green))


def arbre(x, y, zoom):
    """ Dessine un arbre en (x, y) avec un zoom """
    brown = ["6c584a", "413020"]
    light_brown = ["c4996c", "a6835b"]
    EZ.trace_rectangle_droit(x, y, 5, 40, random.choice(light_brown), zoom)
    EZ.trace_rectangle_droit(x + 5, y, 5, 40, random.choice(brown), zoom)

    EZ.trace_disque(x + 5, y - 30, 30, "078640", zoom)
    EZ.trace_disque(x + 5, y - 30, 20, "3aa342", zoom)
    EZ.trace_disque(x + 5, y - 30, 10, "078640", zoom)


def lune(y, zoom):
    """ Dessine une lune en (x, y) avec un zoom """
    x = random.randint(100, 700)
    EZ.trace_disque(x, y, 50, "f5ea36", zoom)
    EZ.trace_disque(x + 10, y - 10, 40, "5560af", zoom)


def imeuble(x, y, zoom):
    """ Dessine un immeuble en (x, y) avec un zoom """
    color = ["e43d69", "f98437", "c973b0"]
    current_color = random.choice(color)
    EZ.trace_rectangle_droit(x, y, 110, 150, current_color, zoom)
    # Dessine aléatoirement le toit de l'immeuble parmi 3 possibilités
    ran = random.randint(0, 2)
    if ran == 0:
        EZ.trace_triangle(x - 10, y, x + 120, y, x + 55, y - 75, current_color, zoom)
    elif ran == 1:
        EZ.trace_triangle(x - 10, y, x + 115, y, x + 115, y - 40, current_color, zoom)
    else:
        EZ.trace_rectangle_droit(x - 5, y - 20, 120, 20, current_color, zoom)
        EZ.trace_rectangle_droit(x + 5, y - 40, 100, 20, current_color, zoom)
        EZ.trace_rectangle_droit(x + 15, y - 60, 80, 20, current_color, zoom)
        EZ.trace_rectangle_droit(x + 25, y - 80, 60, 20, current_color, zoom)
        EZ.trace_rectangle_droit(x + 45, y - 100, 20, 20, current_color, zoom)

    # Dessine les fenêtres avec une ombre
    for i in range(5):
        for j in range(3):
            EZ.trace_rectangle_droit(x + 10 + i * 20, y + 10 + j * 40, 10, 30, "ffffff", zoom)
            EZ.trace_rectangle_droit(x + 10 + i * 20 + 1, y + 10 + j * 40 + 1, 10, 30, "000000", zoom, 75)


def generer_dessin():
    """ GÃ©nÃ¨re un dessin """
    EZ.creation_fenetre(800, 600)

    # GÃ©nÃ¨re le fond
    background()

    # Dessine la terre
    terre()

    # Dessine les montagnes
    for i in [50, 290, 425]:
        montagne(i, 300, 1.5)
        montagne(i + 10, 180, 2.5)
    montagne(130, 150, 3)

    # Dessine les immeubles
    for i in [200, 350, 600]:
        imeuble(i, 301, 1)

    # Dessine les arbres
    for i in [50, 101, 130, 210]:
        arbre(i, 450, 1)

    # Dessine la lune
    lune(100, 1)

    EZ.mise_a_jour()
    EZ.attendre_action()
    EZ.destruction_fenetre()


generer_dessin()
