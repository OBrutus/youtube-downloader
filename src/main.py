import sys

from pytube import YouTube

SAVE_PATH = "./yt_downloaded"

def main(URL, file_extension):
    try:
        yt = YouTube(URL)
    except:
        print("Connection Error")
        sys.exit(1)

    mp4_stream = yt.streams.filter(file_extension = file_extension)

    print(mp4_stream, '\n', type(mp4_stream))
    d_video = mp4_stream[-1]

    try:
        d_video.download(output_path=SAVE_PATH)
        print('Video Donwloaded successfully')
    except:
        print("Error occured")


if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        file_extension = 'mp4'
    else:
        file_extension = sys.argv[1]
    main(input("URL for youtube video :: "), file_extension)
