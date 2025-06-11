# src/itcity/bandi/content/bando.py

from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema import Email
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer, invariant, Invalid
from datetime import datetime, time
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
        description=_("Data e ora dell'apertura del bando. Usa questo campo se vuoi impostare una data di apertura specifica. Se non impostato, il bando sarà aperto immediatamente."),
        required=False,
    )
    
    termine_chiarimenti = schema.Datetime(
        title=_("Termine per la richiesta di chiarimenti"),
        description=_("Data entro la quale sarà possibile far pervenire domande e richieste di chiarimento a chi eroga il bando"),
        required=False,
    )
    
    data_scadenza = schema.Datetime(
        title=_("Data e ora di scadenza"),
        description=_("Scadenza dei termini per partecipare al bando"),
        required=False,
    )
    
    data_chiusura_procedimento = schema.Date(
        title=_("Data chiusura procedimento"),
        description=_("Data di chiusura del procedimento"),
        required=False,
    )
    
    ulteriori_informazioni = RichText(
        title=_("Ulteriori informazioni"),
        description=_("Ulteriori informazioni non previste negli altri campi; si può trattare di contatti o note informative la cui conoscenza è indispensabile per la partecipazione al bando"),
        required=False,
    )
    
    note_aggiornamento = schema.Text(
        title=_("Note di aggiornamento"),
        description=_("Inserisci una nota per indicare che il contenuto corrente è stato aggiornato. Questo testo può essere visualizzato nei blocchi elenco con determinati layout per informare gli utenti che un determinato contenuto è stato aggiornato. Ad esempio se in un bando sono stati aggiunti dei documenti."),
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

    @invariant
    def validate_date_order(data):
        d_apertura = data.data_apertura
        d_chiarimenti = data.termine_chiarimenti
        d_scadenza = data.data_scadenza
        d_chiusura = data.data_chiusura_procedimento

        # Converti la data di chiusura in datetime (aggiungendo mezzanotte)
        if d_chiusura:
            d_chiusura_dt = datetime.combine(d_chiusura, time.min)
        else:
            d_chiusura_dt = None

        if d_apertura and d_chiarimenti:
            if d_apertura > d_chiarimenti:
                raise Invalid(
                    _("La data di apertura deve essere precedente o uguale al termine per la richiesta di chiarimenti.")
                )

        if d_scadenza:
            if d_chiarimenti and d_scadenza <= d_chiarimenti:
                raise Invalid(
                    _("La data di scadenza deve essere successiva al termine per la richiesta di chiarimenti.")
                )
            if d_apertura and d_scadenza <= d_apertura:
                raise Invalid(
                    _("La data di scadenza deve essere successiva alla data di apertura.")
                )

        if d_chiusura_dt:
            if d_apertura and d_chiusura_dt <= d_apertura:
                raise Invalid(
                    _("La data di chiusura del procedimento deve essere successiva alla data di apertura.")
                )
            if d_chiarimenti and d_chiusura_dt <= d_chiarimenti:
                raise Invalid(
                    _("La data di chiusura del procedimento deve essere successiva al termine per la richiesta di chiarimenti.")
                )
            if d_scadenza and d_chiusura_dt <= d_scadenza:
                raise Invalid(
                    _("La data di chiusura del procedimento deve essere successiva alla data di scadenza.")
                )


@implementer(IBando)
class Bando(Container):
    """Content type Bando"""
    
    portal_type = "Bando"