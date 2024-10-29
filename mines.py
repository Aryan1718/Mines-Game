import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 5
CELL_SIZE = WIDTH // GRID_SIZE
MIN_MINES = 1
MAX_MINES = 24

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BUTTON_COLOR = (50, 150, 50)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mines Game")

# Game Variables
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
game_over = False
won = False
num_mines = MIN_MINES  # Default number of mines

# Function to place mines randomly
def setup_game():
    global grid, num_mines
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines_placed = 0
    print("num_mines_from_mines ",num_mines)
    # Place mines
    while mines_placed < num_mines:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        
        if grid[x][y] != -1:
            grid[x][y] = -1
            mines_placed += 1

    # Ensure at least one green cell (diamond) by selecting a random cell that is not a mine
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] !=-1:
                print("col and row",i,j)
        

# Function to draw the grid
def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[x][y]:
                if grid[x][y] == -1:
                    pygame.draw.rect(screen, RED, rect)  # Show mine
                else:
                    pygame.draw.rect(screen, GREEN, rect)  # Show diamond
            else:
                pygame.draw.rect(screen, GRAY, rect)  # Hide cell
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw cell border

# Function to reset the game
def reset_game():
    global game_over, won
    game_over = False
    won = False
    setup_game()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            revealed[x][y] = False

# Function to display a game over message
def show_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))
    
    # Create buttons for restart and exit
    restart_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 60, WIDTH // 2, 50)
    
    pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
    
    restart_text = font.render("Restart", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)
    
    screen.blit(restart_text, (restart_button.x + 40, restart_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 40, exit_button.y + 10))
    
    pygame.display.flip()
    
    # Wait for user interaction
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    reset_game()
                    waiting = False
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Function to display the winning message
def show_win_popup():
    global won
    won = True
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, GREEN)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))
    
    # Create buttons for restart and exit
    restart_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 60, WIDTH // 2, 50)
    
    pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
    
    restart_text = font.render("Restart", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)
    
    screen.blit(restart_text, (restart_button.x + 40, restart_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 40, exit_button.y + 10))
    
    pygame.display.flip()
    
    # Wait for user interaction
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    reset_game()
                    waiting = False
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Function to display the mine selection popup
def mine_selection_popup():
    global num_mines
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 40)
        title = font.render("Select Number of Mines (1-24):", True, BLACK)
        screen.blit(title, (WIDTH // 8, HEIGHT // 4))

        # Input box for user to see current number of mines
        input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
        pygame.draw.rect(screen, BLACK, input_box, 2)

        # Show current number of mines in the input box
        input_text = font.render(str(num_mines), True, BLACK)
        screen.blit(input_text, (input_box.x + 10, input_box.y + 10))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Confirm input
                    if MIN_MINES <= num_mines <= MAX_MINES:
                        return  # Proceed to the game
                elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                    num_mines = MIN_MINES  # Reset to minimum
                elif event.key == pygame.K_UP:  # Increase mines
                    if num_mines < MAX_MINES:
                        num_mines += 1
                elif event.key == pygame.K_DOWN:  # Decrease mines
                    if num_mines > MIN_MINES:
                        num_mines -= 1

# Game loop
if __name__ == '__main__':
    mine_selection_popup()  # Show mine selection popup before the game starts
    reset_game()  # Reset game with the selected number of mines
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not won:
                x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                revealed[x][y] = True  # Allow clicking anywhere on the grid
                if grid[x][y] == -1:
                    game_over = True
                elif all(revealed[i][j] or grid[i][j] == -1 for i in range(GRID_SIZE) for j in range(GRID_SIZE)):
                    won = True  # Set win state when all non-mine cells are cleared

        screen.fill(WHITE)
        draw_grid()
        
        if game_over:
            show_game_over()  # Show game over popup
        elif won:
            show_win_popup()  # Show win popup

        pygame.display.flip()
