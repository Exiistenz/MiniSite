from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.shortcuts import render, get_object_or_404

from core.models import Article, Categorie, Contact
from core.forms import ContactForm
from django.views.generic import TemplateView
from django.views.generic import ListView

from core.forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  #@login_required before function


#
#
#   Class Article
#
#
# def view_article(request, id_article, slug):
def view_article(request, id_article):
    """ Affiche un article en fonction de l'id. """
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'core/view_article.html', {'article': article})


#
#
#   Class Contact
#
#
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 

        if form.is_valid(): 
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            envoi = True

    else: 
        form = ContactForm()  

    return render(request, 'core/contact.html', locals())

def new_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'core/contact.html', locals())

#
#
#   Class Faq
#
#
class FAQView(TemplateView):
   template_name = "core/faq.html" 

def faq(request):
    return render(request, 'core/faq.html', {})

#
#
#   Class View
#
#
class ListArticles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "core/home.html"
    paginate_by = 10
    # queryset = Article.objects.filter(categorie__id=1)

    # def get_queryset(self):
        # return Article.objects.filter(categorie__id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(ListArticles, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class ListContacts(ListView):
    model = Contact
    context_object_name = "contacts"
    template_name = "core/view_contacts.html"
    paginate_by = 5
    # queryset = Article.objects.filter(categorie__id=1)

    # def get_queryset(self):
        # return Article.objects.filter(categorie__id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(ListContacts, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context

#
#
# Connexion
#
#
def connect(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: 
                login(request, user) 
            else: 
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'core/login.html', locals())

def disconnect(request):
    logout(request)
    return redirect(reverse(login))