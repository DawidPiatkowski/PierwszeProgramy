import pygame

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the dimensions of the game board
BOARD_WIDTH = 300
BOARD_HEIGHT = 300

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the font
font = pygame.font.SysFont("Arial", 50)

def draw_board():
    # Draw the horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 2)

    # Draw the vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 2)

def draw_x(row, col):
    # Draw the X symbol in the specified row and column
    x_pos = col * 100 + 50
    y_pos = row * 100 + 50
    pygame.draw.line(screen, BLACK, (x_pos - 40, y_pos - 40), (x_pos + 40, y_pos + 40), 2)
    pygame.draw.line(screen, BLACK, (x_pos - 40, y_pos + 40), (x_pos + 40, y_pos - 40), 2)

def draw_o(row, col):
    # Draw the O symbol in the specified row and column
    x_pos = col * 100 + 50
    y_pos = row * 100 + 50
    pygame.draw.circle(screen, BLACK, (x_pos, y_pos), 40, 2)

def check_win(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    game_over = False
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_player == "X":
                    col = event.pos[0] // 100
                    row = event.pos[1] // 100
                    if board[row][col] == " ":
                        board[row][col] = current_player
                        draw_x(row, col)
                        current_player = "O"
                        if check_win(board):
                            winner
