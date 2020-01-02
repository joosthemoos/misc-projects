"""
Stanford CS106AP Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, and Nick Bowman.

This program takes in breakoutgraphics.py and accesses it, and runs through the move_ball and handle_collisions
functions in a loop in order to check for collisions per movement. This goes until num_lives runs out (hit the bottom
3 times) or the brick_count is zero (the screen is cleared).
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    FRAME_RATE = 1000 / 120  # 120 frames per second.
    while graphics.num_lives != 0 and graphics.brick_count != 0:
        if graphics.running:
            graphics.move_ball()
            graphics.handle_collisions()
        pause(FRAME_RATE)
    graphics.game_over()





if __name__ == '__main__':
    main()
