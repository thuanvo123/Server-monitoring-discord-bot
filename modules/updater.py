from os import system as run
from os import remove, open


def main():
    open("Update", "w")
    run('git pull > update.lg')
    with open('update.lg', 'r') as f:
        c = f.read(-1).split('\n')
    remove('update.lg')
    if len(c) > 2:
        return True
    else:
        return False

if __name__=='__main__':
    main()