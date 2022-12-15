from requests import get as rget
from discord import app_commands, Intents, Client, Interaction

print("""\
Hey, welcome to the active developer badge bot.
Please enter your bot's token below to continue.

Don't close this application after entering the token.
You may close it after the bot has been invited and the command has been ran.""")


# loop until valid token is entered
while True:
    token = input("> ")

    # Make a request to the Discord api to check token validity 
    r = rget("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    # If the token is correct, continue the code
    if r.json().get("id", None):
        break

    # If the token is incorrect, user will be asked to enter their token again
    print("\nSeems like you entered an invalid token. Try again.")


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)


# Variable to store the bot class and interact with it
# Since we only run one slash command we don't require any intents
client = FunnyBadge(intents=Intents.none())

@client.event
async def on_ready():
    """ This is called when the bot is ready and has a connection with Discord
        It also prints out the bot's invite URL that automatically uses your
        Client ID to make sure you invite the correct bot with correct scopes.
    """
    print(f"""\
Logged in as {client.user} (ID: {client.user.id})

Use this URL to invite {client.user} to your server:
https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot""")


@client.tree.command()
async def givemebadge(interaction: Interaction):
    """ Sends a basic message on how to obtain badge """

    # Log to console that the command has been ran
    print(f"> {interaction.user} used the command.")

    # Then responds in the channel with this message
    await interaction.response.send_message(f"""\
Hi **{interaction.user}**, thank you for saying hello to me.

__**Where's my badge?**__
Eligibility for the badge is checked by Discord in intervals
at this moment in time, 24 hours is the recommended time to wait before trying.

__**It's been 24 hours, now how do I get the badge?**__
If it's already been 24 hours, you can head to
https://discord.com/developers/active-developer and fill out the 'form' there.

__**Active Developer Badge Updates**__
Updates regarding the Active Developer badge can be found in the
Discord Developers server -> discord.gg/discord-developers - in the #active-dev-badge channel.""")

client.run(token)  # Execute the bot