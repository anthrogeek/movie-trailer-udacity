
import fresh_tomatoes
import media

"""List of movie objects that the Fresh Tomatoes application uses to pull 
in the relevant movie information. We list the title, storyline, 
poster image URL, trailer URL.
"""

fried_green_tomatoes = media.Movie("Fried Green Tomatoes", 
								   "A story of Tuwanda", 
								   "https://upload.wikimedia.org/wikipedia/en/6/6e/Fried_Green_Tomatoes_%28poster%29.jpg", 
								   "https://youtu.be/o5hb5mc-dfI")

avatar = media.Movie("Avatar", 
					 "A marine on an alien planet", 
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

being_john_malkovich = media.Movie("Being John Malkovich", 
								   "A portal into another's mind", 
								   "https://upload.wikimedia.org/wikipedia/en/5/55/Being_John_Malkovich_poster.jpg", 
								   "https://youtu.be/2UuRFr0GnHM")

school_of_rock = media.Movie("School of Rock", 
							 "Using Rock Music to Learn", 
							 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
							 "https://youtu.be/3PsUJFEBC74")

notting_hill = media.Movie("Notting Hill", 
						   "A story of a boy asking her to love him", 
						   "https://upload.wikimedia.org/wikipedia/en/3/38/NottingHillRobertsGrant.jpg", 
						   "https://youtu.be/h_daSz5FZYs")

little_miss_sunshine = media.Movie("Little Miss Sunshine", 
								   "Don't give up on your dreams", 
								   "https://upload.wikimedia.org/wikipedia/en/1/16/Little_miss_sunshine_poster.jpg", 
								   "https://www.youtube.com/watch?v=wvwVkllXT80")

midnight_in_paris = media.Movie("Midnight in Paris", 
								"Going back in time to meet authors", 
								"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
								"https://youtu.be/wuOUdZjuCIA")

hunger_games = media.Movie("Hunger Games", 
						   "A really real reality show", 
						   "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", 
						   "https://youtu.be/KmYNkasYthg")

a_league_of_their_own = media.Movie("A League of Their Own", 
									"Women's professional baseball league back in the day", 
									"https://upload.wikimedia.org/wikipedia/en/5/5f/League_of_their_own_ver2.jpg", 
									"https://www.youtube.com/watch?v=tkZTcofj3wU")

"""Loads the list of movies. 

The position of the movies on the fresh_tomatoes.html page is determined 
by their position in this list.
"""

movies = [fried_green_tomatoes, avatar, being_john_malkovich, 
a_league_of_their_own, notting_hill, little_miss_sunshine,
school_of_rock, midnight_in_paris, hunger_games]

"""Creates the fresh_tomatoes HTML page.

Runs the open_movies_page function from the 
fresh_tomatoes file and passes the movies list into the function
"""
fresh_tomatoes.open_movies_page(movies)

