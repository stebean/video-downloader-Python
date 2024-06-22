import tkinter
import customtkinter
from pytube import YouTube

def YTDownload():
    try:
        ytLink = url.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        ytObject.streams
        
        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Downloaded")   
    except:
        finishlabel.configure(text="URL invalid", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    #Update progress bar
    pBar.set(float(percentage_of_completion) / 100)
    
# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Video Downloader")

# UI
title = customtkinter.CTkLabel(app, text="Insert URL")
title.pack(padx=10, pady=10)

# URL input
url_var =tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
url.pack()

#End Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progess bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

pBar = customtkinter.CTkProgressBar(app, width=400)
pBar.set(0)
pBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=YTDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()