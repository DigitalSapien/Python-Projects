# Creating a Advanced YouTube Video Downloader

from pytube import YouTube


link = input ("Please enter the link : " )
youtube = YouTube(link)
       
print (youtube.title)
print (youtube.author)
print ("Downloading...")

youtubedownload = youtube.streams.get_highest_resolution()
youtubedownload.download ('C:\\Users\\veera\\Downloads')

print ("Download Completed.")



# !! Can't Download Age-Restricted Videos from YouTube
# !! Can't Download High-Resolution Videos from YouTube
