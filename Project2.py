import tkinter
from tkinter import ttk
import requests

class MoviesDB:

    def __init__(self, master):
        self.master = master
        self.createWidgets()

    def createWidgets(self):
        self.movie_label = ttk.Label(self.master, text='Search for a Movie', background='light blue', font=('helvetica', 20))
        self.movie_label.grid(row=0, sticky='w', padx=50, pady=25)

        self.entry = ttk.Entry(self.master, width=50)
        self.entry.grid(row=1, sticky='w', padx=50, pady=5, ipady=4)

        self.button = ttk.Button(text='Go', command=self.getMovie)
        self.button.grid(row=2, sticky='w', padx=50, pady=5)

        self.movie_frame = ttk.LabelFrame(self.master, width=1000, height=450, relief='groove', text='Movie details')
        self.movie_frame.grid_propagate(False)#This is because the frame doesn't show size of the widget inside it
        self.movie_frame.grid(row=3, sticky='w', padx=50, pady=5)

    def getMovie(self):
        if self.movie_frame.grid_slaves():
            self.clearContents()

        endpoint = "http://www.omdbapi.com/" #Location of movie website
        payload = {"apikey":"6b1ede37", "t": self.entry.get()}#apikey and t is the search parameter
        response = requests.get(endpoint, params=payload)#url and parameters are arg
        movie =response.json() #will display the data of movie

        keys = ['Title', 'Year', 'Rated', 'Genre', 'Director', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'imdbRating']

        for item in keys:
            text_val = item + " : " + movie[item]
            ttk.Label(self.movie_frame,
                      text=text_val,
                      font=('helvetica', 9),
                      wraplength=1000).grid(padx=3, pady=3, sticky='w')
        self.entry.delete(0, 'end') #remove contents of the entry box
        
    def clearContents(self):
        for widget in self.movie_frame.grid_slaves():
            widget.destroy()#call it in get_movie method

    def closemethod(self):
        pass
        


if __name__ == '__main__':
    master = tkinter.Tk()
    MoviesDB(master)
    master.title('Movies DB')
    master.geometry('1200x650+125+50')
    master.mainloop()