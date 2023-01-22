import os
import django

os.environ["DJANGO_SETTINGs_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import Movie, Rating

# new_movie = Movie(name="arr",duration_min=122,description="ghjjjjjj",release_year=2000)
# new_movie.save()
#
#
# all_movies = Movie.objects.all()
# for movie in all_movies:
#     Rating(movie=movie,rating=3.4).save()

movie = Movie.get