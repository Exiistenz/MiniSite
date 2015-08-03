from django.contrib import admin
from core.models import Categorie, Article, Contact

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'cut_content')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre', ), }
    fieldsets = (('Général', {
        'fields': ('titre', 'slug', 'auteur', 'categorie')
	    }),
	    # Fieldset 2 : contenu de l'article
	    ('Contenu de l\'article', {
	       'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
	       'fields': ('contenu', )
	    }),
	)

    def cut_content(self, article):
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    cut_content.short_description = 'Aperçu du contenu'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Contact)