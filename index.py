import requests
import json
import inspect

from discord import app_commands, Intents, Client, Interaction

# This will print the information in console
# inspect.cleandoc() is used to remove the indentation from the message
# while using triple quotes so that it looks nice in the code
# Normally some developers don't use it and move the text all the way back to the left
# However I personally prefer clean code
print(inspect.cleandoc("""
    Hey, welcome to the active developer badge bot.
    Please enter your bot's token below to continue.

    Don't close this application after entering the token
    You may close it after the bot has been invited and the command has been ran
"""))


try:
    with open("./config.json", "r", encoding="utf8") as f:
        config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # You can in theory also do "except Exception", but it is not recommended
    config = {}


while True:
    # While loop starts and used Python.input() to get the token
    token = config.get("token", None)
    if token:
        print("\n--- Detected token in config.json saved from previous run, using that. ---\n")
    else:
        token = input("> ")

    # Then validates if the token you provided was correct or not
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    # If the token is correct, it will continue the code
    data = r.json()
    if data.get("id", None):
        break  # Breaks the while loop

    # If the token is incorrect, it will print the error message
    # and ask you to enter the token again (while Loop)
    print("\nSeems like you entered an invalid token. Try again by entering the correct token.")
    # Resets the config so that it doesn't use the previous token again
    config = {}

# This is used to save the token for the next time you run the bot
with open("./config.json", "w", encoding="utf8") as f:
    # Making sure that 'token' key exists in the config.json file
    config["token"] = token
    # This dumps our working setting to the config.json file
    # Indent is used to make the file look nice and clean
    # If you don't want to indent, you can remove the indent=2 from code
    json.dump(config, f, indent=2)


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)


# Variable to store the bot class and interact with it
# Since this is a simple bot to run 1 command over slash commands
# We then do not need any intents to listen to events
client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    """ This is called when the bot is ready and has a connection with Discord
        It also prints out the bot's invite URL that automatically uses your
        Client ID to make sure you invite the correct bot with correct scopes.
    """
    print(inspect.cleandoc(f"""
        Logged in as {client.user} (ID: {client.user.id})

        Use this URL to invite {client.user} to your server:
        https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot
    """))


@client.tree.command()
async def hello(interaction: Interaction):
    # Responds in the console that the command has been ran
    print(f"> {interaction.user} used the command.")

    # Then responds in the channel with this message
    await interaction.response.send_message(inspect.cleandoc(f"""
        Hi **{interaction.user}**, thank you for saying hello to me.

        __**Where's my badge?**__
        Eligibility for the badge is checked by Discord in intervals,
        at this moment in time, 24 hours is the recommended time to wait before trying.

        __**It's been 24 hours, now how do I get the badge?**__
        If it's already been 24 hours, you can head to
        https://discord.com/developers/active-developer and fill out the 'form' there.

        __**Active Developer Badge Updates**__
        Updates regarding the Active Developer badge can be found in the
        Discord Developers server -> https://discord.gg/discord-developers - in the #active-dev-badge channel.
    """))


# Runs the bot with the token you provided
client.run(token)
