import readline
import code
import rlcompleter
import os
import sys
import dice
import re

def get_tty_size():
    rows, columns = os.popen("stty size", "r").read().split()
    rows = int(rows)
    columns = int(columns)
    return rows, columns

def get_splitter_line():
    rows, columns = get_tty_size()
    txt = ""
    a = 0
    while(len(txt) < columns):
        if(a % 2 == 0):
            txt += "="
        else:
            txt += "-"
        a += 1
    return txt

class RPGCalc():
    def __init__(self):
        self.start()

    def start(self):
        self.print_banner()
        continue_running = True
        while(continue_running):
            continue_running = self.get_input()

    def get_input(self):
        cmd = input("> ")
        m_roll = re.match(r"r(?:oll)?[ ](.+)", cmd)
        if(m_roll):
            roll, kwargs = dice.roll(m_roll.group(1), raw=True, return_kwargs=True)
            result = roll.evaluate_cached(**kwargs)
            txt = m_roll.group(1)
            txt += ": " + str(sum(result))
            print(txt)
        elif(cmd == "exit"):
            return False
        elif cmd:
            try:
                print(eval(cmd))
            except:
                print("Error occured!")
        return True
    
    def print_banner(self):
        txt = "Python RPG Calculator\n\n"
        txt += "A Python REPL with some added commands.\n"
        txt += get_splitter_line() + "\n\n"
        print(txt)


RPGCalc()
