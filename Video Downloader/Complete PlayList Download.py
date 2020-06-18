import pytube

pl = "https://www.youtube.com/playlist?list=PLCLnBNc46Gh_9ly7uWbxEf0zhJHflRqH3"

# pytube.Playlist("https://www.youtube.com/playlist?list=PLCLnBNc46Gh_9ly7uWbxEf0zhJHflRqH3").download_all("E:/")

pytube.Playlist(pl).download_all("E:/")