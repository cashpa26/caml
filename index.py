# ejemplo sencillo de código en Python para simular el movimiento de Pac-Man en un tablero


import os
import sys
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(pacman_pos):
    board = [
        "#############",
        "#           #",
        "#   o   o   #",
        "#           #",
        "#############"
    ]
    x, y = pacman_pos
    board[y] = board[y][:x] + 'C' + board[y][x+1:]  # 'C' representa a Pac-Man
    for row in board:
        print(row)

def main():
    pacman_pos = [2, 2]  # Posición inicial de Pac-Man

    while True:
        clear_screen()
        print_board(pacman_pos)

        key = msvcrt.getch()  # Captura la tecla presionada
        if key == b'w':
            pacman_pos[1] -= 1
        elif key == b's':
            pacman_pos[1] += 1
        elif key == b'a':
            pacman_pos[0] -= 1
        elif key == b'd':
            pacman_pos[0] += 1
        elif key == b'q':
            print("¡Juego terminado!")
            break

if __name__ == "__main__":
    main()
