from plugin import plugin, require
from bs4 import BeautifulSoup
from security import safe_requests

valid_genres = [
    "comedy",
    "sci-fi",
    "horror",
    "romance",
    "action",
    "thriller",
    "drama",
    "mystery",
    "crime",
    "animation",
    "adventure",
    "fantasy",
    "comedy,romance",
    "action,comedy",
    "superhero",
]


@require(network=True)
@plugin("topmedia")
class topmedia:
    """
    Plugin to extract most popular movies and TV shows from IMDB by genre
    """

    def __call__(self, jarvis, medium):
        valid_mediums = ["tv", "movies", "television", "movie", "cinema"]
        medium = medium.lower()

        if medium not in valid_mediums:
            jarvis.say(
                "Please run the command with a valid medium.\n Valid inputs: topmedia tv, topmedia movies"
            )
        else:
            for i in range(len(valid_genres)):
                jarvis.say(str(i + 1) + "." + " " + valid_genres[i])
            # .lower() to take care of accidental capitalisations
            # ? Might be useful to allow the user to choose a genre by number.
            # ? For example, if a user enters 1, we direct the user to top comedy i.e. valid_genres[0] movies
            user_genre = jarvis.input(
                "\nPlease choose a genre from one of the genres above: You can enter either the genre name (e.g. comedy) or the number (e.g. 1 for comedy)\n\n"
            ).lower()
            flag = True
            if user_genre.isdigit():
                user_genre = self.conv_num(jarvis, user_genre)

            elif user_genre not in valid_genres:
                jarvis.say(
                    "The genre you have entered is not valid.\nPlease try again."
                )
                flag = False
            # else:  # the medium is already validated, so it's either tv or movie
            if flag:
                jarvis.say(
                    "\nNow displaying top 250 " + user_genre + "medium on IMDB \n\n"
                )
                if medium == "tv" or medium == "television":
                    self.top_250_extractor(jarvis, user_genre, "tv")
                else:
                    self.top_250_extractor(jarvis, user_genre, "movie")

    def top_250_extractor(self, jarvis, genre, medium):
        if medium == "tv":
            title_type = "tvSeries"
        else:
            title_type = "movie"
            # Each page on IMDB contains 50 movies. So, start = 1 implies movies ranked 1-50.
        for start in [1, 51, 101, 151, 201]:
            url = (
                "https://www.imdb.com/search/title/?genres="
                + genre
                + "&start="
                + str(start)
                + "&explore=title_type,genres&title_type="
                + title_type
            )
            r = safe_requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            table = soup.find("div", attrs={"class": "lister-list"})
            i = 0
            for row2 in table.findAll("h3", attrs={"class": "lister-item-header"}):
                # Printing rank and name of the movie/show.
                jarvis.say(
                    str(start + i) + ". " + row2.a.text
                )  # The a tag has the name of the movie/show
                i += 1

    # function to convert number to valid genres
    def conv_num(self, jarvis, input_genre):
        if input_genre == "1":
            return "comedy"
        elif input_genre == "2":
            return "sci-fi"
        elif input_genre == "3":
            return "horror"
        elif input_genre == "4":
            return "romance"
        elif input_genre == "5":
            return "action"
        elif input_genre == "6":
            return "thriller"
        elif input_genre == "7":
            return "drama"
        elif input_genre == "8":
            return "mystery"
        elif input_genre == "9":
            return "crime"
        elif input_genre == "10":
            return "animation"

        elif input_genre == "11":
            return "adventure"

        elif input_genre == "12":
            return "fantasy"

        elif input_genre == "13":
            return "comedy,romance"
        elif input_genre == "14":
            return "action,comedy"

        elif input_genre == "15":
            return "superhero"
