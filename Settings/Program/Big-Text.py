from pyfiglet import Figlet
import datetime
from colorama import Fore, Style, init
from Config.Util import *
from Config.Config import *

# تهيئة colorama
init()

# قائمة بأنماط ASCII art المتاحة
styles = [
    'standard',  # النمط الأساسي
    'slant',     # نمط مائل
    'big',       # نمط كبير
    'block',     # نمط كتل
    'starwars',  # نمط مستوحى من Star Wars
    'bulbhead'   # نمط رأس المصباح
]

def current_time():
    return datetime.datetime.now().strftime("[%H:%M:%S]")

def generate_ascii_art(text, font):
    figlet = Figlet(font=font)
    ascii_art = figlet.renderText(text)
    return ascii_art

def display_styles():
    print(f"{current_time()} | Available styles:")
    for idx, style in enumerate(styles, start=1):
        print(f"{idx}. {style}")

def main():
    print("ASCII Art Generator")
    
    message = input(f"{current_time()} {color.RED}{INPUT}Enter the text you want to convert to ASCII art: {color.RESET}")
    
    display_styles()
    
    try:
        choice = int(input(f"{current_time()} {color.RED}{INPUT}Choose a style number: {color.RESET}"))
        if choice < 1 or choice > len(styles):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(f"{current_time()} Error: {e}")
        return
    
    selected_style = styles[choice - 1]
    ascii_art = generate_ascii_art(message, selected_style)
    
    print(f"\n{current_time()} ASCII Art in style '{selected_style}':")
    print(ascii_art)
    
    # إبقاء الشاشة مفتوحة حتى يضغط المستخدم على مفتاح
    input(f"\n{current_time()} Press Enter to exit...")

if __name__ == "__main__":
    main()
