import pygame
import sys
from config import WIDTH, HEIGHT, WHITE, RED, GREEN
from player import Player
from computer import Computer

pygame.init()

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Fight")

# Clock
clock = pygame.time.Clock()
running = True

# Create fighters
player = Player(100, 450)
computer = Computer(700, 450)

# Health bar
def draw_health_bar(x, y, health):
    pygame.draw.rect(screen, RED, (x, y, 100, 10))
    pygame.draw.rect(screen, GREEN, (x, y, max(0, health), 10))

# Game loop
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input & updates
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.update()
    computer.update(player.x)
    computer.attack_player(player)
    computer.handle_blocking(player)

    # Player attack
    if player.attacking:
        if abs(player.x + 50 - computer.x) < 20:
            computer.health -= 1

    # Win check
    if player.health <= 0 or computer.health <= 0:
        winner = "Player" if player.health > computer.health else "Computer"
        print(f"{winner} wins!")
        pygame.time.delay(2000)
        player.health = 100
        computer.health = 100
        player.x = 100
        computer.x = 700

    # Draw
    screen.fill(WHITE)
    draw_health_bar(20, 20, player.health)
    draw_health_bar(WIDTH - 120, 20, computer.health)
    player.draw(screen)
    computer.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
