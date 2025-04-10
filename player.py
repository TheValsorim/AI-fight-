import pygame
from config import BLACK

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.jump = False
        self.jump_velocity = 0
        self.gravity = 1
        self.attacking = False
        self.attack_cooldown = 0
        self.blocking = False
        self.ground_y = y

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_SPACE] and self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 20
        if keys[pygame.K_w] and not self.jump:
            self.jump = True
            self.jump_velocity = -15
        self.blocking = keys[pygame.K_s]

    def update(self):
        # Cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            if self.attack_cooldown == 0:
                self.attacking = False

        # Jump
        if self.jump:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity
            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.jump = False

        # Keep in screen
        self.x = max(20, min(800 - 20, self.x))  # 800 = screen width

    def draw(self, screen):
        color = (100, 100, 100) if self.blocking else BLACK
        x, y = self.x, self.y

        # Head
        pygame.draw.circle(screen, color, (x, y), 10, 2)
        # Body
        pygame.draw.line(screen, color, (x, y + 10), (x, y + 40), 2)
        # Arms
        pygame.draw.line(screen, color, (x - 15, y + 20), (x + 15, y + 20), 2)
        # Legs
        pygame.draw.line(screen, color, (x, y + 40), (x - 10, y + 60), 2)
        pygame.draw.line(screen, color, (x, y + 40), (x + 10, y + 60), 2)
        # Stick
        pygame.draw.line(screen, color, (x + 15, y + 20), (x + 50, y + 10), 4 if self.attacking else 2)
