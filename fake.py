button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello")
slogan.pack(side=tk.LEFT)

w = Scale(root, from_=0, to=42)
w.pack()


l = Label(root, text = "Walking Speed")
l.config(font =("Courier", 14))
l.pack()
button1 = ttk.Button(text="Button Example")

# pack() padding adds pixels outside the TButton. The widget’s position is changed.
button1.grid(row=15,column=15)