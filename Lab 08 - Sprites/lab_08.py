""" Sprite Sample Program """
import arcade
import random
bomb_sound = arcade.load_sound("bombsound.wav")
money_sound = arcade.load_sound("moneysound.wav")

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
ENEMY_SCALE = .1
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = .8
BULLET_SPEED = 10
COIN_COUNT = 50
ENEMY_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Enemy(arcade.Sprite):
    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

class Coin(arcade.Sprite):
    def reset(self):
        def update(self):
            self.center_y -= 1

        if self.top <= 0:
            self.bottom = SCREEN_HEIGHT

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None
        self.enemy_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMETHYST)

        self.bullet_list = None
        self.money_sound = arcade.load_sound("moneysound.wav")
        self.bomb_sound = arcade.load_sound("bombsound.wav")

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("hero.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(ENEMY_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            bad = Enemy("bomb3.png", SPRITE_SCALING_COIN)

            # Position the coin
            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center_y = random.randrange(100, SCREEN_HEIGHT)
            bad.change_x = random.randrange(-3, 4)
            bad.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.enemy_list.append(bad)

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("money.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        self.enemy_list.draw()


        output = "Score " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):

        self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.money_sound)
        self.enemy_list.update()
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in enemy_hit_list:
            enemy.remove_from_sprite_lists()
            self.score -= 5
            arcade.play_sound(self.bomb_sound)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
