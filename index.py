import requests

from discord import app_commands, Intents, Client, Interaction

__version__ = "1.0.1"


def check_me(token_test: str) -> dict:
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token_test}"
    })

    return r.json()


print("\n".join([
    "Hey, welcome to the active developer badge bot.",
    "Please enter your bot's token below to continue.",
    "",
    "Don't close this application after entering the token. You may close it after the bot has been invited and the command has been ran."
]))


while True:
    token = input("> ")
    data = check_me(token)

    if data.get("id", None):
        break

    print("\nSeems like you entered an invalid token. Try again.")


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    print("\n".join([
        f"Logged in as {client.user} (ID: {client.user.id})",
        "",
        f"Use this URL to invite {client.user} to your server:",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"
    ]))


@client.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something """
    print(f"> {interaction.user} used the command.")
    await interaction.response.send_message(
        f"Hi **{interaction.user}**, thank you for saying hello to me.\n\n__**Where's my badge?**__\nEligibility for the badge is checked by Discord in intervals, at this moment in time, 24 hours is the recommended time to wait before trying.\n\n__**It's been 24 hours, now how do I get the badge?**__\nIf it's already been 24 hours, you can head to https://discord.com/developers/active-developer and fill out the 'form' there.\n\n__**Active Developer Badge Updates**__\nUpdates regarding the Active Developer badge can be found in the Discord Developers server -> discord.gg/discord-developers - in the #active-developer-badge channel."
    )


client.run(token)
