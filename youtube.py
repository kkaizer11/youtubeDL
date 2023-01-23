from pytube import YouTube
import sys

def audio():
    yt = YouTube(sys.argv[1])
    audio
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download("/home/kkaizer/Music/ytDL")

def video():
    yt = YouTube(sys.argv[1])
    yt = yt.streams.get_highest_resolution()
    yt.download("/home/kkaizer/Videos/ytVideo")

x=int(input("0 pra audio ou 1 para video: "))

if x == 0:
    print("Audio")
    audio()
if x == 1:
    print("Video")
    video()


