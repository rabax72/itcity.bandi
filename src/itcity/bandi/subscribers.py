from zope.lifecycleevent.interfaces import IObjectAddedEvent
from zope.component import adapter
from plone.dexterity.interfaces import IDexterityContent
from plone.api import content
import logging

logger = logging.getLogger(__name__)

@adapter(IDexterityContent, IObjectAddedEvent)
def create_subfolders_for_bando(obj, event):
    if obj.portal_type != "Bando":
        return

    # Evita duplicazioni se già presenti
    existing_ids = obj.objectIds()

    folder_titles = [
        ("allegati", "Allegati"),
        ("comunicazioni", "Comunicazioni"),
        ("esiti", "Esiti"),
        ("collegamenti", "Collegamenti"),
    ]

    for folder_id, folder_title in folder_titles:
        if folder_id not in existing_ids:
            content.create(
                container=obj,
                type='Folder',
                id=folder_id,
                title=folder_title
            )
            logger.info(f"Cartella '{folder_title}' creata sotto '{obj.id}'")
