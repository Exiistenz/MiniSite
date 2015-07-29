from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

def home():
	return

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    return HttpResponse('<h1>Mon article ici</h1>')

# def view_redirection(request):
#     return HttpResponse("Vous avez été redirigé.")

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)