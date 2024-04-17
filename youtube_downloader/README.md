# YouTube Video to MP3 Downloader

This Python script allows you to download the audio from YouTube videos and save them as MP3 files.

## Prerequisites
- Python 3.x
- pytube library (`pip install pytube`)

## Usage
1. Run the script.
2. Enter the path where you want to save the .mp3 files when prompted.
3. Enter the URL of the YouTube video you want to download. You can also type "Exit" to quit.
4. The script will download the audio from the provided video URL and save it as an MP3 file in the specified destination.
5. Repeat steps 3-4 as needed. The script will continue to prompt for URLs until you type "Exit".

## How it works
- The script uses the `pytube` library to interact with the YouTube API and download videos.
- It prompts the user to input the destination path for saving the downloaded MP3 files.
- Then, it asks for the URL of the YouTube video to download. If "Exit" is entered, the script terminates.
- After downloading the audio, it converts the file format to MP3 and saves it in the specified destination.

## Notes
- Make sure you have a stable internet connection while downloading videos.
- Respect copyright laws and only download content that you have the right to use.

