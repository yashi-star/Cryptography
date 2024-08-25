# file-encryption
This code is a Python script that creates a graphical user interface (GUI) application for encrypting and decrypting various types of files such as text, audio, images, PDFs, and videos using the Fernet encryption algorithm from the cryptography library. The GUI is built using the tkinter library.

Here's a brief overview of the code:

Video Player (Displaying Video):

The script starts by creating a basic video player using OpenCV and tkinter. It displays frames from a video file (animation.mp4) in a tkinter window.
File Encryption and Decryption:

The script provides functionalities to encrypt and decrypt files of different types, including audio, images, PDFs, and videos. The encryption and decryption process involves generating a key using Fernet symmetric encryption.
Each type of file has its own set of functions (encrypt_audio, decrypt_audio, encrypt_image, decrypt_image, encrypt_pdf, decrypt_pdf, encrypt_video, decrypt_video) responsible for handling the encryption and decryption operations for that file type.
Text Encryption and Decryption:

The script also allows for encrypting and decrypting text using a secret key. The encrypt_text and decrypt_text functions handle the text encryption and decryption, respectively.
Graphical User Interface (GUI):

The main GUI is created using tkinter. It consists of frames for text input, buttons for encryption and decryption operations, and options to select file types for encryption and decryption.
There are different frames for encrypting and decrypting audio, images, PDFs, and videos. The GUI also includes an area for entering a secret key when encrypting or decrypting text.
The GUI has a menu bar with options like File, Option, More, Window, and Help.
About and Reset:

The script includes an "About" function (show_about) to display information about the application.
There's also a "Reset" function to clear the secret key and text input fields.
Running the Application:

The create_gui function initializes and runs the main GUI application.
Important Notes:

The encryption key is stored in a file named key.key.
The text encryption and decryption use base64 encoding.
The GUI includes an option to exit the application through the File menu.
The code is written in Python, and it uses libraries such as tkinter for GUI, cv2 for video processing, PIL for working with images, and cryptography for encryption and decryption.
