import os
import re
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *

# save path for downloaded videos

MAC_SAVE_PATH = "/Users/Monroe/Downloads"
WIN_SAVE_PATH = r"C:\Users\keonm\Downloads"
MP3_SAVE_PATH = os.path.join(WIN_SAVE_PATH, "converted_mp3")
YOUTUBE_STREAM_AUDIO = "140"  # modify the value to download a different stream


def main():
    """1. Download public playlist using PyTube. Output are .mp4
    2. Convert .mp4 files to .mp3 using moviePy"""
    # create a playlist object
    # jovian_dsa_pl = "https://www.youtube.com/playlist?list=PLyMom0n-MBrqFwguQhbCu0Anlxoel08dr"
    slowed_pl = "https://www.youtube.com/playlist?list=PLsmLp2JHrigK1FBB-nuy3panZJzH5sHWO"

    PLAYLIST_OBJ = Playlist(slowed_pl)

    # this fixes the empty playlist.videos list
    PLAYLIST_OBJ._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    # create a dict of the playlist name, index
    all_urls = PLAYLIST_OBJ.video_urls
    print(len(all_urls))

    # for i, url in enumerate(all_urls):
    #     # get video title from its url
    #     myVideo = YouTube(url)
    #     title = myVideo.title
    #     length = myVideo.length
    #     print(f"{i}. Video Title: {title} \t(Length:{length})")

    # for url in PLAYLIST_OBJ.video_urls:
    #     print(url)

    # # physically downloading the audio track
    # for video in PLAYLIST_OBJ.videos:
    #     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    #     audioStream.download(output_path=WIN_SAVE_PATH)

    # TODO - convert mp4 to mp3. only obtain audio files
    # list all mp4 files in the downloads folder
    mp4_files = list_files_by_type(WIN_SAVE_PATH, ".mp4")
    print(f"\n\nThere are {len(mp4_files)} .mp4 files in the downloads dir")

    # create a dir and move all items to the dir - NOTE: define this earlier (make dir for output)
    if not os.path.exists(MP3_SAVE_PATH):
        os.mkdir(MP3_SAVE_PATH)

    for i, each_file in enumerate(mp4_files):
        # convert each file to an .mp3, then delete the .mp4 file
        mp4_name = os.path.basename(each_file).split(".mp4")[0]
        mp3_path = os.path.join(MP3_SAVE_PATH, f"{mp4_name}.mp3")
        # mp3_name = str(mp4_name, "utf-8")
        # video = VideoFileClip(os.path.join(WIN_SAVE_PATH, f"{mp4_name}.mp4"))
        # video.audio.write_audiofile(os.path.join(MP3_SAVE_PATH, f"{mp4_name}.mp3"))

        mp4_to_mp3(each_file, mp3_path)
        print(f"\n{i+1}. Converted mp4 file to mp3 : \n\t{mp3_path}")

        os.remove(each_file)


def mp4_to_mp3(mp4, mp3):
    """
    https://stackoverflow.com/questions/55081352/how-to-convert-mp4-to-mp3-using-python
    """
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()


def list_files_by_type(input_dir, input_listFileEnd):
    """Return a list of files with an extension in a given dir."""
    match_type = []  # populate list with matching files

    # TODO - create a dict using list of file extensions
    # filearrays = { '.csv':[],'.txt':[],'.jpg':[],'.png':[] }

    # filearrays = dict((val, range(int(val), int(val) + 2)) for val in input_listFileEnd)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            filename, fileext = os.path.splitext(file)
            if fileext == input_listFileEnd:
                # filearrays[fileext].append(os.path.join(root, file))
                match_type.append(os.path.join(root, file))

    return match_type


if __name__ == "__main__":
    main()
else:
    print("Executed when imported")
