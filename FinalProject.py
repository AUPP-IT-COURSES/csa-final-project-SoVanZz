import tkinter as tk
import base64
from tkinter import messagebox
from tkinter import scrolledtext

main = None

# Function to create the decryption page
def decryption_page():
    main.withdraw()
    decrypt_page = tk.Toplevel(main)
    decrypt_page.title("Decryption")
    decrypt_page.geometry("400x300")
    decrypt_page.configure(bg="#808080")

    # Labels and entry for decryption page
    tk.Label(decrypt_page, text="DECRYPT", font=("Arial", 16), fg="white", bg="#00bd56").place(x=10, y=0)
    tk.Label(decrypt_page, text="Enter the message to decrypt:", fg="black", font=("calibri", 14)).place(x=10, y=40)

    text2 = tk.Text(decrypt_page, font="Roboto 16", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text2.place(x=10, y=80, width=380, height=100)

    # Function to decrypt the entered message
    def decrypt():
        message = text2.get(1.0, tk.END)
        try:
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypted_message = base64_bytes.decode("ascii")
            result_page("Decrypted", decrypted_message)
            text2.delete(1.0, tk.END)
            text2.insert(tk.END, decrypted_message)
            decrypt_page.withdraw()
        except Exception as e:
            messagebox.showerror("Decryption", "Error decrypting message: {}".format(str(e)))

    # Function to go back to the main page
    def go_back():
        decrypt_page.destroy()
        main.deiconify()

    # Buttons for decryption page
    tk.Button(decrypt_page, text="Decrypt", height="2", width="23", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=10, y=200)
    tk.Button(decrypt_page, text="Back", height="2", width="23", bg="#0088CC", fg="white", bd=0, command=go_back).place(x=200, y=200)

# Function to create the encryption page
def encryption_page():
    main.withdraw()
    encrypt_page = tk.Toplevel(main)
    encrypt_page.title("Encryption")
    encrypt_page.geometry("400x300")
    encrypt_page.configure(bg="#808080")

    # Labels and entry for encryption page
    tk.Label(encrypt_page, text="ENCRYPT", font=("Arial", 16), fg="white", bg="#ed2833").place(x=10, y=0)
    tk.Label(encrypt_page, text="Enter the message to encrypt:", fg="black", font=("calibri", 14)).place(x=10, y=40)

    text2 = tk.Text(encrypt_page, font="Roboto 16", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text2.place(x=10, y=80, width=380, height=100)

    # Function to encrypt the entered message
    def encrypt():
        message = text2.get(1.0, tk.END)
        try:
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypted_message = base64_bytes.decode("ascii")
            result_page("Encrypted", encrypted_message)
            text2.delete(1.0, tk.END)
            text2.insert(tk.END, encrypted_message)
            encrypt_page.withdraw()
        except Exception as e:
            messagebox.showerror("Encryption", "Error encrypting message: {}".format(str(e)))

    # Function to go back to the main page
    def go_back():
        encrypt_page.destroy()
        main.deiconify()

    # Buttons for encryption page
    tk.Button(encrypt_page, text="Encrypt", height="2", width="23", bg="#ed2833", fg="white", bd=0, command=encrypt).place(x=10, y=200)
    tk.Button(encrypt_page, text="Back", height="2", width="23", bg="#0088CC", fg="white", bd=0, command=go_back).place(x=200, y=200)

# Function to create the result page
def result_page(title, message):
    result_window = tk.Toplevel(main)
    result_window.title(title)
    result_window.geometry("300x250")
    result_window.configure(bg="#F0F0F0")

    # Labels and scrolled text for result page
    title_label = tk.Label(result_window, text=title, font=("Arial", 16), fg="#333", bg="#F0F0F0")
    title_label.pack(pady=10)

    result_text = scrolledtext.ScrolledText(result_window, font=("Roboto", 12), wrap=tk.WORD, width=30, height=5)
    result_text.pack(pady=10)
    result_text.insert(tk.END, message)
    result_text.configure(state='disabled')

    # Functions for result page buttons
    def close_result():
        result_window.destroy()
        main.deiconify()

    def copy_to_clipboard():
        main.clipboard_clear()
        main.clipboard_append(message)
        main.update()

    # Buttons for result page
    close_button = tk.Button(result_window, text="Close", command=close_result, bg="#0088CC", fg="white", bd=0, padx=10)
    close_button.pack(side="bottom", pady=10)

    copy_button = tk.Button(result_window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#0088CC", fg="white", bd=0, padx=10)
    copy_button.pack(side="bottom", pady=10)

# Function to create the main screen
def mainScreen():
    global main

    # Function to exit the application
    def exit_app():
        main.destroy()

    # Main window setup
    main = tk.Tk()
    main.title("Encrypt/Decrypt Message App")
    main.geometry("400x250")
    main.configure(bg="#F0F0F0")

    # Labels and buttons for main screen
    tk.Label(main, text="Encrypt/Decrypt Message", font=("calibri", 20)).place(x=20, y=10)
    tk.Label(main, text="------------------------------", font=("calibri", 15)).place(x=20, y=50)
    tk.Label(main, text="Choose an Operation", font=("calibri", 15)).place(x=20, y=70)

    tk.Button(main, text="Encrypt", height="2", width="24", bg="#ed2833", fg="white", bd=0, command=encryption_page).place(x=20, y=120)
    tk.Button(main, text="Decrypt", height="2", width="25", bg="#00bd56", fg="white", bd=0, command=decryption_page).place(x=200, y=120)
    tk.Button(main, text="Exit", height="2", width="51", bg="#808080", fg="white", bd=0, command=exit_app).place(x=20, y=170)

    main.mainloop()

# Run the main screen
mainScreen()
