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
  
def save_script(str):
    try:
        os.remove('current_weather.mp3')
    except:
        print("webscraping_weather.py: line 59, File current_weather.mp3 not found")
    tts = gTTS(text=str, lang='en', slow=False)
    tts.save("current_weather.mp3")
    return "current_weather.mp3"

def play(mp3):
    try:
        PID = subprocess.Popen(mp3, shell=True).pid
        time.sleep(8)
        taskKillExitCode = subprocess.call('TASKKILL /F /IM  wmplayer.exe /T >nul', shell=True)
    except Exception:
        print ("text_to_talk.py Failed to close Windows Media Player," 
            + " process id: " + PID)

def speak(str):
    mp3 = save_script(str)
    play(mp3)

    