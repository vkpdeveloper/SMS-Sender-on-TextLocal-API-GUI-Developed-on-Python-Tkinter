import urllib.request
import urllib.parse
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from tkinter.scrolledtext import ScrolledText
import re

win = tk.Tk()
win.title("SMS Sending ~ Vaibhav Pathak")
win.geometry("400x500")
win.minsize(400,500)
win.maxsize(400,500)
frame = tk.Frame()
frame.grid(row=2, column=0, padx=40, pady=10)

def onSend():
    api_key = api.get()
    receiver = number.get()
    get_sender = senders.get()
    get_message = message_get.get()
    if (api_key != '') and (receiver != '') and (get_message != ''):
        data =  urllib.parse.urlencode({'apikey': api_key, 'numbers': receiver, 'message' : get_message, 'sender': get_sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        checking = str(fr)

        if re.search('success', checking):
            m_box.showinfo("Success", "Message Sended Successfully.")
        elif re.search("failure", checking):
            m_box.showerror('Error', "Message Not Sended (Something Went Wrong !)")
    else:
        m_box.showerror("Error", "Please Fill Every Detail Carefully !")


example = ttk.Label(win, text="SMS Sender", font="AiralBlack 20").grid(row=0, columnspan=3, pady=30)

label1 = ttk.Label(frame, text="Enter Your TextLocal API Key : ")
label1.grid(row=2, column=0, padx=0, pady=0, sticky=tk.W)

api = tk.StringVar()
api_entry = ttk.Entry(frame, width=50, textvariable=api)
api_entry.grid(row=3, columnspan=4, ipady=3, padx=0)
api_entry.focus()

label2 = ttk.Label(frame, text="Enter Receiver Mobile Number : ")
label2.grid(row=4, column=0, padx=0, pady=0, sticky=tk.W)

number = tk.StringVar()
number_entry = ttk.Entry(frame, width=50, textvariable=number)
number_entry.grid(row=5, columnspan=3, ipady=3, padx=0)

label3 = ttk.Label(frame, text="Enter Sender ID (If You Have else Do not Fill It) : ")
label3.grid(row=6, column=0, padx=0, pady=2, sticky=tk.W)

senders = tk.StringVar()
sender_entry = ttk.Entry(frame, width=50, textvariable=senders)
sender_entry.grid(row=7, columnspan=3, ipady=3, padx=0)

label4 = ttk.Label(frame, text="Enter Your Message Here : ")
label4.grid(row=8, column=0, padx=0, pady=2, sticky=tk.W)

message_get = tk.StringVar()
message_entry = ttk.Entry(frame, width=50, textvariable=message_get)
message_entry.grid(row=9, column=0, ipady=4, padx=0, pady=0)

btn1 = ttk.Button(frame, width=30, text= "Send Message", command=onSend).grid(row=10, columnspan=3, padx=20, pady=10, ipady=6)

win.mainloop()