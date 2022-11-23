
import youtube_dl
from requests import get
import asyncio


illegal_chars = [
'!'
,'@'
,'#'
,'$'
,'%'
,'^'
,'&'
,'*'
,'('
,')'
,'"'
,'+'
,'<'
,'>'
,','
,'.'
,'?'
,';'
,':'
,"'"
,'{'
,'['
,']'
,'}'
,'-'
,'='
]
async def run(arg):
    if is_url(arg):
        video_info = youtube_dl.YoutubeDL().extract_info(f"{arg}", download=False)['entries'][0]
    else:
        video_info = youtube_dl.YoutubeDL().extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
    filename = video_info['title']
    filename = replace_chars(filename)
    filename = f"{filename}.mp3"

    print(f'filename1: {filename}')
    options={

        'format':'worstaudio',
        'keepvideo':False,
        'outtmpl':filename,
        'ext':'mp3'
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f'filename {filename}')
    print("Download complete... {}".format(filename))

    return filename
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

def replace_chars(arg):
    for i in illegal_chars:
        arg = arg.replace(i, '')
    return arg

async def main():
    await run("we don't talk about bruno")
if __name__=='__main__':

    asyncio.run(main())

