import requests
from tkinter import *


def generate_quote():
    global quote_text
    data = requests.get(url=api)
    quote = data.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


api = "https://api.kanye.rest"

screen = Tk()
screen.title("Kanye Says...")
screen.config(padx=20, pady=50)
canvas = Canvas(width=300, height=414)
photo_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=photo_image)
quote_text = canvas.create_text(150, 207, text="Kanye says...", width=250, font=("Arial", 15, "bold"))
canvas.grid(row=0, column=0)

kanye_photo_image = PhotoImage(file="kanye.png")
button = Button(image=kanye_photo_image, command=generate_quote, highlightthickness=0, borderwidth=0)
button.grid(row=1, column=0)

screen.mainloop()
