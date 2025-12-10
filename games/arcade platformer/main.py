""""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""

import arcade

# constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"
WINDOW_COLOR = arcade.csscolor.CORNFLOWER_BLUE


# the window where everything shows up on
class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # call parent class to set up window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # set BG color
        self.background_color = WINDOW_COLOR

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen"""

        # clear screen (ALWAYS PUT FIRST)
        self.clear()

        # code to draw other things will go here

def main():
    """Main function, makes sure that the game doesn't execute if importing this file from another file"""

    window = GameView()
    window.setup()
    arcade.run()

# run the code
if __name__ == "__main__":
    main()