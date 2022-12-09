# Importing libraries
import os

import discord
import youtube_dl
import asyncio
from requests import get
import re
import pprint
import sys




help_message = """!play url/search joins current voice channel and plays song
!download url/search - generates a link to download mp3 from
!pause
!resume
!stop
!help
"""

download_message = """Preparing mp3 file. This may take up to a minute"""


def run_discord_bot():
    # Discord bot Initialization
    TOKEN = sys.argv[1]
    client = discord.Client(intents=discord.Intents.all())
    voice_clients = {}
    yt_dl_opts = {
        'format': 'bestaudio/best',
    }
    ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
    ffmpeg_options = {'options': "-vn"} # exclude video

    def is_url(url):
        if url.startswith('https') or url.startswith('www'):
            pass
        else:
            url = f'https://' + url
        try:
            get(url)
            return True
        except:
            return False

    def download_mp3(arg):
        if is_url(arg):
            video_info = youtube_dl.YoutubeDL().extract_info(arg, download=False)
        else:
            video_info = youtube_dl.YoutubeDL().extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        filename = video_info['title']
        filename = re.sub(r'[^A-Za-z0-9 ]+', '', filename)
        filename = f"{filename}.mp3"

        with youtube_dl.YoutubeDL(yt_dl_opts) as ydl:
            ydl.download([video_info['webpage_url']])
        return filename


    async def play_song(msg, url):
        voice_client = await msg.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
        loop = asyncio.get_event_loop()
        if is_url(url):
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            song = data['url']
            title = data['title']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C://ffmpeg//ffmpeg.exe")

            voice_client.play(player)
        else:
            printer = pprint.PrettyPrinter()

            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(f"ytsearch:{url}", download=False))
            data = data['entries'][0]
            song = data['url']
            printer.pprint(data)
            title = data['title']

            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C://ffmpeg//ffmpeg.exe")

            voice_client.play(player)
        return data,title
    @client.event
    async def on_ready():
        print(f"Bot logged in as {client.user}")

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        if msg.content.startswith("!play"):  # command to play music given a url
            try:
                url = msg.content[6:]
                data,title = await play_song(msg, url)
                await msg.channel.send(f"Now playing {title}")
            except Exception as err:
                print(f'error: {err}')
        if msg.content.startswith("!pause"):
            try:
                voice_clients[msg.guild.id].pause()
            except Exception as err:
                print(f'error: {err}')

        # This resumes the current song playing if it's been paused
        if msg.content.startswith("!resume"):
            try:
                voice_clients[msg.guild.id].resume()
            except Exception as err:
                print(f'error: {err}')

        # This stops the current playing song
        if msg.content.startswith("!stop"):
            try:
                voice_clients[msg.guild.id].stop()
                await voice_clients[msg.guild.id].disconnect()
            except Exception as err:
                print(err)

        if msg.content.startswith("!download"):  # download the video
            url = msg.content.split()[1]
            await msg.channel.send(download_message)
            filepath = download_mp3(msg.content[10:])
            await msg.channel.send(file=discord.File(filepath))
            os.remove(filepath)
        if msg.content.startswith('!help'):
            await msg.channel.send(help_message)
        if msg.content.startswith('!'):
            await msg.delete()

    client.run(TOKEN)