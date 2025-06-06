# src/itcity/bandi/browser/bando_view.py

from plone.dexterity.browser.view import DefaultView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BandoView(DefaultView):
    """Vista personalizzata per il content type Bando"""
    
    template = ViewPageTemplateFile("templates/bando_view.pt")
    
    def __call__(self):
        return self.template()
    
    def get_tipologia_display(self):
        """Restituisce il titolo della tipologia per la visualizzazione"""
        if hasattr(self.context, 'tipologia_bando') and self.context.tipologia_bando:
            vocabulary = self.context.portal_vocabularies.getVocabularyByName(
                'itcity.bandi.tipologie_bando'
            )
            try:
                term = vocabulary.getTerm(self.context.tipologia_bando)
                return term.title
            except KeyError:
                return self.context.tipologia_bando
        return ""
    
    def get_destinatari_display(self):
        """Restituisce i titoli dei destinatari per la visualizzazione"""
        if hasattr(self.context, 'destinatari') and self.context.destinatari:
            vocabulary = self.context.portal_vocabularies.getVocabularyByName(
                'itcity.bandi.destinatari_bando'
            )
            titles = []
            for value in self.context.destinatari:
                try:
                    term = vocabulary.getTerm(value)
                    titles.append(term.title)
                except KeyError:
                    titles.append(value)
            return titles
        return []
    
    def get_enti_display(self):
        """Restituisce i titoli degli enti per la visualizzazione"""
        if hasattr(self.context, 'ente') and self.context.ente:
            vocabulary = self.context.portal_vocabularies.getVocabularyByName(
                'itcity.bandi.enti_bando'
            )
            titles = []
            for value in self.context.ente:
                try:
                    term = vocabulary.getTerm(value)
                    titles.append(term.title)
                except KeyError:
                    titles.append(value)
            return titles
        return []