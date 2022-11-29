
import youtube_dl
from requests import get
import asyncio
import re
import subprocess
import os


def run(arg):
    if is_url(arg):
        video_info = youtube_dl.YoutubeDL().extract_info(arg, download=False)
    else:
        video_info = youtube_dl.YoutubeDL().extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
    filename = video_info['title']
    filename = re.sub(r'[^A-Za-z0-9 ]+', '', filename)
    filename = f"{filename}.mp3"

    print(f'filename1: {filename}')
    options={

        'format':'worstaudio',
        'keepvideo':False,
        'outtmpl':filename,
        'ext':'mp3',
        'audio-format' : 'mp3'
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f'filename {filename}')
    print("Download complete... {}".format(filename))

    return filename
def get_mp3():
    video_url = "https://www.youtube.com/watch?v=UEA8A0mR4aY"
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}"
    options={
        'format' : 'bestaudio/best',
        'keepvideo' : False,
        'outtmpl' : filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', }]
    }
    mp3 = filename+'.mp3'

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
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

def test(s):
    ydl_opts = {"audio-format":"mp3"}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download(s)
async def main():
    #wait test(["youtube.com/watch?v=d1VH7ygA2kw"])
    get_mp3()
    #run("we don't talk about bruno")
if __name__ == '__main__':

    asyncio.run(main())

