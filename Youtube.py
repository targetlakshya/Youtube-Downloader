from pytube import YouTube

link = input("Please provide me a link\n")

check = int(input("Please Choose One of them\n 1. Videos\n 2. Audio \n 3. Thumbnail \n "))

if check == 1:
    youtube_1 = YouTube(link)

    print(youtube_1.title) # Title

    videos = youtube_1.streams.filter(progressive = True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)

    Stream = int(input("Please provide your index that you want to download\n"))

    videos[Stream].download()
    print("Successfully Downloaded")

elif check == 2:
    youtube_2 = YouTube(link)
    audio = youtube_2.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    stream = int(input("Type your index that you want to download\n")) 
    audio[stream].download()
    print("Successfully Downloaded")

elif check == 3:
    youtube_3 = YouTube(link)
    print(youtube_3.thumbnail_url) 
