# src/itcity/bandi/vocabularies.py

from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from itcity.bandi import _


@implementer(IVocabularyFactory)
class TipologieBandoVocabulary:
    """Vocabolario per le tipologie di bando"""
    
    def __call__(self, context):
        terms = [
            SimpleTerm(value="servizi", title=_("Servizi")),
            SimpleTerm(value="forniture", title=_("Forniture")),
            SimpleTerm(value="lavori", title=_("Lavori")),
            SimpleTerm(value="alienazioni", title=_("Alienazioni")),
            SimpleTerm(value="avvisi_pubblici", title=_("Avvisi pubblici")),
            SimpleTerm(value="concorso", title=_("Concorso")),
        ]
        return SimpleVocabulary(terms)


@implementer(IVocabularyFactory)
class DestinatariBandoVocabulary:
    """Vocabolario per i destinatari del bando"""
    
    def __call__(self, context):
        terms = [
            SimpleTerm(value="cittadini", title=_("Cittadini")),
            SimpleTerm(value="imprese", title=_("Imprese")),
            SimpleTerm(value="enti_locali", title=_("Enti locali")),
            SimpleTerm(value="associazioni", title=_("Associazioni")),
            SimpleTerm(value="altro", title=_("Altro")),
        ]
        return SimpleVocabulary(terms)


@implementer(IVocabularyFactory)
class EntiBandoVocabulary:
    """Vocabolario per gli enti del bando"""
    
    def __call__(self, context):
        terms = [
            SimpleTerm(value="authority_stu", title=_("Authority Stu")),
            SimpleTerm(value="comune_di_parma", title=_("Comune di Parma")),
            SimpleTerm(value="itcity_spa", title=_("It.City s.p.a.")),
            SimpleTerm(value="parma_infrastrutture", title=_("Parma Infrastrutture")),
            SimpleTerm(value="regione_emilia_romagna", title=_("Regione Emilia Romagna")),
        ]
        return SimpleVocabulary(terms)


# Factory instances
tipologie_bando_vocabulary = TipologieBandoVocabulary()
destinatari_bando_vocabulary = DestinatariBandoVocabulary()
enti_bando_vocabulary = EntiBandoVocabulary()