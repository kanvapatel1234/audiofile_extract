from yt_dlp import YoutubeDL
import os


def download_mp3(url: str):

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)

        original_file = ydl.prepare_filename(info)

    mp3_file = os.path.splitext(original_file)[0] + ".mp3"

    if not os.path.isfile(mp3_file):
        raise FileNotFoundError(f"MP3 file not found: {mp3_file}")

    return os.path.abspath(mp3_file)


def download_mp4(url: str):

    ydl_opts = {
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)

        original_file = ydl.prepare_filename(info)

    mp4_file = os.path.splitext(original_file)[0] + ".mp4"

    if not os.path.isfile(mp4_file):
        raise FileNotFoundError(f"MP4 file not found: {mp4_file}")

    return os.path.abspath(mp4_file)