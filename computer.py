import pygame
from config import BLACK

class Computer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 2
        self.jump = False
        self.jump_velocity = 0
        self.gravity = 1
        self.blocking = False
        self.ground_y = y

    def update(self, player_x):
        # Simple AI: move toward player
        if abs(self.x - player_x) > 60:
            if self.x > player_x:
                self.x -= self.speed
            elif self.x < player_x:
                self.x += self.speed

        # Jumping behavior: jump if the player is too close or as a reaction
        if abs(self.x - player_x) < 100 and not self.jump:
            self.jump = True
            self.jump_velocity = -15

        # Update jump position
        if self.jump:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity
            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.jump = False

    def attack_player(self, player):
        if abs(self.x - player.x) < 60 and not player.blocking:
            player.health -= 0.2

    def handle_blocking(self, player):
        # Block if player is attacking and computer is close
        if abs(self.x - player.x) < 60 and player.attacking:
            self.blocking = True
        else:
            self.blocking = False

    def draw(self, screen):
        x, y = self.x, self.y

        # Head
        pygame.draw.circle(screen, BLACK, (x, y), 10, 2)
        # Body
        pygame.draw.line(screen, BLACK, (x, y + 10), (x, y + 40), 2)
        # Arms (show blocking if blocking)
        arm_color = BLACK if not self.blocking else (200, 0, 0)
        pygame.draw.line(screen, arm_color, (x - 15, y + 20), (x + 15, y + 20), 2)
        # Legs
        pygame.draw.line(screen, BLACK, (x, y + 40), (x - 10, y + 60), 2)
        pygame.draw.line(screen, BLACK, (x, y + 40), (x + 10, y + 60), 2)
        # Stick (always left-facing)
        pygame.draw.line(screen, BLACK, (x - 15, y + 20), (x - 50, y + 10), 2)
