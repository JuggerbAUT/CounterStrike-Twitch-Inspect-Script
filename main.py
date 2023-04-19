import re
from twitchio.ext import commands

# Read auth data from auth.txt file
oauth_token = ""
channel_name = ""

with open("auth.txt") as f:
    f = f.readlines()
    oauth_token = f[0].replace("\n", "").replace(" ", "")
    channel_name = f[1].replace("\n", "").replace(" ", "")

# Bot class
class Bot(commands.Bot):

    # Initialize bot
    def __init__(self):
        self.msg_queue = []
        super().__init__(token=oauth_token, prefix='!', initial_channels=[channel_name])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        check = re.search("(\\+*csgo_econ_action_preview)(([0-9]*)([A-Z]*))*", message.content)
        if check:
          with open("skins.txt", "a") as skins:
            skins.write(message.content)
            skins.write("\n")



bot = Bot()
bot.run()