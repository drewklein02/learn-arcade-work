"""
Testing how to draw stuff.
"""
import arcade
# Open a window.
arcade.open_window(600, 600, "Drawing example")
# Sets Color of window
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#Get ready to draw
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,600,300,0, arcade.csscolor.GREEN)

arcade.draw_rectangle_filled(100,320,20,60, arcade.csscolor.BROWN)
arcade.draw_circle_filled(100,350,30,arcade.csscolor.DARK_GREEN)
arcade.draw_ellipse_filled(300,500,200,100,arcade.csscolor.WHITE)
arcade.draw_arc_outline(100,500,350,200,arcade.csscolor.RED,0,180)
arcade.draw_triangle_filled(400,400,370,320,430,420,arcade.csscolor.BROWN)
arcade.draw_polygon_filled(((500, 400),
                           (470,320),
                           (530,320),
                           (520,360),
                           ),arcade.csscolor.BLUE)
arcade.draw_line(200,500,15,20,arcade.csscolor.RED)
arcade.draw_text("How to make a baseball field",
                 150,300,
                 arcade.csscolor.BLACK)
#Finish program
arcade.finish_render()
arcade.run()