import random
import string
import tkinter as tk

def generate_custom_password():
    sub()

def exit_program():
    root.destroy()

def sub():
    len_of_password = int(entry.get())
    s1 = string.ascii_lowercase
    s2 = string.digits
    s3 = string.ascii_uppercase
    s4 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    text.set(''.join(s[:len_of_password]))

root = tk.Tk()
root.title('Password Generator')
root.geometry('350x400')

entry_label = tk.Label(root, text='Enter the length of password:')
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

custom_button = tk.Button(root, text='Generate Custom Password', command=generate_custom_password)
custom_button.pack(pady=10)

exit_button = tk.Button(root, text='Exit', command=exit_program)
exit_button.pack(pady=10)

text = tk.StringVar()
result_label = tk.Label(root, textvariable=text)
result_label.pack(pady=10)

root.mainloop()