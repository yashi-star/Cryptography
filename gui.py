from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import base64
import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.resizable (True,True)                                                             
root.title("Video Player")
root.configure(bg="#0c111b")
video = cv2.VideoCapture('animation.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


def play_video():
    # Read
    ret,frame = video.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo
        root.after(30, play_video)
    else:
        video.release()
play_video()
animation_duration = 4000
root.after(animation_duration, root.destroy)
root.mainloop()


def encrypt_audio():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as filekey:
        filekey.write(key)
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if file_path:
        with open(file_path, 'rb') as file:
            original_file = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(original_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Audio Files", "*.wav")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(encrypted)
                print("Audio encryption completed.")


def decrypt_audio():
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if file_path:
        with open(file_path, 'rb') as file:
            encrypted_file = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Audio Files", "*.wav")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(decrypted)
                print("Audio decryption completed.")


def encrypt_image():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as filekey:
        filekey.write(key)
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpeg")])
    if file_path:
        with open(file_path, 'rb') as file:
            original_file = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(original_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.jpeg")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(encrypted)
                print("Image encryption completed.")
               

def decrypt_image():
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpeg")])
    if file_path:
        with open(file_path, 'rb') as file:
            encrypted_file = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.jpeg")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(decrypted)
                print("Image decryption completed.")
                

def encrypt_pdf():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as filekey:
        filekey.write(key)
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            original_file = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(original_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(encrypted)
                print("PDF encryption completed.")
               

def decrypt_pdf():
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            encrypted_file = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(decrypted)
                print("PDF decryption completed.")

                
def encrypt_video():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as filekey:
        filekey.write(key)
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Videos", "*.mkv")])
    if file_path:
        with open(file_path, 'rb') as file:
            original_file = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(original_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Video", "*.mkv")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(encrypted)
                print("Video encryption completed.")
               

def decrypt_video():
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    file_path = filedialog.askopenfilename(filetypes=[("Video", "*.mkv")])
    if file_path:
        with open(file_path, 'rb') as file:
            encrypted_file = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_file)
        save_path = filedialog.asksaveasfilename(filetypes=[("Video", "*.mkv")])
        if save_path:
            with open(save_path, 'wb') as file:
                file.write(decrypted)
                print("Video decryption completed.")

                
def encrypt_text():
    key = code.get()
    if key == "1234" :
        root1 = Toplevel(root)
        root1.title("encryption")
        root1.geometry("400x200")
        root1.configure (bg="#0c111b")
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode (encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(root1, text="ENCRYPT", font="arial", fg="white", bg="#0c111b").place(x=10, y=0)
        text2 = Text (root1, font="Rpbote 10", bg="white", relief=SUNKEN)
        text2.place(x=10, y=40,width=380,height=150)
        text2.insert (END,encrypt)
        print("text encryption completed.")
    elif key == "":
        messagebox.showerror("encryption", "Input secret key") 
    elif key != "1234":
        messagebox.showerror("encryption", "Invalid key")


def decrypt_text():
    key = code.get()
    if key == "1234" :
        root2 = Toplevel(root)
        root2.title("decryption")
        root2.geometry("400x200")
        root2.configure (bg="#0c111b")
        message = text1.get(0.0, END).strip()
        base64_bytes = base64.b64decode(message)
        decrypt = base64_bytes.decode("ascii")
        Label(root2, text="DECRYPT", font="arial", fg="white", bg="#0c111b").place(x=10, y=0)
        text2=Text (root2, font="Rpbote 10", bg="white", relief=SUNKEN)
        text2.place(x=10, y=40,width=380,height=150)
        text2.insert (END,decrypt)
        print("text decryption completed.")
    elif key == "":
        messagebox.showerror("decryption", "Input secret kry")
    elif key != "1234":
        messagebox.showerror("decryption", "Invalid secret key")
        

def show_about():
    messagebox.showinfo("About", "This is a sample application.\n\nVersion: 1.0\n By-Yashi Pant")
def reset():
        code.set("")
        text1.delete (1.0, END)

def create_gui():
    global root
    global text1
    global code
    root = Tk()
    root.title("Data Security")
    root.geometry("700x900")
    root.resizable (False,True)                                                             
    root.configure(bg="#0c111b")
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_command(label='Exit', command=root.quit)
    optionmenu = Menu(menu)
    menu.add_cascade(label='Option', menu=optionmenu)
    optionmenu.add_command(label="cut")
    optionmenu.add_command(label="copy")
    optionmenu.add_command(label="paste")
    moremenu = Menu(menu)
    menu.add_cascade(label='More', menu=moremenu)
    moremenu.add_command(label="Undo")
    moremenu.add_command(label="Redo")
    windowmenu = Menu(menu)
    menu.add_cascade(label='window', menu=windowmenu)
    windowmenu.add_command(label="gui.py-C:/users/desktop/miniproject/gui.py")
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=show_about)
    
#logo
    Label(root, text="' Securing Your Files '",bg="#0c111b", fg="white", font="algerian 30 bold").place(x=100,y=20)

#first Frame
    frame1 = Frame (root, bd=3, bg="black",width=340, height=280, relief=SUNKEN)
    frame1.place(x=10,y=80)
    lb1 = Label(frame1, bg="black")
    lb1.place(x=40, y=10)
    Button(frame1, text="Encrypt",width=10, height=2 ,fg="white",bg="green",command=encrypt_text).place(x=130, y=26)
    Button(frame1, text="Decrypt",width=10, height=2,fg="white",bg="green",command=decrypt_text).place(x=130,y=76)
    Button(frame1, text="Reset",width=10, height=2,fg="white",bg="red",command=reset).place(x=130,y=130)
    Label(text=" enter secret key ", fg="white", bg="black", font=("calibri", 13)).place(x=130, y=250)
    code = StringVar()
    Entry(textvariable=code, width=10, bd=0, font=("arial", 20), show="*").place(x=110, y=280)   
#Second Frame
    frame2 = Frame (root, bd=3, width=340,height=280, bg="white", relief=SUNKEN)
    frame2.place(x=350, y=80)
   # Label(text, fg="white",bg="black", font=("calbri", 13)).place(x=360, y=90)
    text1 = Text (frame2, font="Robote 20", bg="black", fg="green", relief=RAISED)
    text1.place(x=0, y=0,width=320, height=295)
    scrollbar1=Scrollbar (frame2)
    scrollbar1.place(x=320, y=0, height=300)
    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)
#third Frame
    frame3 = Frame (root, bd=3, bg="#aaa", width=330, height=150, relief=SUNKEN)
    frame3.place(x=10, y=370)
    Button(frame3, text="Audio",width=10, height=2,command=encrypt_audio,fg="white",bg="#dc143c").place(x=30, y=26)
    Button(frame3, text="Image",width=10, height=2,command=encrypt_image,fg="white",bg="#dc143c" ).place(x=180, y=26)
    Button(frame3, text="PDF",width=10, height=2,command=encrypt_pdf,fg="white",bg="#dc143c" ).place(x=30, y=76)
    Button(frame3, text="Video",width=10, height=2,command=encrypt_video,fg="white",bg="#dc143c" ).place(x=180, y=76)
    Label(frame3, text="Encrypting- video, Image, audio,pdf", bg="#aaa",fg="black").place(x=20, y=5)
#fourth Frame
    frame4 = Frame (root, bd=3, bg="#aaa",width=330,height=150, relief=SUNKEN)
    frame4.place(x=360, y=370)
    Button (frame4, text="Audio",width=10, height=2 ,command=decrypt_audio,fg="white",bg="#dc143c").place(x=30, y=26)
    Button (frame4, text="Image",width=10, height=2,command=decrypt_image,fg="white",bg="#dc143c").place(x=180,y=26)
    Button (frame4, text="PDF",width=10, height=2,command=decrypt_pdf,fg="white",bg="#dc143c" ).place(x=30, y=76)
    Button (frame4, text="Video",width=10, height=2,command=decrypt_video,fg="white",bg="#dc143c").place(x=180, y=76)
    Label(frame4, text="Decrypting- video, Image, audio,pdf", bg="#aaa", fg="black").place (x=20,y=5)
    root.mainloop()
create_gui()

