import os
from pytube import YouTube


def get_destination():
    dest = input("Enter the path where you want to save the .mp3 files: \n>>")
    return dest


def get_video_url():
    # Gets the URL from user
    url = str(input("\nEnter the URL of the video you want to download or enter \"Exit\" to quit: \n>> "))

    if url.lower() == 'exit':
        return 'exit'

    return url


def download_audio_from_youtube(url, destination):
    # Downloads audio from a YouTube video and saves it as a mp3 file.
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)
    base, _ = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file, yt.title


def main():
    destination = get_destination()
    url = get_video_url()

    while url != 'exit':
        downloaded_file, title = download_audio_from_youtube(url, destination)
        print(f'\"{title}\" has been successfully downloaded!')
        url = get_video_url()


if __name__ == "__main__":
    main()
