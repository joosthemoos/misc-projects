from campy.graphics.gwindow import GWindow
from panel import Panel

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700

class Story():
    def __init__(self):
        self.window = GWindow(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.panel = Panel(self.window)

    def start_story(self):
        print('Testing your panel!')
        self.panel.view_panel()


def main():
    cs106ap_story = Story()
    cs106ap_story.start_story()


if __name__ == '__main__':
    main()
