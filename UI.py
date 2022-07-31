#!bin/python3/3.6
import tkinter as tk
from tkinter import Menu, Scrollbar, ttk
from tkinter import filedialog
import webbrowser
from googletts import TTS
import tkinter.filedialog
import os

main = tk.Tk()
main.title('AnySay')
current_theme = ttk.Style(main).theme_use('clam')

Width = main.winfo_screenwidth()
Height = main.winfo_screenheight()
main.geometry(f'{Width-20}x{Height-20}')
os.getcwd()

Blue = '#264653'
SemiBlue = '#e76f51'
white = '#e9c46a'
black = '#575366'

Text1 = tk.StringVar()

MenuBar = Menu(main,tearoff=0)
main.config(menu=MenuBar)
FileMenu = Menu(MenuBar)
MenuBar.add_cascade(label='File',menu=FileMenu)
FileMenu.add_separator()
FileMenu.add_command(label='Donate', command=lambda a='':webbrowser.open('https://www.paypal.me/zone1onpay'))
FileMenu.add_separator()
FileMenu.add_command(label='Exit', command=main.quit)

Options = Menu(MenuBar)
MenuBar.add_cascade(label='Options',menu=Options)

AboutUs = Menu(MenuBar)
MenuBar.add_cascade(label='About Us',menu=AboutUs)
AboutUs.add_command(label='About Us', command=lambda a='':webbrowser.open('https://www.zone1on.com/about-us/'))
AboutUs.add_command(label='Donate', command=lambda a='':webbrowser.open('https://www.paypal.me/zone1onpay'))
AboutUs.add_command(label='Contact Us', command=lambda a='':webbrowser.open('https://www.zone1on.com/contact-us/'))

class Pages:
    def Convert():
        Frame = tk.Frame(main,background=white)
        Frame.pack(fill=tk.BOTH, expand=1)
        Label = tk.Label(Frame, text='Convert Text to Speech',font='Times 22',fg=black,bg=white)
        Label.pack(padx=10, pady=10)

        Label = tk.Label(Frame, text='Text:',font='Times 12',fg=black,bg=white)
        Label.pack(fill='both')

        TextFrame = tk.Frame(Frame,height=Height//60,background=Blue)
        TextFrame.pack(fill=tk.BOTH)

        Scroll = Scrollbar(TextFrame,orient=tk.VERTICAL,background=SemiBlue,troughcolor=white)
        Scroll.pack(side=tk.RIGHT, fill=tk.Y)
        Text = tk.Text(TextFrame,font='Times 15',yscrollcommand=Scroll.set,wrap=tk.WORD,height=Height//50,background=white,fg=black,blockcursor=True,cursor='arrow')
        Text.pack(fill='both',padx=15,pady=5)
        if Text1.get() != '':
            Text.insert(tk.END,Text1.get())
        else:
            Text.insert(tk.END,'Type your text here.....')
        
        def Copy():
            Text.clipboard_clear()
            Text.clipboard_append(Text.get(1.0,tk.END))
            MSG = tk.Label(Frame, text='Copied to clipboard',font='Times 12',fg=black,bg=white).pack(padx=10, pady=10)
        def Paste():
            Text.insert(tk.END,Text.clipboard_get())
        Text.bind('<Control-c>',lambda event: Copy())
        Text.bind('<Control-v>',lambda event: Paste())
        Text.bind('<Control-a>',lambda event: Text.tag_add('sel','1.0','end'))
        Text.bind('<Control-x>',lambda event: Text.delete(Text.tag_ranges('sel')))
        def OpenFile():
            Text.delete(1.0,tk.END)
            file = filedialog.askopenfilename(parent=Frame,filetypes=[('Text Files','*.txt')])
            with open(file,'r') as e:
                Text.insert(tk.END,e.read())
        
        def SaveFile():
            file = filedialog.asksaveasfilename(parent=Frame,filetypes=[('Text Files','*.txt')])
            with open(file,'w') as e:
                e.write(Text.get(1.0,tk.END))
                e.close()
        Options.add_command(label='Save Text', command=lambda a='':SaveFile())
        Options.add_command(label='Open', command=lambda a='': OpenFile())
        Scroll.config(command=Text.yview)
        Label = tk.Label(Frame, text='Language:',font='Times 12',fg=black,bg=white)
        Label.pack(fill='x',padx=50,pady=5)

        Language = tk.StringVar()
        Option = ttk.Combobox(Frame, textvariable=Language,exportselection=False,justify='center', values=TTS.LangList(),background=Blue,foreground=black)
        Option.pack(fill='x',padx=50,pady=5)
        Option.current(0)

        Label = tk.Label(Frame, text='Filename:',font='Times 12',fg=black,bg=white)
        Label.pack(fill='x',padx=50,pady=5)
        Filename = tk.Entry(Frame)
        Filename.pack(fill='x',padx=50,pady=5)
        def OpenDirectory():
            
            File = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
            Filename.insert(0,str(File).join('.mp3'))
            return File

        ButtonFrame = tk.Frame(Frame,background='#f0f0f0')
        Width = main.winfo_screenwidth()
        ButtonFrame.pack(fill='x',pady=20,side='top')

        Button = tk.Button(Filename, text='Choose Directory', command=lambda: OpenDirectory(),width=15,height=1,background=Blue,fg=white)
        Button.pack(side='right',padx=10,pady=10,fill='y')

        Button2 = tk.Button(ButtonFrame, text='Download', command=lambda: TTS.Save(Text.get('1.0', 'end-1c'), Language.get(), Filename.get()),width=15,height=2,background=SemiBlue,fg=white)
        Button2.pack(side='left',padx=Width//5,pady=10,fill='y')

        Button3 = tk.Button(ButtonFrame, text='Play', command=lambda: TTS.Say(Text.get('1.0', 'end-1c'), Language.get()),width=15,height=2,background=SemiBlue,fg=white)
        Button3.pack(side='right',padx=Width//5,pady=10,fill='y')


Pages.Convert()
main.mainloop()