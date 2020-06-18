from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=98mWszwbX9M")
dw = yt.streams.get_by_itag(18)

print(yt.streams.all())
print(yt.streams.get_by_itag(18))

dw.download("E:/")