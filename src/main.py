import sys

from pytube import YouTube

SAVE_PATH = "./yt_downloaded"


def download_video(url, file_extension):
    try:
        yt = YouTube(url)
    except Exception as e:
        print("Connection Error", e)
        sys.exit(1)

    mp4_stream = yt.streams.filter(file_extension=file_extension)

    print(mp4_stream, '\n', type(mp4_stream))
    d_video = mp4_stream[-1]

    try:
        d_video.download(output_path=SAVE_PATH)
        print('Video Donwloaded successfully')
    except Exception as e:
        print("Error occured", e)


if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        file_extension = 'mp4'
    else:
        file_extension = sys.argv[1]
    download_video(input("URL for youtube video :: "), file_extension)
