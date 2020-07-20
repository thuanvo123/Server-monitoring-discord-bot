import subprocess
from platform import system
from os import system as run
from os import path, remove
from sys import argv
from time import sleep

interpreter = 'python' if system() == 'Windows' else 'python3'

def main():
    """
    Main loop that handdles starting the server, and deciding what to do after an update.
    """
    server = subprocess.Popen([interpreter, 'bot_core.py'])  #Creates a child process with the 'server.py' script
    while server.poll() is None:    #Works while the child process runs
        try:
            if path.exists('Restart'):  #When the server requires a restart changing it's runmode between developper and normal mode
                remove('Restart')
                server.kill()
                while server.poll() is None:
                    pass
                print(f"Restarting...")
                server = subprocess.Popen([interpreter, 'bot_core.py'])
        except:
            pass
        finally:
            sleep(0.2)

if __name__ == '__main__':
    #Starts the server, while required
    while True:
        main()
        print('Bot killed!')
        ansv = str(input('Do you want to restart the bot? ([Y]/N) ') or 'Y')
        if ansv.upper() == 'N':
            break