# youtube-to-mp3

This very simple piece of code uses the youtube_dl library to take youtube links as inputs, and converts them into mp3 files. These mp3 files have the exact same name as the youtube video, and are stored in the same directory as the python file.

## YouTube Links
The youtube links are passed to the python file via a text file, namely the 'playlist.txt' file. Here, the youtube links to the videos should each be on a new line, as demonstrated in the file. All of these youtube videos will be downloaded as mp3s.

## Running the code
Firstly, it may be worth it to run the command `youtube-dl --rm-cache-dir` via the Command Line Interface (CLI) on your machine, or there may be errors thrown by the code. Then, you can simply run the python file. This can usually be done via a CLI command. The command may vary, but it will generally be along the lines of `python3 y2dl.py`. The code will then iterate through the 'playlist.txt' file, and download all of the videos as mp3s.
