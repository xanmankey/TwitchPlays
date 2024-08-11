from src.TwitchPlays_KeyCodes import *

commands = ["left", "right", "up", "down", "long left", "long right", "long up", "long down", "cleft", "cright", "cup", "cdown", "long cleft", "long cright", "long cup", "long cdown", "a", "b", "x", "y", "z", "l", "r"]

def handle_message(msg, team_modifier):  # do not rename this function. it has to be "handle_message"
    # Now that you have a chat message, this is where you add your game logic.
    # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
    # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
    # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
    # Use the pydirectinput library to press or move the mouse
    keys = team_modifier
    if msg == "left":
        keys.append(A)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "right":
        keys.append(D)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "up":
        keys.append(W)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "down":
        keys.append(S)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "light left":
        keys.append(A)
        HoldAndReleaseKey(keys, 0.3)
        return

    if msg == "light right":
        keys.append(D)
        HoldAndReleaseKey(keys, 0.3)
        return

    if msg == "light up":
        keys.append(W)
        HoldAndReleaseKey(keys, 0.3)
        return

    if msg == "light down":
        keys.append(S)
        HoldAndReleaseKey(keys, 0.3)
        return
    
    if msg == "long left":
        keys.append(A)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long right":
        keys.append(D)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long up":
        keys.append(W)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long down":
        keys.append(S)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "cleft":
        keys.append(GC_LEFT)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "cright":
        keys.append(GC_RIGHT)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "cup":
        keys.append(GC_UP)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "cdown":
        keys.append(GC_DOWN)
        HoldAndReleaseKey(keys, 1)
        return

    if msg == "long cleft":
        keys.append(GC_LEFT)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long cright":
        keys.append(GC_RIGHT)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long cup":
        keys.append(GC_UP)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "long cdown":
        keys.append(GC_DOWN)
        HoldAndReleaseKey(keys, 3)
        return

    if msg == "a":
        keys.append(GC_A)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "b":
        keys.append(GC_B)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "x":
        keys.append(GC_X)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "y":
        keys.append(GC_Y)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "z":
        keys.append(GC_Z)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "l":
        keys.append(GC_L)
        HoldAndReleaseKey(keys, 0.2)
        return

    if msg == "r":
        keys.append(GC_R)
        HoldAndReleaseKey(keys, 0.2)
        return
