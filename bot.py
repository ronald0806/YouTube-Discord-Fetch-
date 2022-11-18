# Importing libraries
import discord
import youtube_dl
import asyncio
import youtube
import os

help_message = """!play {url} 
!download {url}
!search {search_terms} (in progress)
!pause
!resume
!stop
!help
"""

def run_discord_bot():
    # Discord bot Initialization
    TOKEN ='MTAyMDAxOTg0MTAwMTg0ODk2Mg.GVIemQ.3JJGQ-TWaTJkdrbwQ3K8nqnsnBt8ZAuq8IWWTM'
    client = discord.Client(intents=discord.Intents.all())
    voice_clients = {}
    yt_dl_opts = {
        'format': 'bestaudio/best',
    }
    ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
    ffmpeg_options = {'options': "-vn"} # exclude video

    async def play_song(msg, url):
        voice_client = await msg.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C://ffmpeg//ffmpeg.exe")

        voice_client.play(player)
    @client.event
    async def on_ready():
        print(f"Bot logged in as {client.user}")



    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        if msg.content.startswith("!play"):  # command to play music given a url
            try:
                url = msg.content.split()[1]
                await play_song(msg,url)
            except Exception as err:
                print(err)
        if msg.content.startswith("!search"): # search query
            await msg.channel.send('in progress...')

        if msg.content.startswith("!pause"):
            try:
                voice_clients[msg.guild.id].pause()
            except Exception as err:
                print(err)

        # This resumes the current song playing if it's been paused
        if msg.content.startswith("!resume"):
            try:
                voice_clients[msg.guild.id].resume()
            except Exception as err:
                print(err)

        # This stops the current playing song
        if msg.content.startswith("!stop"):
            try:
                voice_clients[msg.guild.id].stop()
                await voice_clients[msg.guild.id].disconnect()
            except Exception as err:
                print(err)
        if msg.content.startswith("!download"):  # download the video
            url = msg.content.split()[1]
            filepath = youtube.download_mp3(url)
            await msg.channel.send(file=discord.File(filepath))
            os.remove(filepath)
        if msg.content.startswith('!help'):
            await msg.channel.send(help_message)
        if msg.content.startswith('!'):
            await msg.delete()



    client.login(TOKEN)
    client.run(TOKEN)