from src.TwitchPlays_KeyCodes import *
import pydirectinput


def handle_message(msg):  # do not rename this function. it has to be "handle_message"
    # Now that you have a chat message, this is where you add your game logic.
    # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
    # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
    # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
    # Use the pydirectinput library to press or move the mouse

    if msg == "left":
        HoldAndReleaseKey(A, 2)

    if msg == "right":
        HoldAndReleaseKey(D, 2)

    if msg == "up":
        HoldAndReleaseKey(W, 2)

    if msg == "down":
        HoldAndReleaseKey(S, 2)

    if msg == "a":
        HoldAndReleaseKey(GC_A, 0.1)

    if msg == "b":
        HoldAndReleaseKey(GC_B, 0.1)

    if msg == "x":
        HoldAndReleaseKey(GC_X, 0.1)

    if msg == "y":
        HoldAndReleaseKey(GC_Y, 0.1)

    if msg == "start":
        HoldAndReleaseKey(GC_START, 0.1)

    if msg == "l":
        HoldAndReleaseKey(GC_L, 0.1)

    if msg == "r":
        HoldAndReleaseKey(GC_R, 0.1)
