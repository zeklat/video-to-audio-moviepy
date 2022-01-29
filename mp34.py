#mp4 to mp3
from tkinter import ttk
from tkinter import filedialog 
from tkinter import *
import moviepy.editor as mp

root = Tk()
root.title("convert mp4 to mp3")
root.geometry("500x500")
def mp4():
    thefile = filedialog.askopenfile(initialdir= "/",title= "choose video",filetypes=(("mp4 files","*.mp4"),("wav files","*.wav")))
    clip = mp.VideoFileClip(thefile)
    clip.audio.write_audiofile(thefile+".mp3")

    



selecfile = Button(root,text="select file",command=mp4).pack()

root.mainloop()

