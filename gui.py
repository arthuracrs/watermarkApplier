import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

def button_function():
    print("button pressed")

def openWatermarkImage():
    filename = tkinter.filedialog.askopenfilename()

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()


# import customtkinter

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# def apply():
#     print("fom")

# root = customtkinter.CTk()
# root.geometry("500x300")

# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20,padx=60, fill="both", expand=True)

# label = customtkinter.CTkLabel(master=frame, text="watermark applier")
# label.pack(pady=12, padx=10)

# buttom = customtkinter.CTkButton(master=frame, text="apply", command=apply)
# buttom.pack(pady=12, padx=10)

# root.mainloop()