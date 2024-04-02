import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pytube
 

  
class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#85929E")
       

        self.video_url = tk.StringVar()
        self.download_folder = tk.StringVar()
        self.selected_resolution = tk.StringVar()
        self.button = tk.Button(bg="blue")

        self.create_widgets()
    
    
    def create_widgets(self):
        # Frame 1
        frame1 = ttk.LabelFrame(self.root, text="Video URL")
        frame1.pack(pady=10)

        entry1 = ttk.Entry(frame1, width=50, textvariable=self.video_url)
        entry1.grid(row=0, column=0, padx=(20, 0), pady=10)

        browse_button = ttk.Button(frame1, text="Browse", command=self.browse_video)
        browse_button.grid(row=0, column=1, padx=10, pady=10)

        # Frame 2
        frame2 = ttk.LabelFrame(self.root, text="Download Folder")
        frame2.pack(pady=10)

        entry2 = ttk.Entry(frame2, width=50, textvariable=self.download_folder, state="readonly")
        entry2.grid(row=0, column=0, padx=(20, 0), pady=10)

        browse_button = ttk.Button(frame2, text="Browse", command=self.browse_folder)
        browse_button.grid(row=0, column=1, padx=10, pady=10)

        # Frame 3
        frame3 = ttk.LabelFrame(self.root, text="Resolution")
        frame3.pack(pady=10)

        resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
        self.resolution_options = ttk.Combobox(frame3, values=resolutions, textvariable=self.selected_resolution)
        self.resolution_options.current(0)
        self.resolution_options.grid(row=0, column=0, padx=(20, 0), pady=10)

        # Frame 4
        frame4 = ttk.LabelFrame(self.root, text="Actions")
        frame4.pack(pady=10)

        download_button = ttk.Button(frame4, text="Download", command=self.download_video)
        download_button.grid(row=0, column=0, padx=10, pady=10)

        reset_button = ttk.Button(frame4, text="Reset", command=self.reset)
        reset_button.grid(row=0, column=1, padx=10, pady=10)

        exit_button = ttk.Button(frame4, text="Exit", command=self.exit)
        exit_button.grid(row=0, column=2, padx=10, pady=10)

    def browse_video(self):
        url = filedialog.askopenfilename(filetypes=[("Video URL", "url")])
        self.video_url.set(url)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.download_folder.set(folder)

    def download_video(self):
        url = self.video_url.get()
        folder = self.download_folder.get()
        resolution = self.selected_resolution.get()

        if url == "" or folder == "":
            messagebox.showerror("Error", "Video URL and Download Folder are required.")
            return

        try:
            youtube = pytube.YouTube(url)
            video = youtube.streams.filter(res=resolution).first()
            video.download(folder)
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error downloading video: {e}")

    def reset(self):
        self.video_url.set("")
        self.download_folder.set("")
        self.selected_resolution.set("1080p")

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
    
    
