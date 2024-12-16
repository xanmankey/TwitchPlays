from src.TwitchPlays_KeyCodes import *
import pydirectinput


NUM_COMMANDS = 11


# NOTE: in order to use this, you do need to map the keys to dolphin
# NOTE: this only works on Windows machines
def handle_message(
    msg, team_num
):  # do not rename this function. it has to be "handle_message"
    # Now that you have a chat message, this is where you add your game logic.
    # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
    # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
    # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
    # Use the pydirectinput library to press or move the mouse

    if msg == "left":
        HoldAndReleaseKey(Q + MODIFIER[team_num], 2)

    if msg == "right":
        HoldAndReleaseKey(W + MODIFIER[team_num], 2)

    if msg == "up":
        HoldAndReleaseKey(E + MODIFIER[team_num], 2)

    if msg == "down":
        HoldAndReleaseKey(R + MODIFIER[team_num], 2)

    if msg == "a":
        HoldAndReleaseKey(T + MODIFIER[team_num], 0.1)

    if msg == "b":
        HoldAndReleaseKey(Y + MODIFIER[team_num], 0.1)

    if msg == "x":
        HoldAndReleaseKey(U + MODIFIER[team_num], 0.1)

    if msg == "y":
        HoldAndReleaseKey(I + MODIFIER[team_num], 0.1)

    if msg == "start":
        HoldAndReleaseKey(O + MODIFIER[team_num], 0.1)

    if msg == "l":
        HoldAndReleaseKey(P + MODIFIER[team_num], 0.1)

    if msg == "r":
        HoldAndReleaseKey(A + MODIFIER[team_num], 0.1)
