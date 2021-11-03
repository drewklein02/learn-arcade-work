""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
MOUSE_CLICK_SOUND = arcade.load_sound("arcade_resources_sounds_error2.wav")
WALL_HIT_SOUND = arcade.load_sound("arcade_resources_sounds_error4.wav")
MOUSE_CLICK_SOUND2 = arcade.load_sound("arcade_resources_sounds_gameover3.wav")


def draw_watch():
    arcade.set_background_color(arcade.color.TAN)
    arcade.draw_rectangle_filled(295, 475, 200, 300, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(295, 0, 200, 300, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300, 300, 200, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(300, 300, 185, arcade.csscolor.LIGHT_GRAY)
    arcade.draw_circle_filled(300, 300, 175, arcade.csscolor.GRAY)


def draw_battery():
    arcade.draw_rectangle_filled(350, 400, 100, 40, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(350, 400, 90, 30, arcade.csscolor.GREEN)
    arcade.draw_rectangle_filled(410, 400, 10, 30, arcade.csscolor.WHITE)


def draw_steps():
    arcade.draw_circle_outline(200, 240, 40, arcade.csscolor.BLUE, 4)
    arcade.draw_text("Steps",
                     185, 250,
                     arcade.csscolor.BLACK, 8)
    arcade.draw_text("1518",
                     170, 220,
                     arcade.csscolor.BLACK, 20)


def draw_distance():
    arcade.draw_circle_outline(300, 170, 40, arcade.csscolor.WHITE, 4)
    arcade.draw_text("Distance",
                     280, 180,
                     arcade.csscolor.BLACK, 8)
    arcade.draw_text("17.6",
                     270, 150,
                     arcade.csscolor.BLACK, 20)


def draw_heart_rate():
    arcade.draw_circle_outline(400, 240, 40, arcade.csscolor.BLUE, 4)
    arcade.draw_text("Heart Rate",
                     376, 250,
                     arcade.csscolor.BLACK, 8)
    arcade.draw_text("79",
                     385, 220,
                     arcade.csscolor.BLACK, 20)


def draw_date_time():
    arcade.draw_text("Thursday 9",
                     175, 400,
                     arcade.csscolor.BLACK, 15)
    arcade.draw_text("2:25",
                     200, 290,
                     arcade.csscolor.BLACK, 80)
    arcade.draw_text("20",
                     410, 300,
                     arcade.csscolor.BLACK, 30)


def draw_freckle(x, y):
    arcade.draw_circle_filled(100 + x - 90, 100 + y - 110, 4, arcade.csscolor.BROWN, num_segments=32)
    arcade.draw_circle_filled(90 + x - 90, 115 + y - 110, 5, arcade.csscolor.BROWN, num_segments=32)
    arcade.draw_circle_filled(65 + x - 90, 110 + y - 110, 8, arcade.csscolor.BROWN, num_segments=32)


def draw_hair(x, y):
    arcade.draw_rectangle_filled(100 + x - 100, 100 + y - 100, 25, 3, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(110 + x - 100, 110 + y - 100, 20, 3, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(120 + x - 100, 90 + y - 100, 30, 3, arcade.csscolor.BLACK)


class I_love_running:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw_love(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, 10,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)
        arcade.draw_circle_filled(15 + self.position_x, 20 + self.position_y, 20,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)
        arcade.draw_circle_filled(self.position_x - 15, self.position_y - 25, 15,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 30:
            arcade.play_sound(WALL_HIT_SOUND)
            self.position_x = 30

        if self.position_x > SCREEN_WIDTH -35:
            arcade.play_sound(WALL_HIT_SOUND)
            self.position_x = SCREEN_WIDTH - 35

        if self.position_y < 40:
            arcade.play_sound(WALL_HIT_SOUND)
            self.position_y = 40

        if self.position_y > SCREEN_HEIGHT - 40:
            arcade.play_sound(WALL_HIT_SOUND)
            self.position_y = SCREEN_HEIGHT - 40


class Sweat:
    def __init__(self, position_x, position_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_ellipse_filled(100 + self.position_x - 100, 100 + self.position_y - 100, 10, 35,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)
        arcade.draw_ellipse_filled(115 + self.position_x - 100, 120 + self.position_y - 100, 20, 27,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)
        arcade.draw_ellipse_filled(85 + self.position_x - 100, 75 + self.position_y - 100, 15, 30,
                                   arcade.csscolor.SKY_BLUE, num_segments=32)


class MyGame(arcade.Window):
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.sweat.position_x = x
        self.sweat.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(MOUSE_CLICK_SOUND)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(MOUSE_CLICK_SOUND2)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.sweat2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.sweat2.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.sweat2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.sweat2.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sweat2.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.sweat2.change_y = 0

    def update(self, delta_time):
        self.sweat2.update()

    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.sweat = Sweat(50, 50, 15, arcade.color.BLACK)
        self.sweat2 = I_love_running(50, 50, 0, 0, 10, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.sweat.draw()
        self.sweat2.draw_love()

        draw_watch()
        draw_date_time()
        draw_battery()
        draw_steps()
        draw_distance()
        draw_heart_rate()
        draw_freckle(500, 50)
        draw_freckle(100, 450)
        draw_freckle(500, 450)
        draw_hair(500, 550)
        draw_hair(40, 350)
        draw_hair(60, 80)
        draw_hair(500, 100)


def main():
    MyGame()
    arcade.run()


main()