import pygame
from random import choice
#--- Global constants ---
from settings import *



# ====== SNAKE CLASS ===========
class Snake:
    """ Represents the Snake that the player controls. """
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        
        # Snake's Starting position | keeps track of the heads cordinates
        self.x = 3
        self.y = 7
        # Snakes starting velocity & direction
        self.dx = 1
        self.dy = 0
        # Max lenght of Snake.  How many body parts it can have
        self.maxCells = 3
        # List of all the cells the snake's body is currently in
        self.cells = [(self.x, self.y), (self.x -1, self.y), (self.x -2, self.y)]
        # List of all the cells current direction | corresponds the self.cells
        self.velocity_cells = [(1, 0), (1, 0), (1, 0)]
        
        # Load all of the sprite images
        self.load_sprite_images()
    
    def load_sprite_images(self):
        """ Loads all of the snake sprites for all of its different body parts. """
        # Snake Head sprites
        self.head_up_image = pygame.image.load(HEAD_UP).convert_alpha()
        self.head_down_image = pygame.image.load(HEAD_DOWN).convert_alpha()
        self.head_right_image = pygame.image.load(HEAD_RIGHT).convert_alpha()
        self.head_left_image = pygame.image.load(HEAD_LEFT).convert_alpha()
        
        # Snake tail sprites
        self.tail_image_up = pygame.image.load(TAIL_UP).convert_alpha()
        self.tail_image_down = pygame.image.load(TAIL_DOWN).convert_alpha()
        self.tail_image_right = pygame.image.load(TAIL_RIGHT).convert_alpha()
        self.tail_image_left = pygame.image.load(TAIL_LEFT).convert_alpha()
        
        # Snake body sprites
        self.body_image_vertical = pygame.image.load(BODY_VERTICAL).convert_alpha()
        self.body_image_horizontal = pygame.image.load(BODY_HORIZONTAL).convert_alpha()
        
        # Loading the turning body segments 
        self.turn_down_left_image = pygame.image.load(TURN_DOWN_LEFT).convert_alpha()
        self.turn_down_right_image = pygame.image.load(TURN_DOWN_RIGHT).convert_alpha()
        self.turn_up_left_image = pygame.image.load(TURN_UP_LEFT).convert_alpha()
        self.turn_up_right_image = pygame.image.load(TURN_UP_RIGHT).convert_alpha()

    def change_direction(self, key_pressed):
        """ Takes a keyboard input and updates the snakes direction acordingly. """
        # Move Up - W or Up arrow key
        if (key_pressed == pygame.K_UP or key_pressed == pygame.K_w) and self.dy != 1:
            self.dx = 0
            self.dy = -1
        # Move Down - S or Down arrow key
        if (key_pressed == pygame.K_DOWN or key_pressed == pygame.K_s) and self.dy != -1:
            self.dx = 0
            self.dy = 1
        # Move Left - A or Left arrow key
        if (key_pressed == pygame.K_LEFT or key_pressed == pygame.K_a) and self.dx != 1:
            self.dx = -1
            self.dy = 0
        # Move Right - D or Right arrow key
        if (key_pressed == pygame.K_RIGHT or key_pressed == pygame.K_d) and self.dx != -1:
            self.dx = 1
            self.dy = 0

    def update(self):
        """ Updates the position of the snake each frame. """
        # Updates the snake's x cordinate
        self.x += self.dx
        if self.x > (GRID_WIDTH-1): self.x = 0
        elif self.x < 0: self.x = (GRID_WIDTH-1)
        # Updates the snake's y cordinate
        self.y += self.dy
        if self.y > (GRID_HEIGHT-1): self.y = 0
        elif self.y < 0: self.y = (GRID_HEIGHT-1)
        # Keeps tracks of all the cells that the snake's body occupys
        self.cells = [(self.x, self.y)] + self.cells
        self.velocity_cells = [(self.dx, self.dy)] + self.velocity_cells
        # Removes items from cells & cell_dir if it goes over the maxCell amount
        if len(self.cells) > self.maxCells: self.cells.pop()
        if len(self.velocity_cells) > self.maxCells: self.velocity_cells.pop()
    
    
    def draw(self):
        """ Draws rect objects every where the snake's head and body currently occupy. """
        # Update the head image
        self.update_head_graphic()
        # Update the tail image
        self.update_tail_graphic()
        
        # Draw each part of the snake's body
        for index, cur_cell in enumerate(self.cells):
            x_cor = (cur_cell[0] * CELL_SIZE)
            y_cor = (cur_cell[1] * CELL_SIZE)
            
            # Draw the head
            if index == 0:
                self.parent_screen.blit(self.head, (x_cor, y_cor))
            
            # Draw the tail
            elif index == (len(self.cells) - 1):
                self.parent_screen.blit(self.tail, (x_cor, y_cor))
            
            # Draw the body parts
            else:
                ahead_block  = self.cells[index - 1]
                behind_block = self.cells[index + 1]
                
                # Draw the horizontal body segments
                if ahead_block[1] == behind_block[1]:
                    self.parent_screen.blit(self.body_image_horizontal, (x_cor, y_cor))
                # Draw the vertical body segments
                elif ahead_block[0] == behind_block[0]:
                    self.parent_screen.blit(self.body_image_vertical, (x_cor, y_cor))

                # Draw the turning body parts
                else:
                    previous_block_dx = self.cells[index + 1][0] - cur_cell[0]
                    previous_block_dy = self.cells[index + 1][1] - cur_cell[1]
                    next_block_dx = self.cells[index - 1][0] - cur_cell[0]
                    next_block_dy = self.cells[index - 1][1] - cur_cell[1]
                    
                    if previous_block_dx == 16: previous_block_dx = -1
                    if next_block_dx == 16: next_block_dx = -1
                    if previous_block_dy == 14: previous_block_dy = -1
                    if next_block_dy == 14: next_block_dy = -1
                    
                    if previous_block_dx == -16: previous_block_dx = 1
                    if next_block_dx == -16: next_block_dx = 1
                    if previous_block_dy == -14: previous_block_dy = 1
                    if next_block_dy == -14: next_block_dy = 1
                    
                    # draw === turn_up_left_image
                    if previous_block_dx == -1 and next_block_dy == -1 or next_block_dx == -1 and previous_block_dy == -1:
                        self.parent_screen.blit(self.turn_up_left_image, (x_cor, y_cor))
                    
                    # draw === turn_up_right_image
                    elif previous_block_dx == 1 and next_block_dy == -1 or next_block_dx == 1 and previous_block_dy == -1:
                        self.parent_screen.blit(self.turn_up_right_image, (x_cor, y_cor))
                
                    # draw === turn_down_left_image
                    elif previous_block_dx == -1 and next_block_dy == 1 or next_block_dx == -1 and previous_block_dy == 1:
                        self.parent_screen.blit(self.turn_down_left_image, (x_cor, y_cor))
                    
                    # draw === turn_down_right_image
                    elif previous_block_dx == 1 and next_block_dy == 1 or next_block_dx == 1 and previous_block_dy == 1:
                        self.parent_screen.blit(self.turn_down_right_image, (x_cor, y_cor))
                    
    
    
    def update_head_graphic(self):
        """ Updates the snake's head graphic so it matches with the direction it's going."""
        if self.dx == 1: self.head = self.head_right_image
        elif self.dx == -1: self.head = self.head_left_image
        elif self.dy == 1: self.head = self.head_down_image
        elif self.dy == -1: self.head = self.head_up_image
    
    def update_tail_graphic(self):
        """ Updates the snake's tail graphic so it matches with the direction it's going."""
        tail_velocity = self.velocity_cells[-2]
        if tail_velocity == ( 1, 0): self.tail = self.tail_image_right
        elif tail_velocity == (-1, 0): self.tail = self.tail_image_left
        elif tail_velocity == (0,  1): self.tail = self.tail_image_down
        elif tail_velocity == (0, -1): self.tail = self.tail_image_up



# ====== FOOD CLASS ============
class Food:
    """ Represents the food that the snake eats to grow. """
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(FOOD_IMAGE_PATH).convert_alpha()
        # Set the Food's starting position
        self.x = 15
        self.y = 7
        self.cell = (self.x, self.y)
        
    def respawn(self, occupied_cells):
        """ Finds a spot on the board that is not occupied to spawn on. """
        # TODO Prevent spawning anywhere close to head of snake
        
        looking_for_spawn = True
        while looking_for_spawn:
            # Select a random x and y value
            x_cor = choice([i for i in range(GRID_WIDTH)])
            y_cor = choice([j for j in range(GRID_HEIGHT)])
            # Check if it is already taken.  Loop if it is and break loop if it isn't
            if (x_cor, y_cor) not in occupied_cells:
                looking_for_spawn = False
                break
        
        # Set new x y cordinates
        self.x = x_cor
        self.y = y_cor
        self.cell = (self.x, self.y)
    
    
    def update(self):
        """ Updates the food sprite. It doesn't move right now. In future maybe animate it."""
        return
    
    def draw(self):
        """ Draws the rect representing the food onto the screen. """
        self.parent_screen.blit(self.image, (CELL_SIZE * self.x, CELL_SIZE * self.y))

