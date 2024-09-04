import random
import diceart as dc

# Settings
COLOR_ORDER = ['yellow', 'red']
players = {
    'yellow': {'position': (1, 14), 'symbol': "♟"},
    'red': {'position': (13, 17), 'symbol': "♙"}
}

# Menu
def Instrucciones():
    print("Instrucciones")
    print()
    print("1. Con un par(Los dos dados concuerden con el mismo número)se puede sacar maximo 2 fichas (ó una de ser el caso).")
    print("2. Es obligatorio primero salir de la cárcel. Si no se tienen fichas en la cárcel, la prioridad será capturar la ficha del jugador contrario.")
    print("3. Si se tiene una ficha en la cárcel y se obtiene un par (ambos dados muestran el mismo número), se saca la ficha de la cárcel y se utiliza el restante con una ficha diferente a la que salió. En caso de no tener otra ficha, se perderá ese movimiento y solo se saldrá de la cárcel.")
    print("4. Si saca un par(Los dos dados concuerden con el mismo número)le vuelve a tirar.")
    print("5. Solo se permiten dos fichas máximo por cada casilla.")
    print("6. Si una ficha se encuentra en una salida o en un seguro, esta ficha no puede ser capturada por ninguna otra. Esta regla no se cumple cuando una ficha se encuentra en la salida de un equipo enemigo junto a una ficha del equipo enemigo y el equipo enemigo saca una ficha en su turno, éste capturará a la ficha que no pertenece a dicha salida.")
    print("7. Si dos fichas se encuentran en una casilla, tenemos estas posibilidades:")
    print("a) Son del mismo color/equipo, y por ende, forman un bloqueo siempre.")
    print("b) Son de diferente color/equipo pero se encuentran en un seguro o en una salida y entonces forman un bloqueo.")
    print("c) Son de diferente equipo y no se encuentran en ninguna casilla especial, por lo que la que la ficha que llega en segundo lugar a la casilla captura a laprimera ficha y la envía a su respectiva cárcel.")
    print("8. Si no existe un movimiento posible para ninguna de las fichas, ya sea porque existe un bloqueo o porque la casilla de llegada está a menos movimientos de lo que se obtuvo en los dados, entonces el turno simplemente pasa.")
    print("9. Si una ficha es coronada, se le concederán 10 movimientos adicionales con otra ficha, siempre que sea permitido. Si se captura una ficha, se le otorgarán 20 movimientos adicionales con la ficha que elija, si es posible. Estos movimientos extra se aplican inmediatamente al coronar una ficha o al capturar una ficha.")
    print("10. Si un jugador obtiene tres pares consecutivos, coronará inmediatamente la ficha más adelantada que tenga. (Si solo tiene una ficha, ganará la partida).")
    print("11.Un jugador no puede bloquear una casilla por más de dos turnos; al tercer turno, estará obligado a mover una de sus fichas de bloqueo.")
    print("12. Gana quien logre coronar todas sus fichas primero, momento en el cual la partida terminará.")
    print()
    input("Presione ENTER para regresar al menú")
    menu()

def dos_jugadores():
    COLOR_ORDER = ['yellow', 'red']
    players = {
        'yellow': {'position': (1, 14), 'symbol': "♟"},
        'red': {'position': (13, 17), 'symbol': "♙"}
    }
def menu():
    print("Parques")
    print(dc.COVER_ART)
    print()
    print(">Instrucciones")
    print(">2 Jugadores")
    print(">3 Jugadores")
    a = input("Respuesta: ")

    if a == "1":
        Instrucciones()
    elif a == "2":
        print("¡Iniciando juego para dos jugadores!")
        dos_jugadores()
    else:
        print("Proximamente: Aún no lo termino profe xd")
        menu()
menu()

# Funciones

def dice():
    roll = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print_dice(roll), print_dice(roll2)
    return roll + roll2


def print_dice(roll):
    dice_face = dc.DICE_ART[roll]
    for row in dice_face:
        print(row)


def initialize_board():
    for player in players.values():
        x, y = player['position']
        board_2d[x][y] = player['symbol']

def print_board():
    for row in board_2d:
        print(' '.join(str(cell) for cell in row))


