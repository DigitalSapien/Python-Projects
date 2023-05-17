# Basic YouTube Video Downloader

from pytube import YouTube


link = input ("Please enter the link : " )
youtube = YouTube(link)
       
print (youtube.title)
print (youtube.author)
print ("Downloading...")

youtubedownload = youtube.streams.get_highest_resolution()
youtubedownload.download ('C:\\Users\\veera\\Downloads')

print ("Download Completed.")



# !! Age-Restricted Videos from YouTube
# !! High-Resolution Videos from YouTube
