import discord
import responses
import download


# Send messages
async def send_message(message, user_message, is_private):
    print(user_message)
    try:
        response = responses.handle_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    #zqLTrD6BI8FfEvKZ0WDPkP_5fEf5eh1G
    #MTAyMDAxOTg0MTAwMTg0ODk2Mg.G6qeCH.TG1Oz_Mg3VMc4V-3L6SqWLsqQH-2iu6_QLfMbw
    TOKEN =     'MTAyMDAxOTg0MTAwMTg0ODk2Mg.G1Tad1.iP3GrufelhNoCEt4mxt0ZaG64Bv6aa5jN-ESaA'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        #await message.channel.send('recieved message')
        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' in {channel}")
        
        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        if user_message[1] == '!':
            user_message = user_message[1:]
            message.content = 'youtube.link'
            await send_message(message, user_message, is_private='False')
        else:
            await send_message(message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.login(TOKEN)
    client.run(TOKEN)