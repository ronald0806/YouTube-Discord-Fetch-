# importing packages
from pytube import YouTube
import os
def download_mp3(url):
    yt = YouTube(url)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    destination = './videos'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

if __name__ == '__main__':
    download_mp3('https://www.youtube.com/watch?v=vrvs-Hy69oo')
