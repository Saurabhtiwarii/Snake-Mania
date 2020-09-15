import pygame
x = pygame.init()
game_window = pygame.display.set_mode((600,500))
pygame.display.set_caption("Snake Mania")
# game specific variable
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()
