import pygame as pg
import sys, os
# --- Snake & Food Classes
from sprites import *
#---- Global constants ---
from settings import *


"""
TODO:
= Game:
- Make Like The Google Snake Game
-
"""


class Game:
    def __init__(self):
        # Initiliaze pygame & set the window title
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mixer.init()
        
        # Load Sound Resources
        self.hit_self_sound = pg.mixer.Sound(HIT_SELF_SOUND)
        self.hit_food_sound = pg.mixer.Sound(HIT_FOOD_SOUND)
        self.hit_food_sound.set_volume(0.1)
        self.hit_self_sound.set_volume(0.25)
        
        # Create the window surface object
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.background_image = pg.image.load(BG_IMAGE_PATH).convert()
        
        # Create our objects & set the beginning of game data
        self.running = True
        self.load_high_score()
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        
    def load_high_score(self):
        """ Gets the current High Score from high_score.tx or sets the High Score to 0. """
        # Default High Score
        self.high_score = 0
        # Gets the current working directory
        self.dir = os.path.dirname(__file__)
        
        # Try to read the high score text file
        try:
            high_score_file = open(os.path.join(self.dir, HS_FILE), 'r')
            self.high_score = int(high_score_file.read())
            high_score_file.close()
            print(f"The High Score is: {self.high_score}")
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
    
    
    def save_high_score(self):
        """ Update the High Score file if the current score beats the old high score."""
        
        print(f"Your Score: {self.score} | High Score: {self.high_score}")
        
        if self.score > self.high_score:
            self.high_score = self.score
            print("You beat the high score!")
            try:
                # Write the file to the disk
                high_score_file = open(os.path.join(self.dir, HS_FILE), 'w')
                high_score_file.write(str(self.high_score))
                high_score_file.close()
                print("High Score Saved")
            except IOError:
                # Hm, can't write it
                print("Unable to save the high score.")
            
        else:
            print("Better luck next time")
    
    
    def new(self):
        """ Start a new game. """
        self.score = 0
        # Create the Snake & Food Objects
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        # Run the game loop
        self.run()
    
    
    def run(self):
        """ Game Loop """
        self.playing = True
        while self.playing:
            self.clock.tick(FPS_SPEED)
            self.process_events()
            self.run_logic_update()
            self.display_frame()

    
    def process_events(self):
        """ Process all of the events. Return a "True" if we need to close the window. """
        for event in pg.event.get():
            # Checks if player has exited out of window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            # Checks if the player has hit any keys
            elif event.type == pg.KEYDOWN: 
                # Update the Snake's Direction based off user's key inputs
                self.snake.change_direction(event.key)
    
    
    def run_logic_update(self):
        """ Updates positions & checks for collisions. Ran each frame. """ 
        # Update the Snake & food
        self.snake.update()
        self.food.update()

        # Check if snake and food have collided
        if self.snake.cells[0] == self.food.cell:
            #print("Snake and Food have collided.")
            self.hit_food_sound.play()
            self.food.respawn(self.snake.cells)
            self.snake.maxCells += 1
            self.score += 10
                
        # Check if Snake has collided with itself
        for block in self.snake.cells[1:]:
            if block == self.snake.cells[0]:
                self.hit_self_sound.play()
                pg.time.delay(250)
                self.playing = False
                
    
    
    def display_frame(self):
        """ Draws & displays everything to the screen for the game. """
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.background_image, (0, 0))
        self.snake.draw()
        self.food.draw()
        pg.display.update()
    
    
    def wait_for_key(self):
        """ Checks for input while at the Splash/GameOver screens. """
        waiting = True
        while waiting:
            self.clock.tick(FPS_SPEED)
            for event in pg.event.get():
                # Checks if player has exited out of window
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                # Checks if player hit a key | exits the current screen
                if event.type == pg.KEYDOWN:
                    waiting = False
    
    
    def show_start_screen(self):
        """ Displays the SPLASH SCREEN when program is first ran. """
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.background_image, (0, 0))
        self.draw_text(TITLE, 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Arrows or WASD to move", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pg.display.update()
        self.wait_for_key()
    
    
    def show_go_screen(self):
        """ Displays the GAME OVER SCREEN when player has died. """
        if not self.running:
            return
        
        # Update the high score file
        self.save_high_score()
        
        # Draw the Game Over Screen
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press any key to play again", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pg.display.update()
        self.wait_for_key()
     
    
    def draw_text(self, text, size, color, x, y):
        """ Draws any text to the screen. """
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



if __name__ == '__main__':
    # Create a Game Object
    game = Game()
    
    # Display the SPLASH SCREEN when program is first ran
    game.show_start_screen()
    
    # Loop through new games & the GAME OVER screen until player exits window
    while game.running:
        game.new()
        game.show_go_screen()

    # End Pygame
    pg.quit()
    # Exist Script
    sys.exit()