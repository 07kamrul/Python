from pytube import YouTube

video_list = open("sample.txt", "r")
drive = "E:/"
for i in video_list:
    yt = YouTube(i)
    #dw = yt.streams.first()
    try:
        dw = yt.streams.get_by_itag(22)
        # dw.download("E:/")
        dw.download(drive)
        print("Downloaded", i)
    except:
        print("Download Failed For", i)