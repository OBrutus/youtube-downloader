import sys

from time import time
from pytube import YouTube, Playlist

import video_download

if __name__ == '__main__':
    file_extension = 'mp4'
    if sys.argv.__len__() > 1:
        file_extension = sys.argv[1]

    playlist_link = input('Enter Playlist URL :: ')

    video_links = Playlist(playlist_link).video_urls

    video_title = []

    start = time()
    for link in video_links:
        yt_video = YouTube(link)
        video_title.append(yt_video.title)
        current_video_start_time = time()
        print(f'Downloading {yt_video.title}')

        try:
            video_download.download_video(
                yt_video.watch_url,
                file_extension=file_extension
            )
        except Exception as e:
            print('Exception occurred while downloading video '
                  + f'{yt_video.title()} with err :: {e}')

        print(f'Execution of {yt_video.title} in '
              + '{time() - current_video_start_time} seconds')

    print(f'Time taken: {time() - start}')
