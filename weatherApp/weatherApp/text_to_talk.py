# text_to_talk.py
#    - A script to read text out loud.
#      This will open an windows mp3 player
#      to play the script and close the player
# 
# Requirements:
#   OS: Windows
#   pip install gtts

from gtts import gTTS
import os
import time
import subprocess
import colorama

mp3 = '.\media\\text_to_talk.mp3'
redFont = '\033[2;31;47m'
resetfont = ' \033[0;0m'
program = 'text_to_talk.py '
  
def save_script(str):
    try:
        tts = gTTS(text=str, lang='en', slow=False)
        tts.save(mp3)
    except Exception:
        print(redFont + program,
                + 'Failed to save ' + mp3,
                + resetfont)
        exit()
    return mp3

def remove_mp3():
    try:
        time.sleep(3)
        os.remove(mp3)
    except Exception:
        print(redFont + program,
                + 'Failed to delete ' + mp3,
                + resetfont)

def close_player(pid):
    try:
         subprocess.call('TASKKILL /F /IM  wmplayer.exe /T >nul', shell=True)
    except Exception:
        print (redFont + program,
                + 'Failed to close Windows Media Player, ', 
                + 'process id: ' + pid,
                + resetfont)

def play():
    try:
        pid = subprocess.Popen(mp3, shell=True).pid
        time.sleep(8)
    except Exception:
        print(redFont + program,
            + 'Failed to play ' + mp3,
            + resetfont )
        exit()

# Entry point
def speak(str):
    print("Reading out loud:")
    save_script(str)
    pid = play()
    close_player(pid)
    remove_mp3()