import fresh_tomatoes
import media

#This file holds the information for 'instances' of Class Movie (located in media.py)


the_replacements = media.Movie("The Replacements",
                               "The NFL on Strike",
                               "http://ts1.mm.bing.net/th?id=HN.607988007446447616&pid=1.7",
                               "https://www.youtube.com/watch?v=QNpb9H703tg",
                               "118 minutes",
                               "PG-13",
                               "Howard Duetch",
                               "8/11/2000")

sherlock_holmes = media.Movie("Sherlock Holmes",
                              "A comical detective story",
                              "http://antiscribe.files.wordpress.com/2011/12/sherlock-holmes-movie-poster.jpg",
                              "https://www.youtube.com/watch?v=I0hXhGt5XPg",
                              "128 minutes",
                              "PG-13",
                              "Guy Ritchie",
                              "12/25/2009")

school_of_rock = media.Movie("School of Rock",
                             "Life lessons taught through music",
                             "http://www.movieposter.com/posters/archive/main/16/MPW-8303",
                             "https://www.youtube.com/watch/v=3PsUJFEBC74",
                             "108 minutes",
                             "PG-13",
                             "Richard Linklater",
                             "10/3/2003")

the_proposal = media.Movie("The Proposal",
                           "A enterprising man promises to marry his boss to keep her in the country",
                           "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra900/a958/a95843kyn51.jpg",
                           "https://www.youtube.com/watch?v=cVAEPPQfJ8I",
                           "118 minutes",
                           "PG-13",
                           "Ann Fletcher",
                           "6/19/2009")

couples_retreat = media.Movie("Couples Retreat",
                              "A group of friends go to marriage counseling on a tropical island",
                              "http://1.bp.blogspot.com/_kwPXnZqnoSc/S3WIuXCOFHI/AAAAAAAAAUg/6cajwzduGQQ/Couples-Retreat-poster.jpg",
                              "https://www.youtube.com/watch?v=-s-DjmXYEZQ",
                              "114 minutes",
                              "PG-13",
                              "Peter Billingsley",
                              "10/9/2009")

american_sniper = media.Movie("American Sniper",
                              "Action packed thriller",
                              "http://ts4.mm.bing.net/th?id=HN.608002902398406511&pid=1.7",
                              "https://www.youtube.com/watch?v=99k3u9ay1gs",
                              "132 minutes",
                              "R",
                              "Clint Eastwood",
                              "11/11/2014")

#Array to feed movie list into fresh_tomatoes()
movies = [the_replacements, sherlock_holmes, school_of_rock, the_proposal, couples_retreat, american_sniper] 


fresh_tomatoes.open_movies_page(movies)

