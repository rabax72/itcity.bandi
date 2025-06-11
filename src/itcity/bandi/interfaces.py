# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IItcityBandiLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


from zope.interface import Interface, invariant, Invalid
from zope import schema


class IBando(Interface):
    data_apertura = schema.Datetime(
        title=u"Data di apertura",
        required=False,
    )

    data_chiarimenti = schema.Datetime(
        title=u"Data per la richiesta di chiarimenti",
        required=False,
    )

    data_scadenza = schema.Datetime(
        title=u"Data e ora di scadenza",
        required=False,
    )

    data_chiusura = schema.Datetime(
        title=u"Data di chiusura del procedimento",
        required=False,
    )

    @invariant
    def validate_date_order(data):
        d_apertura = data.data_apertura
        d_chiarimenti = data.data_chiarimenti
        d_scadenza = data.data_scadenza
        d_chiusura = data.data_chiusura

        if d_apertura and d_chiarimenti:
            if d_apertura > d_chiarimenti:
                raise Invalid(u"La data di apertura deve essere precedente o uguale alla data per la richiesta di chiarimenti.")

        if d_scadenza:
            if d_chiarimenti and d_scadenza <= d_chiarimenti:
                raise Invalid(u"La data di scadenza deve essere successiva alla data per la richiesta di chiarimenti.")
            if d_apertura and d_scadenza <= d_apertura:
                raise Invalid(u"La data di scadenza deve essere successiva alla data di apertura.")

        if d_chiusura:
            if d_apertura and d_chiusura <= d_apertura:
                raise Invalid(u"La data di chiusura deve essere successiva alla data di apertura.")
            if d_chiarimenti and d_chiusura <= d_chiarimenti:
                raise Invalid(u"La data di chiusura deve essere successiva alla data per la richiesta di chiarimenti.")
            if d_scadenza and d_chiusura <= d_scadenza:
                raise Invalid(u"La data di chiusura deve essere successiva alla data di scadenza.")
