import validators as validators
import youtube_dl
import os
from pytube import YouTube
from pytube.cli import on_progress


# from tqdm import tqdm]


def download_video(url, filename, directory):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(directory, f"{filename}.mp4")
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.DownloadError:
            print("Error downloading the video.")


def download_video_utube(url, directory):
    try:
        yt = YouTube(url)
        yt.register_on_progress_callback(on_progress)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=directory)
    except (YouTube.Error, IOError, ConnectionError) as e:
        print(f"Error downloading the video: {str(e)}")


def on_progress(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentage = (bytes_downloaded / total_bytes) * 100
    print(f"\rDownloaded {percentage:.2f} %", end="")
    if bytes_remaining == 0:
        print()


def validate_directory(directory):
    if not os.path.isdir(directory):
        print("Invalid directory path. Please provide a valid directory.")
        return False
    return True


def validate_url(url):
    if not validators.url(url):
        print("Invalid URL. Please provide a valid URL.")
        return False
    return True


def main():
    while True:
        try:
            root_directory = input('input directory path or input "root" for current directory: ')
            if root_directory == "root":
                root_directory = os.getcwd()
            if not validate_directory(root_directory):
                continue
            video_url = input('input url: ')
            if not validate_url(video_url):
                continue
            if "youtu" in video_url:
                download_video_utube(video_url, root_directory)
            else:
                with youtube_dl.YoutubeDL() as ydl:
                    try:
                        info_dict = ydl.extract_info(video_url, download=False)
                        filename = info_dict.get('title', None)
                        if not filename or [file for file in os.listdir(root_directory) if
                                            file.startswith(f'{filename}')]:
                            files = [file for file in os.listdir(root_directory) if
                                     file.startswith(f'{filename}')]
                            count = len(files)
                            if count > 0:
                                print("already been downloaded")
                                filename = f"video{count}"
                            else:
                                filename = 'video'
                    except youtube_dl.utils.DownloadError:
                        print("Error extracting video information.")
                        continue
                download_video(video_url, filename, root_directory)


        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            key = input("Press any key to continue or Enter to exit: ")
            if key == "":
                break


if __name__ == '__main__':
    main()
