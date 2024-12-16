import concurrent.futures
import keyboard
import pyautogui
import time
from src.TwitchPlays_Connection import Twitch, YouTube
from src.TwitchPlays_KeyCodes import *
from dotenv import load_dotenv
import os

load_dotenv()

TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")

TEAMS = ["8N", "7S", "2S", "2N"]

PLAYERS = {}


class TwitchPlays:
    last_time = time.time()
    message_queue = []
    teams = []

    active_tasks = []
    connection = None

    def __init__(
        self,
        streaming_on_twitch,
        twitch_channel,
        youtube_channel_id,
        youtube_stream_url,
        game_file_name,
        message_rate,
        max_queue_length,
        max_workers,
        startup_time,
    ):

        self.message_rate = message_rate
        self.max_queue_length = max_queue_length
        self.max_workers = max_workers
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers)

        try:
            name = "games." + game_file_name
            self.game = __import__(name, fromlist=[""])
        except ModuleNotFoundError as e:
            print("ERROR! Missing game file: " + str(e))
            return

        pyautogui.FAILSAFE = False

        # Count down before starting, so you have time to tab into the game
        countdown = startup_time

        while countdown > 0:
            print(countdown)
            countdown -= 1
            time.sleep(1)

        if streaming_on_twitch:
            self.connection = Twitch()
            self.connection.twitch_connect(twitch_channel.lower())
        else:
            self.connection = YouTube()
            self.connection.youtube_connect(youtube_channel_id, youtube_stream_url)

    def start(self):
        while True:
            self.active_tasks = [t for t in self.active_tasks if not t.done()]

            # Check for new messages
            new_messages = self.connection.twitch_receive_messages()

            if new_messages:
                # New messages are added to the back of the queue
                self.message_queue += new_messages
                # Shorten the queue to only the most recent X messages
                self.message_queue = self.message_queue[-self.max_queue_length :]

            # Get messages to handle by message rate
            messages_to_handle = []

            if not self.message_queue:
                # No messages in the queue
                self.last_time = time.time()
            else:
                # Determine how many messages we should handle now
                rate = (
                    1
                    if self.message_rate == 0
                    else (time.time() - self.last_time) / self.message_rate
                )
                amount = int(rate * len(self.message_queue))

                if amount > 0:
                    # Pop the messages we want off the front of the queue
                    messages_to_handle = self.message_queue[0:amount]
                    del self.message_queue[0:amount]
                    self.last_time = time.time()

            # If user presses Shift+Backspace, automatically end the program
            if keyboard.is_pressed("shift+backspace"):
                exit()

            if not messages_to_handle:
                continue
            else:
                for message in messages_to_handle:
                    if len(self.active_tasks) <= self.max_workers:
                        self.active_tasks.append(
                            self.thread_pool.submit(self.handle_message, message)
                        )
                    else:
                        print(
                            "WARNING: active tasks ({0}) exceeds number of workers ({1}). ({2} messages in the queue)".format(
                                len(self.active_tasks),
                                self.max_workers,
                                len(self.message_queue),
                            )
                        )

    def handle_message(self, message):
        try:
            msg = message["message"].lower()
            username = message["username"].lower()
            team = self.teams.get(username)

            # custom user commands
            if msg == "!help":
                message = f"To join a team, type !join [{', '.join(TEAMS)}] (your team name). Once you've joined you can type any of the following commands: {', '.join(self.game.commands)}"
                self.connection.sock.send(
                    f"PRIVMSG #{TWITCH_CHANNEL} :{message}\r\n".encode("utf-8")
                )
                # self.connection.twitch_send_message(
                #     "Use commands like !up, !down, !left, !right, !a, !b, !x, !y, !start, !l, !r to play the game and prove that your floor is the best!"
                # )
                return

            if msg.startswith("!join"):
                team = msg.split(" ")[1].upper()
                if team in TEAMS:
                    message = "{0} joined team {1}".format(username, team)
                    self.connection.sock.send(
                        f"PRIVMSG #{TWITCH_CHANNEL} :{message}\r\n".encode("utf-8")
                    )
                    self.teams[username] = TEAMS.index(team)
                    return
                else:
                    message = "Invalid team. Please choose from {0}".format(TEAMS)
                    self.connection.sock.send(
                        f"PRIVMSG #{TWITCH_CHANNEL} :{message}\r\n".encode("utf-8")
                    )
                    return

            print("Got this message from {0}: {1}".format(username, msg))

            if team != None:
                self.game.handle_message(msg, team)

        except Exception as e:
            print("Encountered exception: " + str(e))
