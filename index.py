import requests

from discord import app_commands, Intents, Client, Interaction


def check_me(token_test: str) -> dict:
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token_test}"
    })

    return r.json()


print("\n".join([
    "Hey, welcome to the active developer badge bot.",
    "Please enter your token below to continue."
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
        f"Hi **{interaction.user}**, thank you for saying hello to me."
    )


client.run(token)
