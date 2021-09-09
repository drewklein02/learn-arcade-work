import arcade

# Open a window. Name Of Window
arcade.open_window(600, 600, "Lab 2 Picture")
# Sets Color of window
arcade.set_background_color(arcade.csscolor.TAN)
# Get ready to draw

arcade.start_render()
# Bands Of watch and Arm
arcade.draw_rectangle_filled(295, 475, 200, 300, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(295, 0, 200, 300, arcade.csscolor.WHITE)

# Outer edge of watch
arcade.draw_circle_filled(300, 300, 200, arcade.csscolor.BLACK)

# Inner Screen Of watch
arcade.draw_circle_filled(300, 300, 185, arcade.csscolor.LIGHT_GRAY)
arcade.draw_circle_filled(300, 300, 175, arcade.csscolor.GRAY)

# Drawing Battery symbol
arcade.draw_rectangle_filled(350, 400, 100, 40, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(350, 400, 90, 30, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(410, 400, 10, 30, arcade.csscolor.WHITE)

# Putting In Date and Time
arcade.draw_text("Thursday 9",
                 175, 400,
                 arcade.csscolor.BLACK, 15)
arcade.draw_text("2:25",
                 200, 290,
                 arcade.csscolor.BLACK, 80)
arcade.draw_text("20",
                 410, 300,
                 arcade.csscolor.BLACK, 30)

# Drawing 3 circles at the bottom

arcade.draw_circle_outline(200, 240, 40, arcade.csscolor.BLUE, 4)
arcade.draw_circle_outline(300, 170, 40, arcade.csscolor.WHITE, 4)
arcade.draw_circle_outline(400, 240, 40, arcade.csscolor.BLUE, 4)

# Labels In Circles
arcade.draw_text("Steps",
                 185, 250,
                 arcade.csscolor.BLACK, 8)
arcade.draw_text("Distance",
                 280, 180,
                 arcade.csscolor.BLACK, 8)
arcade.draw_text("Heart Rate",
                 376, 250,
                 arcade.csscolor.BLACK, 8)

# Numbers in Circles
arcade.draw_text("1518",
                 170, 220,
                 arcade.csscolor.BLACK, 20)
arcade.draw_text("17.6",
                 270, 150,
                 arcade.csscolor.BLACK, 20)
arcade.draw_text("79",
                 385, 220,
                 arcade.csscolor.BLACK, 20)

arcade.finish_render()
arcade.run()
