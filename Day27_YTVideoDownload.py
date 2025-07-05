from pytube import YouTube

link = input("Enter YouTube video URL: ")

try:
    yt = YouTube(link)
    print("Title:", yt.title)
    print("Views:", yt.views)

    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")
except Exception as e:
    print("Error:", e)
