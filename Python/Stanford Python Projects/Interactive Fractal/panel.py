"""
JESSICA KULESHOV'S ULTIMATE CREATION: INTERACTIVE JULIA SET FRACTAL PATTERN

Basically, how this works is that there is a sliding bar at the bottom that you can move from left to right in order to
increase the progression of a Julia set fractal, which is a famous fractal pattern that is defined by the behavior of a
function that operates on input of complex numbers. The resulting outputs either tend towards infinity or are bounded.

Much credit for the algorithm goes to GeeksForGeeks.org's algorithm for the Julia set, found here:
https://www.geeksforgeeks.org/julia-fractal-python/
This was done in bitmap, so I changed it for it to work with campy/GImage restrictions. It also is not interactive, so
I accordingly modified it.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause

BALL_RADIUS = 20
WINDOW_DIM = 700
BAR_OFFSET = 60
BAR_WIDTH = 20
num_seconds = 20
FRAME_RATE = 60


class Panel:
    def __init__(self, window_object):
        self.window = window_object

        # initialize bar
        self.slide_bar = GRect(WINDOW_DIM - 2*BAR_OFFSET, BAR_WIDTH, x=BAR_OFFSET, y=WINDOW_DIM - BAR_OFFSET)
        self.slide_bar.filled = True
        self.slide_bar.fill_color = 'darksage'
        self.window.add(self.slide_bar)

        # initialize orb
        self.slider_orb = GOval(BALL_RADIUS*2, BALL_RADIUS*2, x=WINDOW_DIM - 2*BAR_OFFSET, y=WINDOW_DIM - BAR_OFFSET - BALL_RADIUS/2)
        self.slider_orb.filled = True
        self.slider_orb.fill_color = 'mediumturquoise'
        self.window.add(self.slider_orb)

        # initialize blank fractal
        self.fractal = GImage.from_file('white_600_400.png')

        # initialize description label
        self.description_1 = GLabel("Click to start animation.", 40, 40)
        self.description_1.x = self.window.width / 2 - self.description_1.\
            width / 2
        self.description_1.y = self.window.height - 2*self.description_1.\
            height + 5
        self.window.add(self.description_1)

        self.description_2 = GLabel("Move the slider in order to see the progression of the Julia set fractal pattern.",
                                    40, 40)
        self.description_2.x = self.window.width/2 - self.description_2.width/2
        self.description_2.y = self.window.height - self.description_2.height + 5
        self.window.add(self.description_2)

        # initialize title
        self.title = GImage.from_file('title.PNG')
        self.title.x = (self.window.width - self.title.width)/2
        self.title.y = 10
        self.window.add(self.title)

        # initialize slider ratio (to measure progression)
        self.slider_ratio = 0

        # add mouse listeners
        onmouseclicked(self.start_sequence)
        onmousemoved(self.zoom_fractal)

        # initialize run statement
        self.running = False

    def start_sequence(self, event):
        """
        Starts the animation on click.
        """
        self.running = True

    def view_panel(self):
        """
        Views the panel when called.
        """
        while True:
            for i in range(int(num_seconds*FRAME_RATE/10)):
                if self.running:
                    self.fractal_change()
                pause(10000 / FRAME_RATE)
            break
        self.running = False

    def zoom_fractal(self, event):
        """
        Determines the ratio of the slider's location along the bar to the length of the bar, in order to determine the
        progress of the fractal generation.
        """
        location = 0
        if self.running:
            if event.x >= WINDOW_DIM - BAR_OFFSET:
                location = WINDOW_DIM - BAR_OFFSET - BALL_RADIUS
            elif event.x < BAR_OFFSET:
                location = BAR_OFFSET - BALL_RADIUS
            else:
                location = event.x - BALL_RADIUS
            self.slider_orb.x = location
            self.slider_ratio = (location - BAR_OFFSET + BALL_RADIUS)/\
                (WINDOW_DIM - 2*BAR_OFFSET)

    def fractal_change(self):
        """
        Displays an image corresponding to the progression of the fractal based on the ratio of the slider to the bar,
        increasing in ratio increments of 0.05.
        """
        self.window.remove(self.fractal)
        dim = int(self.slider_ratio * 20)*5
        if dim == 0:
            self.fractal = GImage.from_file('Fractal_Prog/frac_5.PNG')
        else:
            filename = 'Fractal_Prog/frac_'+str(dim)+'.PNG'
            self.fractal = GImage.from_file(filename)
        self.fractal.x = self.window.width/2 - self.fractal.width/2
        self.fractal.y = self.window.height/2 - self.fractal.height/2
        self.window.add(self.fractal)

    # NOT USED FOR ACTUAL ANIMATION BUT FOR CALCULATION PURPOSES
    def progress_fractal(self):
        """
        Because of the fact that this process takes too long for the animation, I have decided to go ahead and not
        use it, but I left it here so that you understand where the code for the fractal came from and how it
        progresses. The basis of this code was originally written in Bitmap format, but I modified it to work with
        GImage. Original algorithm code is cited at the top of the program.
        """
        w, h, zoom = int(600*self.slider_ratio), int(400*self.slider_ratio), 1

        cX, cY = -0.7, .27015
        moveX, moveY = 0.0, 0.0
        maxIter = 255

        for x in range(w):
            for y in range(h):
                zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
                zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
                i = maxIter
                while zx * zx + zy * zy < 4 and i > 1:
                    tmp = zx * zx - zy * zy + cX
                    zy, zx = 2.0 * zx * zy + cY, tmp
                    i -= 1

                # convert byte to RGB (3 bytes), kinda
                # magic to get nice colors
                #pix[x, y] = (i << 21) + (i << 10) + i * 8 #change this to fit campy language
                temp_pix = self.fractal.get_pixel(x, y)
                temp_pix.red = 200*i
                temp_pix.green = 100
                temp_pix.blue = 200
                self.fractal.set_pixel(x, y, temp_pix)
