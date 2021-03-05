import pandas as pd
from tkinter import *
from tkinter.ttk import *

# Setting up maximum column width for pandas
pd.set_option('display.max_colwidth', 150)

root = Tk()
root.title("Random Anime Selector")

clickedGenre = StringVar()
clickedGenre.set("Genre")
clickedScore = StringVar()
clickedScore.set("Score")

# The Again Button | Generates a random anime with the same parameters as the previous one
def again(a, b, c, d, e, f, x, y):
    # Removes the generated widgets of the anime and makes new ones
    a.grid_remove()
    b.grid_remove()
    c.grid_remove()
    d.grid_remove()
    e.grid_remove()
    f.grid_remove()
    generate(x, y)

# The Back Button | Takes you back to the menu
def back(a, b, c, d, e, f):
    # Places the menu widgets back
    animeLabel.grid()
    dropdownGenre.grid()
    dropdownScore.grid()
    generateButton.grid()
    # Removes the widgets for the anime
    a.grid_remove()
    b.grid_remove()
    c.grid_remove()
    d.grid_remove()
    e.grid_remove()
    f.grid_remove()

# Generates the random anime
def generate(clickgenre, clickscore):
    # Sets up the anime
    genrePicked = clickgenre.get()
    scorePicked = clickscore.get()
    df = pd.read_csv('anime.csv')
    listOne = df[df['genre'].str.contains(genrePicked)]
    listFinal = listOne[listOne['score'].astype(str).str[0].str.contains(scorePicked)]
    # Gets a random one out of a list
    listFinal1 = listFinal.sample()
    title = listFinal1['title'].to_string(index=False)
    genre = listFinal1['genre'].to_string(index=False)
    episode = listFinal1['episodes'].to_string(index=False)
    score = listFinal1['score'].to_string(index=False)
    # Removes the menu widgets
    animeLabel.grid_remove()
    dropdownGenre.grid_remove()
    generateButton.grid_remove()
    dropdownScore.grid_remove()
    # Initializes the new widgets
    showTitle = Label(root, text=title, font='bold')
    showGenres = Label(root, text="Genres: " + genre)
    showEpisodes = Label(root, text="Episodes: " + episode)
    showScore = Label(root, text="Score: " + score)
    againButton = Button(root, text="Again", command=lambda: again(showTitle, showGenres, showBack, showEpisodes,
                                                                   showScore, againButton, clickgenre, clickscore))
    showBack = Button(root, text="Back", command=lambda: back(showTitle, showGenres, showBack, showEpisodes, showScore,
                                                              againButton))
    # Places the new widgets
    showTitle.grid(row=0, column=1)
    showGenres.grid(row=1, column=1)
    showEpisodes.grid(row=2, column=1)
    showScore.grid(row=3, column=1)
    againButton.grid(row=4, column=0)
    showBack.grid(row=5, column=0)


# The Menu
animeLabel = Label(root, text="Random Anime Selector", font='bold')
dropdownGenre = Combobox(root, textvariable=clickedGenre, values=["Action", "Adventure", "Comedy", "Demons", "Cars",
                                                                  "Mystery", "Dementia", "Drama", "Fantasy", "Game",
                                                                  "Historical",
                                                                  "Horror", "Magic", "Ecchi", "Martial Arts", "Mecha",
                                                                  "Parody",
                                                                  "Romance", "School", "Kids", "Military", "Music",
                                                                  "Police",
                                                                  "Samurai", "Sci-Fi", "Shoujo", "Shounen", "Space",
                                                                  "Sports",
                                                                  "Super Power", "Vampire", "Yaoi", "Yuri", "Harem",
                                                                  "Hentai",
                                                                  "Slice of Life", "Supernatural", "Psychological",
                                                                  "Thriller",
                                                                  "Seinen", "Josei"])
dropdownScore = Combobox(root, textvariable=clickedScore, values=["9", "8", "7", "6", "5", "4", "3", "2", "1"])
generateButton = Button(root, command=lambda: generate(clickedGenre, clickedScore), text="Generate")

# Placing the menu widgets
animeLabel.grid(row=0, column=0, columnspan=2)
dropdownGenre.grid(row=1, columnspan=2)
dropdownScore.grid(row=2, columnspan=2)
generateButton.grid(row=3, columnspan=2)

root.mainloop()
