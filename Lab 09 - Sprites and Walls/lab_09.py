"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        for y in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1664, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1600
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1600
            self.wall_list.append(wall)

        for y in range(128, 960, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 192
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(1024, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 192
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(640, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 384
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 576, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 384
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 320, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 576
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(384, 704, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 576
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(768, 1152, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 576
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(1216, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 576
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(128, 1482, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 768
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 960
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(1024, 1554, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 960
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 256, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1152
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(320, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1152
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 128, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1344
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(192, 1472, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1344
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(1536, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 1344
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        arcade.set_background_color(arcade.csscolor.BLUE)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
