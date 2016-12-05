"""
Simple discord bot to say goodbye
"""

import discord
import random

client = discord.Client()


# credentials for discordclient
login = ''
passw = ''


farewells = [
    'bye',
    'farewell',
    'ciao',
]


@client.event
async def on_message(message: discord.Message):
    """
    on_message parse message and respond
    """
    print('{}: {}'.format(message.author, message.content))
    if message.content.startswith('66'):
        await client.send_message(message.channel, 'bye-bye')
    elif message.content.startswith('!stat_farewell'):
        await client.send_message(message.channel, 'Farewells:\n{}'.format('\n'.join(word for word in farewells)))
    elif message.content.startswith('!add_farewell'):
        _, _, new_farewell = message.content.partition(' ')
        farewells.append(new_farewell)
        await client.send_message(message.channel, 'Farewell added!\n{}'.format(new_farewell))
    elif message.content.startswith('!del_farewell'):
        _, _, del_farewell = message.content.partition(' ')
        farewells.remove(del_farewell)
        await client.send_message(message.channel, 'Farewell deleted!\n{}'.format(del_farewell))
    elif message.content.startswith('!help_farewell'):
        await client.send_message(message.channel, '!stat_farewell, !add_farewell, !del_farewell')


@client.event
async def on_voice_state_update(before: discord.Member, after: discord.Member):
    """
    on_voice_state_update say goodbye to people leaving voice_channel
    """
    if before.voice_channel is not None and after.voice_channel is None:
        await client.send_message(before.server.default_channel,
                                  ' '.join([random.choice(farewells), after.display_name]))


client.run(login, passw)
