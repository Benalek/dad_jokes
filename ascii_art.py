import termcolor
import colorama
import pyfiglet
colorama.init()

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")


def print_art(msg, color):

    if color not in valid_colors:
        color = "red"
    ascii_art = pyfiglet.figlet_format(msg)
    ascii_color = termcolor.colored(ascii_art, color=color)
    print(ascii_color)


if __name__ == "__main__":

    msg = input("What would you like to print? ")
    color = input("What color? ")
    print_art(msg, color)
