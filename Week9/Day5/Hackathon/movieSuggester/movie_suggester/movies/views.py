from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Movie
import requests
from .api_keys import API_KEY


def process_response(r):
    response = {}
    r_status = r.status_code

    if r_status == 200:
        data = r.json()

        response['status'] = 200
        response['message'] = 'success'
        response['data'] = data
    else:
        response['status'] = r.status_code
        response['message'] = 'error'
        response['data'] = {}

    return Response(response)


class GetMovies(APIView):
    def get(self, request, category, page):

        r = requests.get(f'https://api.themoviedb.org/3/movie/'
                         f'{category}?language=en-US&page={page}&api_key={API_KEY}')

        return process_response(r)


class Discover(APIView):
    def get(self, request, category, page):

        r = requests.get(f'https://api.themoviedb.org/3/discover/'
                         f'{category}?include_adult=false&include_video=false&language=en-US&page='
                         f'{page}&sort_by=popularity.desc&api_key={API_KEY}')

        return process_response(r)


class Search(APIView):
    def post(self, request, category, query, page):

        r = requests.get(f'https://api.themoviedb.org/3/search/'
                         f'{category}?query={query}&include_adult=false&language=en-US&page={page}'
                         f'&api_key={API_KEY}')

        return process_response(r)


class MovieCheck(APIView):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            movie = None

        response = {}

        if movie:
            data = {
                "favorite": movie.favorite,
                "watched": movie.watched,
                "watchlist": movie.watchlist,
            }

            response['status'] = 200
            response['message'] = 'success'
            response['data'] = data
        else:
            response['status'] = 404
            response['message'] = 'error'
            response['data'] = {}

        return Response(response)


class Favorites(APIView):
    def get(self, request):
        data = Movie.objects.filter(favorite=True)

        serializer = MovieSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    # Check if the movie is already in the database
    def post(self, request):
        movie = Movie.objects.filter(movie_id=request.data.get('movie_id'))

        if len(movie) == 0:
            serializer = MovieSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if movie[0].favorite:
                movie[0].favorite = False
            else:
                movie[0].favorite = True

            movie[0].save()

            return Response(status=status.HTTP_201_CREATED)


class Watched(APIView):
    def get(self, request):
        data = Movie.objects.filter(watched=True)

        serializer = MovieSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    # Check if the movie is already in the database
    def post(self, request):
        movie = Movie.objects.filter(movie_id=request.data.get('movie_id'))

        if len(movie) == 0:
            serializer = MovieSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if movie[0].watched:
                movie[0].watched = False
            else:
                movie[0].watched = True

            movie[0].save()

            return Response(status=status.HTTP_201_CREATED)


class Watchlist(APIView):
    def get(self, request):
        data = Movie.objects.filter(watchlist=True)

        serializer = MovieSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    # Check if the movie is already in the database
    def post(self, request):
        movie = Movie.objects.filter(movie_id=request.data.get('movie_id'))

        if len(movie) == 0:
            serializer = MovieSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if movie[0].watchlist:
                movie[0].watchlist = False
            else:
                movie[0].watchlist = True

            movie[0].save()

            return Response(status=status.HTTP_201_CREATED)
