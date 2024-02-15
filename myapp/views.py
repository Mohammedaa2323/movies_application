from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Movie

from django import forms

# Create your views here.

class MovieForm(forms.Form):

    name=forms.CharField()
    language=forms.CharField()
    run_time=forms.IntegerField()
    genre=forms.CharField()
    director=forms.CharField()
    year=forms.IntegerField()
    actors=forms.CharField()








# (!) to list one the movies only id will change id=1 id=2 etc changing in views

class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})

# (2) to list one movies with using id
    
class MoviedetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    

# (3) to delect movie details
    
class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")
    

# to create form in html page
    
class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MovieForm()
        return render(request,"movie_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Movie.objects.create(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form})
        # data={k:v for k,v in request.POST.items()}
        # data.pop("csrfmiddlewaretoken")
        # Movie.objects.create(**data)
        # return redirect("movie-list")


class MovieupdateView(View):
    def get(self,request,*args,**kwargs):    
        id=kwargs.get("pk")
        movie_objects=Movie.objects.get(id=id)
        data={
            "name":movie_objects.name,
            "language":movie_objects.language,
            "run_time":movie_objects.run_time,
            "genre":movie_objects.genre,
            "director":movie_objects.director,
            "year":movie_objects.year,
            "actors":movie_objects.actors
        }
        form=MovieForm(initial=data)
        return render(request,"movie_edit.html",{"form":form})


    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Movie.objects.filter(id=id).update(**data)
            return redirect("movie-list")
        else:
         return render(request,"movie_edit.html",{"form":form})