board_2d = [
    [0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 1, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 4, 4, 4, 4, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 3, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 9, 2, 9, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 9, 9, 9, 9, 9, 9, 2, 9, 9, 9, 9, 9, 9, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0]
]

# Movimiento
def move_yellow(roll):
    x, y = players['yellow']['position']
    board_2d[x][y] = 0  # Limpiar la posición actual del jugador

    if (x, y) == (1, 9):
        # Movimiento hacia abajo después de llegar a [1,9]
        while roll > 0:
            if x < 9:  # Movimiento hacia abajo
                x += 1
                roll -= 1
                if (x, y) == (9, 9):
                    players['yellow']['position'] = (x, y)
                    board_2d[x][y] = players['yellow']['symbol']
                    print("¡El jugador amarillo ha ganado!")
                    return True  # Termina el juego si el jugador amarillo gana
            else:
                break
        return False

    # Movimiento hacia [1,9]
    while roll > 0:
        if x == 1 and y < len(board_2d[0]) - 2:  # Movimiento hacia la derecha
            y += 1
        elif y == len(board_2d[0]) - 2 and x < len(board_2d) - 2:  # Movimiento hacia abajo
            x += 1
        elif x == len(board_2d) - 2 and y > 1:  # Movimiento hacia la izquierda
            y -= 1
        elif y == 1 and x > 1:  # Movimiento hacia arriba
            x -= 1

        if (x, y) == (1, 9):
            break  # Detener el movimiento cuando llegue a [1,9]

        roll -= 1

    # Revisar si el dado nos permitiría llegar a [9,9]
    if (x, y) == (1, 9):
        if roll + x > 9:
            roll = 9 - x  # Ajustar el roll para no pasarse de [9,9]

        # Movimiento hacia abajo
        while roll > 0:
            if x < 9:  # Movimiento hacia abajo
                x += 1
                roll -= 1
                if (x, y) == (9, 9):
                    players['yellow']['position'] = (x, y)
                    board_2d[x][y] = players['yellow']['symbol']
                    print("¡El jugador amarillo ha ganado!")
                    return True  # Termina el juego si el jugador amarillo gana
            else:
                break
        return False

    # Actualizar nueva posición para el jugador amarillo
    players['yellow']['position'] = (x, y)
    board_2d[x][y] = players['yellow']['symbol']

    return False


def move_red(roll):
    x, y = players['red']['position']
    board_2d[x][y] = 0  # Limpiar la posición actual del jugador

    # Movimiento hacia abajo hasta (17, 17)
    if x < 17 and y == 17:
        while roll > 0 and x < 17:
            x += 1
            roll -= 1

    # Movimiento hacia la izquierda hasta (17, 1)
    if x == 17 and y > 1:
        while roll > 0 and y > 1:
            y -= 1
            roll -= 1

    # Movimiento hacia arriba hasta (1, 1)
    if y == 1 and x > 1:
        while roll > 0 and x > 1:
            x -= 1
            roll -= 1

    # Movimiento hacia la derecha hasta (1, 17)
    if x == 1 and y < 17:
        while roll > 0 and y < 17:
            y += 1
            roll -= 1

    # Movimiento hacia abajo hasta (9, 17)
    if y == 17 and x < 9:
        while roll > 0 and x < 9:
            x += 1
            roll -= 1

    # Movimiento hacia la izquierda hasta (9, 9)
    if x == 9 and y > 9:
        while roll > 0 and y > 9:
            y -= 1
            roll -= 1

    # Actualizar nueva posición para el jugador rojo
    players['red']['position'] = (x, y)
    board_2d[x][y] = players['red']['symbol']

    # Revisar si el jugador rojo ha llegado a (9, 9)
    if (x, y) == (9, 9):
        print("¡El jugador rojo ha ganado!")
        return True  # Termina el juego si el jugador rojo gana

    return False


# Main loop
def play_game():
    initialize_board()
    while True:
        for player in COLOR_ORDER:
            roll = dice()
            print(f"{player} Ha sacado un {roll}")
            if player == 'yellow':
                if move_yellow(roll):
                    return  # Termina el juego si el jugador amarillo gana
            else:
                if move_red(roll):
                    return  # Termina el juego si el jugador rojo gana

            print_board()
            input("Presiona Enter para continuar al siguiente turno...")
            print()


# Iniciar el juego
play_game()
