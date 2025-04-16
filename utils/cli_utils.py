try:
    import curses
except ImportError:
    import windows_curses as curses


class CustomShell:
    def __init__(self):
        self.stdscr = None
        self.current_line = 0

    def customInput(self, prompt: str, default: str) -> str:
        curses.curs_set(1)  # Show cursor
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal text
        curses.init_pair(2, 0, curses.COLOR_BLACK)  # Grey (depends on terminal)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Cyan prefix
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)  # User input

        input_text = list(default)
        pos = len(default)
        typing_started = False

        line = self.current_line

        while True:
            self.stdscr.move(line, 0)
            self.stdscr.clrtoeol()

            question_mark = " \u003F "
            prefill_arrow = " \u00BB "

            self.stdscr.addstr(line, 0, question_mark, curses.color_pair(3))
            self.stdscr.addstr(line, len(question_mark), prompt, curses.color_pair(1))
            self.stdscr.addstr(line, len(prompt) + 3, prefill_arrow, curses.color_pair(2))

            if not typing_started:
                self.stdscr.addstr(line, len(prompt) + 6, "".join(input_text), curses.color_pair(2))  # Grey prefill
            else:
                self.stdscr.addstr(line, len(prompt) + 6, "".join(input_text), curses.color_pair(4))  # Fresh input

            self.stdscr.move(line, len(prompt) + 6 + pos)  # Move cursor
            self.stdscr.refresh()

            key = self.stdscr.getch()

            if key in (10, 13):  # Enter
                break
            elif key in (127, 8):  # Backspace
                if typing_started and pos > 0:
                    pos -= 1
                    input_text.pop(pos)
                    if len(input_text) == 0:
                        input_text = list(default)
                        pos = len(default)
                        typing_started = False
            elif key == curses.KEY_LEFT:
                if pos > 0:
                    pos -= 1
            elif key == curses.KEY_RIGHT:
                if pos < len(input_text):
                    pos += 1
            elif 32 <= key <= 126:  # Printable characters
                if not typing_started:
                    input_text = []
                    pos = 0
                    typing_started = True
                input_text.insert(pos, chr(key))
                pos += 1

        self.current_line += 1  # Move to next line for future inputs
        return "".join(input_text)

    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
