import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pytube as pt
from pytube import YouTube

####################################################################################################
#https://www.youtube.com/watch?v=oHg5SJYRHA0
####################################################################################################

root=tkinter.Tk()
root.title('YouTube Video Downloader')
root.configure(background='white')
root.minsize(500,200)
root.maxsize(500,200)
def url_download():
    try:
        if len(output_path) > 5:
            download_label.config(text = 'Downloading...')
            link = YouTube(str(url_entry.get()))
            link.streams.get_highest_resolution().download(output_path = output_path)
            download_label.config(text = 'Download Complete.')
            output_label.config(text = 'File has been saved to ' + output_path)

        # def progress(currentValue):
        #Couldn't get this working right away, unnecessary for use at this time.
        #     progressbar["value"]=currentValue
        #     maxValue=100
        #     progressbar=ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate")
        #     progressbar.pack(side=tk.TOP)
        #     currentValue=0
        #     progressbar["value"]=currentValue
        #     progressbar["maximum"]=maxValue
        #     divisions=10
        #     for i in range(divisions):
        #         currentValue=currentValue+10
        #         progressbar.after(500, progress(currentValue))
        #         progressbar.update() # Force an update of the GUI


    except:
        download_label.config(text = 'Error.  Press \'Clear\', select directory, and try again.')

def url_clear():
    url_entry.delete(0,END)
    download_label.config(text = 'Select an output folder, then paste a YouTube link above.')
    output_label.forget()
    url_download_button.forget()
    url_clear_button.forget()

def select_output_folder():
    global output_path
    output_path = StringVar()
    output_path =  filedialog.askdirectory(title = 'Select an output folder.')
    output_label.config(text = 'File will be saved to ' + output_path)
    output_label.pack()
    url_download_button.pack(side = 'right', padx = (0,175))
    url_clear_button.pack(side = 'left', padx = (175,0))

####################################################################################################
#Organizing frames
####################################################################################################

frame_top = ttk.Frame(root)
frame_top.pack(pady = '15')
frame_one = ttk.Frame(root)
frame_one.pack()
frame_two = ttk.Frame(root)
frame_two.pack()
frame_three = ttk.Frame(root)
frame_three.pack()
frame_bottom = ttk.Frame(root)
frame_bottom.pack()

####################################################################################################
#GUI
####################################################################################################

output_path_button = ttk.Button(frame_one, text = 'Select Output Directory', command = select_output_folder)
output_path_button.pack()
url_var = StringVar()
url_entry = ttk.Entry(frame_one, textvariable = url_var, width = '250')
url_entry.pack()
download_label = ttk.Label(frame_two, text = 'Select an output directory, then paste a YouTube link above.')
download_label.pack()
output_label_var = StringVar()
output_label = ttk.Label(root)
url_download_button = ttk.Button(frame_two, text = 'Enter', command = url_download)
url_clear_button = ttk.Button(frame_two, text = 'Clear', command = url_clear)


root.mainloop()

####################################################################################################
