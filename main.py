from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt =  YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension="mp4")
        video_res = video.get_highest_resolution()
        video_res.download(output_path = save_path)
        print("Video downloaded successfully")

    except Exception as e:
        print(e)   


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder:  {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hide the main window to show a dialog box instead

    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Starting Download...")
        download_video(video_url, save_dir)

    else:
        print("Invalid save location!")  