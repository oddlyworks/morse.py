"""Produces either printed or audio morse code for an input string."""
import time
try:
    from playsound import playsound
except ImportError:
    playsound = None

DELAY = 0.5  # delay time in seconds
MORSECODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    ' ': ' ',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }

def translate(in_string) -> str:
    """Returns translation of in_string in '.' and '-' format."""
    string = list(in_string)
    morse_string = ''
    for char in string:
        try:
            morse_string += MORSECODE[char.lower()] + ' '
        except KeyError:
            print(f'Key {char} Not Found')
    return morse_string

def sound(in_string) -> None:
    """Produces audio of translated in_string."""
    if playsound is None:
        print("Module 'playsound' is not installed.")
        return
    morse_string = translate(in_string)
    for char in morse_string:
        if char == '.':
            playsound('dot.mp3')
        elif char == '-':
            playsound('dash.mp3')
        elif char == ' ':
            time.sleep(DELAY)

if __name__ == "__main__":
    in_string = input('What do you want to dot-dash? -->')
    print(translate(in_string))
    sound(in_string)