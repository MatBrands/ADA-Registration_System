import os
import platform

def clear() -> None:
    so = platform.system()
    if so == 'Windows':
        os.system('cls')
    else:
        os.system('clear')