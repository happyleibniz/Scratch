import sys
import time
import random
import pygame
from pygame import mixer

pygame.init()
mixer.init()
WIDTH = 480
HEIGHT = 360


def stay():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class Main:
    global WIDTH, HEIGHT

    def __init__(self):
        self.background_colour = (255, 255, 255)  # by default
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)  # by default
        pygame.display.set_caption(' ')  # no caption
        self.screen.fill(self.background_colour)
        pygame.display.flip()


class Background(Main):
    global WIDTH, HEIGHT

    def __init__(self, name: str, background_images: list, sounds: list = None):
        super().__init__()
        self.name = name
        self.background_images = background_images
        self.sounds = sounds
        self.current_bg_image_number = 0
        self.current_bg_image_length = len(self.background_images) - 1
        self.current_bg_image = pygame.image.load(self.background_images[self.current_bg_image_number])

    def show(self):
        self.screen.blit(self.current_bg_image, (0, 0))


class Sprite(Main):
    global WIDTH, HEIGHT

    def __init__(self, name: str, sprite_images: list, pos_x: int = WIDTH // 2, pos_y: int = HEIGHT // 2,
                 size=100, direction=90, sounds: list = None):
        super().__init__()
        self.sounds = sounds
        mixer.music.load(str(sounds[0]))
        mixer.music.set_volume(0.7)
        self.sprite_name = name
        self.sprite_images = sprite_images
        self.size = size / 100
        self.current_sprite_image_number = 0
        self.current_sprite_image_length = len(self.sprite_images) - 1
        self.current_sprite_image = pygame.transform.rotate(
            pygame.image.load(self.sprite_images[self.current_sprite_image_number]), direction - 90)
        self.current_sprite_image = pygame.transform.scale(
            self.current_sprite_image,
            (
                int(self.current_sprite_image.get_width() * self.size),
                int(self.current_sprite_image.get_height() * self.size)
            )
        )
        self.position_x = pos_x
        self.position_y = pos_y
        self.direction = direction - 90

    def show(self):
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def play(self):
        mixer.music.play()

    def move(self, steps):  # TODO: BUG FIX PLZ
        self.screen.fill(self.background_colour)
        self.position_x += steps * 0.025
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def wait_how_many_seconds(self, seconds: int):
        time.sleep(seconds)

    def set_size_to(self, percent):

        self.size = percent / 100
        self.current_sprite_image = pygame.transform.scale(
            self.current_sprite_image,
            (
                self.current_sprite_image.get_width() * self.size,
                self.current_sprite_image.get_height() * self.size
            )
        )
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def change_x_by(self, int_value: int):
        self.position_x += int_value
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def change_y_by(self, int_value: int):
        self.position_y += int_value
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def set_x_to(self, x_coord: int):
        self.position_x = x_coord
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def set_y_to(self, y_coord: int):
        self.position_x = y_coord
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def goto(self, x, y):
        self.position_y = y
        self.position_x = x
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (x, y))

    def go_to(self, random_position_or_mouse_cursor: str):
        """No to be confused with goto(x, y)"""
        if random_position_or_mouse_cursor == "random position":
            self.position_y = random.randint(1, WIDTH)
            self.position_x = random.randint(1, HEIGHT)
            self.screen.fill(self.background_colour)
            self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))
        elif random_position_or_mouse_cursor == "mouse-pointer":
            pass
        else:
            raise RuntimeError(
                'Please select the following argument for the function : random position OR mouse-pointer'
            )

    def turn_right(self, degree):
        self.current_sprite_image = pygame.transform.rotate(self.current_sprite_image, self.direction - degree)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def turn_left(self, degree):
        self.current_sprite_image = pygame.transform.rotate(self.current_sprite_image, self.direction + degree)
        self.screen.fill(self.background_colour)
        self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))

    def next_costume(self):
        self.current_sprite_image_number += 1
        if self.current_sprite_image_number <= self.current_sprite_image_length:
            self.current_sprite_image = pygame.transform.rotate(
                pygame.image.load(self.sprite_images[self.current_sprite_image_number]), self.direction - 90)
            self.current_sprite_image = pygame.transform.scale(
                self.current_sprite_image,
                (
                    self.current_sprite_image.get_width() * self.size,
                    self.current_sprite_image.get_height() * self.size
                )
            )
            self.screen.fill(self.background_colour)
            self.screen.blit(self.current_sprite_image, (self.position_x, self.position_y))
        else:
            return 0

    def update(self):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
