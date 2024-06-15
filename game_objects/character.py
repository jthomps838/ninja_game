import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_DOWN, K_UP

from constants import WIDTH, HEIGHT, DOWN, UP, RIGHT, LEFT, WALKING_FRAME_SETUP


class Player(pygame.sprite.Sprite):

    def __init__(self,
                 filename,
                 frame_width,
                 frame_height,
                 pos_x,
                 pos_y,
                 speed):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = pygame.image.load(filename)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.walking_frame_sets = self.extract_frames(WALKING_FRAME_SETUP)
        self.frame_index = 0
        self.animation_speed = 0.01
        self.animation_counter = 0
        self.image = self.walking_frame_sets[DOWN][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.speed = speed
        self.direction = DOWN
        self.last_direction = None
        self.is_moving = False

    def extract_frames(self, frame_setup):
        frames = {frame: [] for frame in frame_setup}
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        num_frames_x = sheet_width // self.frame_width
        num_frames_y = sheet_height // self.frame_height
        # FIX-ME: spritesheet is not pulling all 4 images for each direction

        for col in range(num_frames_x):
            for row in range(num_frames_y):
                rect = (col * self.frame_width,
                        row * self.frame_height,
                        self.frame_width,
                        self.frame_height)
                print(rect)
                frame = self.sprite_sheet.subsurface(rect)

                if col == 0:
                    frames[DOWN].append(frame)
                elif col == 1:
                    frames[UP].append(frame)
                elif col == 2:
                    frames[LEFT].append(frame)
                elif col == 3:
                    frames[RIGHT].append(frame)

        return frames

    def update(self):
        self.handle_movement()
        self.animate()

    def handle_movement(self):
        #  GET KEY PRESS EVENTS
        key_press = pygame.key.get_pressed()
        self.last_direction = self.direction

        if key_press[K_DOWN]:
            self.rect.y += self.speed
            self.direction = DOWN
            self.is_moving = True
        elif key_press[K_UP]:
            self.rect.y -= self.speed
            self.direction = UP
            self.is_moving = True
        elif key_press[K_LEFT]:
            self.rect.x -= self.speed
            self.direction = LEFT
            self.is_moving = True
        elif key_press[K_RIGHT]:
            self.rect.x += self.speed
            self.direction = RIGHT
            self.is_moving = True
        else:
            self.is_moving = False

        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def animate(self):
        if self.is_moving:
            if self.direction != self.last_direction:
                self.frame_index = 0

            frames = self.walking_frame_sets[self.direction]
            self.image = frames[self.frame_index]

            # UPDATE animation frame
            self.frame_index += 1
            if self.frame_index >= len(frames):
                self.frame_index = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
