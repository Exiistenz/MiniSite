from django.conf.urls import patterns, url
from core.models import Article, Categorie, Contact
from django.views.generic import ListView
from core.views import FAQView 
from core.views import ListArticles, ListContacts

urlpatterns = patterns('core.views',
	url(r'^$', ListArticles.as_view(), name="core_articles"),
	url(r'^article/(\d+)$', 'view_article'),
	url(r'categorie/(?P<id>\d+)', ListArticles.as_view(), name='core_categories'),

	url(r'^contact/$', 'contact'),
	url(r'^contacts/$', ListContacts.as_view(), name="core_contacts"),

	url(r'^faq$', FAQView.as_view()),
)