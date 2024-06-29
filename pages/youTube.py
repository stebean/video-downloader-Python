from pytube import YouTube

def YTDownload(ytLink, title, finishlabel, pPercentage, pBar):
    try:
        ytObject = YouTube(ytLink, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining, pPercentage, pBar))
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Downloaded", text_color="white")
    except Exception as e:
        finishlabel.configure(text="URL invalid", text_color="red")

def on_progress(stream, chunk, bytes_remaining, pPercentage, pBar):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    # Update progress bar
    pBar.set(float(percentage_of_completion) / 100)
