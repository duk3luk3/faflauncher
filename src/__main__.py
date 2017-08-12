import tkinter as tk
from tkevents import TkEventLoop
import asyncio

import updater

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        #asyncio.async(self.launch())
        #self.do_github()
        #asyncio.get_event_loop().run_until_complete(self.do_github())

    def launch(self, loop):
        f = asyncio.ensure_future(updater.fetch_tags('FAForever', 'client'), loop=loop)
        f.add_done_callback(app.set_github)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.label = tk.Label(self)
        self.label["text"] = 'empty...'
        self.label.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    async def do_github(self):
        print("launched")
        tag, zipball_url = await updater.check_update()

        self.label["text"] = "{} => {}".format(tag, zipball_url)

    def set_github(self, fut):
        tag, zipball_url = fut.result()

        self.label["text"] = "{} => {}".format(tag, zipball_url)

root = tk.Tk()
app = Application(master=root)
#app.mainloop()

loop = TkEventLoop(app)
app.launch(loop)
loop.mainloop()
