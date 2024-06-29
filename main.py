import tkinter
import customtkinter
from pages.youTube import YTDownload, on_progress

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
url_var = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
url.pack()

# End Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

pBar = customtkinter.CTkProgressBar(app, width=400)
pBar.set(0)
pBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=lambda: YTDownload(url_var.get(), title, finishlabel, pPercentage, pBar))
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
