from __future__ import unicode_literals
from re import X
import youtube_dl

my_file = open("playlist.txt", "r")
data = my_file.read()
data = data.split("\n")

print("Playlist URLs: ", data)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for url in data:
        ydl.download([url])