from tkinter import Tk, Button


def main(event_loop):
    root = Tk()
    
    b1 = Button(
        master=root,
        text="hello"
    )

    b2 = Button(
        master=root,
        text="hello2"
    )

    b1.pack()
    b2.pack()
    root.mainloop()


if __name__ == "__main__":
    #   event_loop = asyncio.get_event_loop()
    event_loop=None
    main(event_loop)
