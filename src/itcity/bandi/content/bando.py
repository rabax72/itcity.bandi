# src/itcity/bandi/content/bando.py

from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema import Email
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from itcity.bandi import _


class IBando(model.Schema):
    """Schema per il content type Bando"""
    
    # Titolo (eredita da IDublinCore)
    
    # Descrizione (eredita da IDublinCore)
    
    testo = RichText(
        title=_("Testo"),
        description=_("Testo completo del bando"),
        required=False,
    )
    
    tipologia_bando = schema.Choice(
        title=_("Tipologia di Bando"),
        description=_("Seleziona la tipologia del bando"),
        vocabulary="itcity.bandi.tipologie_bando",
        required=True,
    )
    
    destinatari = schema.Set(
        title=_("Destinatari"),
        description=_("Seleziona i destinatari del bando"),
        value_type=schema.Choice(vocabulary="itcity.bandi.destinatari_bando"),
        required=False,
    )
    
    ente = schema.Set(
        title=_("Ente"),
        description=_("Seleziona gli enti coinvolti"),
        value_type=schema.Choice(vocabulary="itcity.bandi.enti_bando"),
        required=False,
    )
    
    data_apertura = schema.Datetime(
        title=_("Data di apertura"),
        description=_("Data e ora di apertura del bando"),
        required=False,
    )
    
    termine_chiarimenti = schema.Datetime(
        title=_("Termine per la richiesta di chiarimenti"),
        description=_("Data e ora limite per richiedere chiarimenti"),
        required=False,
    )
    
    data_scadenza = schema.Datetime(
        title=_("Data e ora di scadenza"),
        description=_("Data e ora di scadenza del bando"),
        required=False,
    )
    
    data_chiusura_procedimento = schema.Date(
        title=_("Data chiusura procedimento"),
        description=_("Data di chiusura del procedimento"),
        required=False,
    )
    
    ulteriori_informazioni = RichText(
        title=_("Ulteriori informazioni"),
        description=_("Informazioni aggiuntive sul bando"),
        required=False,
    )
    
    note_aggiornamento = schema.Text(
        title=_("Note di aggiornamento"),
        description=_("Note relative agli aggiornamenti del bando"),
        required=False,
    )
    
    immagine_anteprima = NamedBlobImage(
        title=_("Immagine di anteprima"),
        description=_("Immagine rappresentativa del bando"),
        required=False,
    )
    
    didascalia_immagine = schema.TextLine(
        title=_("Didascalia immagine di anteprima"),
        description=_("Didascalia per l'immagine di anteprima"),
        required=False,
    )


@implementer(IBando)
class Bando(Container):
    """Content type Bando"""
    
    portal_type = "Bando"