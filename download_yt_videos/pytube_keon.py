
# importing the module
from pytube import YouTube
 
# where to save
SAVE_PATH = "/Users/Monroe/Downloads" #to_do
 
# link of the video to be downloaded
link= 'https://www.youtube.com/watch?v=ZtqBQ68cfJc'

# "https://www.youtube.com/watch?v=pkYVOmU3MgA" -- fcc jovian python data structures and algorithms
# "https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
    # YouTube(link).streams.first().download()
    yt = YouTube(link)
except: 
    print("Connection Error") #to handle exception

print(f'Downloading to save path: {SAVE_PATH}')

yt.streams.filter(progressive=True, file_extension='mp4')\
.order_by('resolution')\
.desc()\
.first()\
.download(SAVE_PATH)

# try:
#     # object creation using YouTube
#     # which was imported in the beginning
#     yt = YouTube(link)
#     print('Connection established')
# except:
#     print("Connection Error") #to handle exception
 
# # filters out all the files with "mp4" extension
# mp4files = yt.streams.filter(file_extension='mp4') # .filter('mp4')
 
# #to set the name of the file
# # yt.set_filename('GeeksforGeeks Video') 
 
# # get the video with the extension and
# # resolution passed in the get() function
# d_video = yt.streams.get(mp4files[-1].extension,mp4files[-1].resolution) # get(mp4files[-1].extension,mp4files[-1].resolution)
# try:
#     # downloading the video
#     d_video.download(SAVE_PATH)
# except:
#     print("Some Error!")
# print('Task Completed!')