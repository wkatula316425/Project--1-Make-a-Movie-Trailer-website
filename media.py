import webbrowser

#Class for the Movie Trailer Website

class Movie():
        
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,movie_length, movie_rating, movie_director, movie_release):
         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = trailer_youtube
         self.movie_length = movie_length
         self.movie_rating = movie_rating
         self.movie_director = movie_director
         self.movie_release = movie_release
         

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
