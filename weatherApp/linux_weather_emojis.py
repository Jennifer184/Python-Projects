# linux_weather_emojis.py
# - A script for weather emojis

def fire():
    return "\U0001F525 " 

def thermometer():
    return "\U0001F321 "

def snowflake():
    return "\u2744 "

def happySun():
    return "\U0001F31E "

def match_weather_emoji(temp):
    if temp <= 55:
        emoji = snowflake()
    elif temp <= 82:
        emoji = happySun()
    else:
        emoji = fire()
    return emoji