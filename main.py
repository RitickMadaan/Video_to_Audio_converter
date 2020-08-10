import moviepy.editor as mp
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def extract_audio(video_path):
    video = mp.VideoFileClip(video_file)

    video.audio.write_audiofile(r"C:\Users\Ritick Madaan\Desktop\audio.mp3")


Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
video_file = askopenfilename()
extract_audio(video_file)
