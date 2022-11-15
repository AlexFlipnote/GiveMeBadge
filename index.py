import requests

from discord import app_commands, Intents, Client, Interaction

print("\n".join([
    "Hey, welcome to the active developer badge bot.",
    "Please enter your bot's token below to continue.",
    "",
    "Don't close this application after entering the token. "
    "You may close it after the bot has been invited and the command has been ran."
]))


while True:
    token = input("> ")

    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    data = r.json()
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


async def _init_command_response(interaction: Interaction):
    print(f"> {interaction.user} used the command.")
    await interaction.response.send_message("\n".join([
        f"Hi **{interaction.user}**, thank you for saying hello to me.",
        "",
        "__**Where's my badge?**__",
        "Eligibility for the badge is checked by Discord in intervals, "
        "at this moment in time, 24 hours is the recommended time to wait before trying.",
        "",
        "__**It's been 24 hours, now how do I get the badge?**__",
        "If it's already been 24 hours, you can head to "
        "https://discord.com/developers/active-developer and fill out the 'form' there.",
        "",
        "__**Active Developer Badge Updates**__",
        "Updates regarding the Active Developer badge can be found in the "
        "Discord Developers server -> discord.gg/discord-developers - in the #active-dev-badge channel.",
    ]))


@client.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something """
    await _init_command_response(interaction)


@client.tree.command()
async def givemebadge(interaction: Interaction):
    """ Says hello or something, but with a different name """
    await _init_command_response(interaction)


client.run(token)
