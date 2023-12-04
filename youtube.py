from pytube import YouTube
import sys


def audio():
    yt = YouTube(sys.argv[1])
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download()  # Adicione o path desejavel


def video():
    yt = YouTube(sys.argv[1])
    yt = yt.streams.get_highest_resolution()
    yt.download()  # Adicione o path desejavel


if __name__ == "__main__":
    x = int(input("0 pra audio ou 1 para video: "))

    if x == 0:
        print("Audio")
        audio()
    if x == 1:
        print("Video")
        video()
