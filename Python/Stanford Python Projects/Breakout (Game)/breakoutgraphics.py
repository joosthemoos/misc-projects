"""
Stanford CS106AP Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, and Nick Bowman.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Color names to cycle through for brick rows.
COLORS = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE']

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 3.5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        num_bricks = 100
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2, y = window_height - \
                            paddle_offset)

        # initializing the paddle
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # initializing the ball
        self.ball = GOval(width=ball_radius*2, height=ball_radius * 2, x=window_width/2 - BALL_RADIUS, y = window_height/2 - BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # initial velocity
        self.vx = 0
        self.vy = INITIAL_Y_SPEED

        # draw bricks
        self.draw_bricks()

        # number of lives left
        self.num_lives = 3

        # running? big question mark
        self.running = False

        # brick count
        self.brick_count = 100

        # mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.move_paddle)

    def start(self, event):
        """
        Starts game on mouse click.
        """
        self.running = True

    def draw_bricks(self):
        """
        Draws bricks by row and with color changing for each turn.
        """
        x_init = 0
        curr_y = BRICK_OFFSET
        color_index = 0
        for row in range(1, BRICK_ROWS+1):
            curr_x = x_init
            for col in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=curr_x, y=curr_y)
                self.brick.filled = True
                self.brick.fill_color = COLORS[color_index]
                self.window.add(self.brick)
                curr_x += BRICK_WIDTH + BRICK_SPACING
            curr_y += BRICK_HEIGHT + BRICK_SPACING
            if row % 2 == 0:
                color_index += 1

    def move_paddle(self, event):
        """
        Moves paddle with mouse event.
        """
        self.paddle.x = event.x - PADDLE_WIDTH/2

    def move_ball(self):
        """
        Moves ball with proper x and y velocities.
        """
        self.ball.move(self.vx, self.vy)

    def handle_collisions(self):
        """
        Handles collisions as necessary per animation loop.
        """
        # changing for wall collisions
        if self.side_wall_hit():  # checks for side wall hits and changes x-component
            print('oop hit a side wall')
            self.vx = -self.vx
        elif self.top_wall_paddle_hit():  # checks for top/paddle hits and changes y-component
            print('oop hit the top or a paddle')
            self.vy = -self.vy
        # changing for block collisions
        elif self.brick_paddle_hit() != -1 and self.ball.y != self.window.height - 2*BALL_RADIUS - PADDLE_OFFSET - PADDLE_HEIGHT:
            loc_x, loc_y = self.brick_paddle_hit()
            print(loc_x, loc_y)
            self.remove_brick(loc_x, loc_y)
            self.vy = -self.vy
            self.vx = random.uniform(-MAX_X_SPEED, MAX_X_SPEED)
        # changing for bottom collision
        elif self.bottom_hit():
            self.num_lives -= 1
            print('the number of lives is', self.num_lives)
            self.reset()

    def bottom_hit(self):
        """
        Checks if the bottom was hit.
        """
        if self.ball.y + 2*BALL_RADIUS >= self.window.height:
            return True
        else:
            return False

    def side_wall_hit(self):
        """
        Checks if the left or right walls were hit.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - 2*BALL_RADIUS:
            return True
        else:
            return False

    def top_wall_paddle_hit(self):
        """
        Checks if the top wall or paddle was hit.
        """
        if self.ball.y <= 0:
            return True
        elif self.brick_paddle_hit() != -1 and self.ball.y >= self.window.height - 2*BALL_RADIUS - PADDLE_OFFSET:
            return True
        else:
            return False

    def brick_paddle_hit(self):
        """
        Checks, according to the guidelines in the handout, if a collision has occurred with the ball and a brick or
        the paddle.
        """
        if self.window.get_object_at(self.ball.x, self.ball.y) != None:
            return self.ball.x, self.ball.y
        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y) != None:
            return self.ball.x+2, self.ball.y
        elif self.window.get_object_at(self.ball.x, self.ball.y + 2*BALL_RADIUS) != None:
            return self.ball.x, self.ball.y + 2*BALL_RADIUS
        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + 2*BALL_RADIUS) != None:
            return self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS
        else:
            return -1

    def remove_brick(self, loc_x, loc_y):
        """
        Remove a brick when hit.
        """
        if self.window.get_object_at(loc_x, loc_y) != self.paddle:
            self.window.remove(self.window.get_object_at(loc_x, loc_y))
            self.brick_count -= 1

    def reset(self):
        """
        Resets the game when the bottom is hit.
        """
        self.window.clear()
        self.window.remove(self.ball)

        self.ball = GOval(width=BALL_RADIUS * 2, height=BALL_RADIUS * 2, x=self.window.width / 2 - BALL_RADIUS,
                          y=self.window.height / 2 - BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        self.draw_bricks()
        self.brick_count = 100
        self.vx = 0
        self.vy = INITIAL_Y_SPEED
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        self.running = False

    def game_over(self):
        game_over_label = GLabel('GAME OVER', x=self.window.width/2 - 40, y=self.window.height/2)
        self.window.add(game_over_label)