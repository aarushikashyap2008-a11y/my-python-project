#MUSIC AUDIO PLAYER PYTHON PROJECT
import os
import vlc
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")

import vlc
from tkinter import*
from tkinter import filedialog
mywin=Tk()
mywin.title("SPOOTIFY")
mywin.geometry("800x800")
mywin.config(bg="black")
instance=vlc.Instance()
player=instance.media_player_new()
#--------song list-----------------------------------------------
songs=[r"C:\Users\anubh\Downloads\Mann Mera (Official Video)  Table No 21  Rajeev Khandelwal & Tina Desai  Gajendra Verma.mp3"
       ,r"C:\Users\anubh\Downloads\Gehra Hua (PenduJatt.Com.Se).mp3",
       r"C:\Users\anubh\Downloads\Sheesha (PenduJatt.Com.Se).mp3",
       r"C:\Users\anubh\Downloads\Aawaara Angaara (PenduJatt.Com.Se).mp3",
       r"C:\Users\anubh\Downloads\Khoobsurat (PenduJatt.Com.Se).mp3"]
#-----------------------------------------listbox--------------------------------------------
playlist=Listbox(mywin,bg="black",fg="white",font=("Times New Roman",20),width=50)
playlist.place(x=50,y=100)
#-------------------------insert song names in listbox----------
for song in songs:
    playlist.insert(END,os.path.basename(song))
#--------------functions-----------------------
def play():
    selected=playlist.curselection()
    if selected:
        index=selected[0]
        media=instance.media_new(songs[index])
        player.set_media(media)
        player.play()
def pause():
    player.pause()
def resume():
    player.play()



Label(mywin,text="SPOOTIFY",bg="black",fg="green",font=("boulder",30)).place(x=300,y=20)
#Label(mywin,text="1. Mann Mera",bg="black",fg="white",font=("constantia",25)).place(x=50,y=100)
#Label(mywin,text="(by Gajendra Verma)",bg="black",fg="white",font=("constantia",15)).place(x=250,y=110)
#Label(mywin,text="2. Gehra Hua",bg="black",fg="white",font=("constantia",25)).place(x=50,y=150)
#Label(mywin,text="(by Arijit Singh)",bg="black",fg="white",font=("constantia",15)).place(x=250,y=160)
#Label(mywin,text="3. Sheesha",bg="black",fg="white",font=("constantia",25)).place(x=50,y=200)
#Label(mywin,text="(by Sawara Verma ",bg="black",fg="white",font=("constantia",15)).place(x=250,y=210)
#Label(mywin,text="4. Awaara Angaara",bg="black",fg="white",font=("constantia",25)).place(x=50,y=250)
#Label(mywin,text="(by AR Rahman)",bg="black",fg="white",font=("constantia",15)).place(x=330,y=260)
#Label(mywin,text="5. Khoobsurat",bg="black",fg="white",font=("constantia",25)).place(x=50,y=300)
#Label(mywin,text="(by Jubin Nautiyal)",bg="black",fg="white",font=("constantia",15)).place(x=260,y=310)


Button(mywin,text="PLAY",command=play,bg="green",fg="white",font=("Times New Roman",30)).place(x=50,y=450)
Button(mywin,text="PAUSE",command=pause,bg="green",fg="white",font=("Times New Roman",30)).place(x=250,y=450)
Button(mywin,text="RESUME",command=resume,bg="green",fg="white",font=("Times New Roman",30)).place(x=450,y=450)
Label(mywin,text="Enjoy Listening Music On Spootify:)  (created by Aarushi) ",bg="black",fg="white",font=("Times New Roman",20)).place(x=50,y=550)
mywin.mainloop()






