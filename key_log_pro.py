#modules to use for this application
import pynput

from pynput.keyboard import key, listener

count = 0
keys= []

def on_press(key):
#function to keep track of key pressed
    

def on_release(key):
    #function to know when key has been released
    
    
with listener(on_press = on_press, on_release) as listener
