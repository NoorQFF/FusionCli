import curses

class CustomShell:
    def __init__(self):
        self.stdscr = None

    def __enter__(self):
        self.stdscr = curses.initscr()
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        curses.endwin()
        pass

def customInput(prompt: str, default: str) -> str:
    # Initialize curses and colors
    stdscr = curses.initscr()
    curses.curs_set(1)  # Show cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal text
    curses.init_pair(2, 0, curses.COLOR_BLACK)  # Grey (depends on terminal)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Grey (depends on terminal)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    input_text = list(default)
    pos = len(default)
    typing_started = False

    while True:
        stdscr.clear()

        question_mark = " \u003F "

        stdscr.addstr(0, 0, question_mark, curses.color_pair(3))
        stdscr.addstr(0, len(question_mark), prompt, curses.color_pair(1))
        stdscr.addstr(0, len(prompt) + 3, " \u00BB ", curses.color_pair(2))  # Grey prefill

        if not typing_started:
            stdscr.addstr(0, len(prompt) + 6, "".join(input_text), curses.color_pair(2))  # Grey prefill
        else:
            stdscr.addstr(0, len(prompt) + 6, "".join(input_text), curses.color_pair(4))  # Fresh input

        stdscr.move(0, len(prompt) + 6 + pos)  # Move cursor to the right position
        stdscr.refresh()


        key = stdscr.getch()

        if key in (10, 13):  # Enter key
            break
        elif key in (127, 8):  # Backspace key
            if typing_started and pos > 0:
                pos -= 1
                input_text.pop(pos)

                if len(input_text) == 0:
                    input_text = list(default)
                    pos = len(default)
                    typing_started = False 
        elif key == curses.KEY_LEFT:  # Move cursor left
            if pos > 0:
                pos -= 1
        elif key == curses.KEY_RIGHT:  # Move cursor right
            if pos < len(input_text):
                pos += 1
        elif 32 <= key <= 126:  # Printable characters
            if not typing_started:
                input_text = []
                pos -= len(default)
                typing_started = True

            input_text.insert(pos, chr(key))  
            pos += 1  


    curses.endwin()

    return "".join(input_text)

