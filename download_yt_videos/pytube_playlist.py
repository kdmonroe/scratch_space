from pytube import Playlist

# save path for downloaded videos
SAVE_PATH = "/Users/Monroe/Downloads"

# create a playlist object
jovian_dsa_pl = "https://www.youtube.com/playlist?list=PLyMom0n-MBrqFwguQhbCu0Anlxoel08dr"
p = Playlist(jovian_dsa_pl)

# loop through all containing videos and download
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.first().download(SAVE_PATH)