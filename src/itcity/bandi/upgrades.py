# src/itcity/bandi/upgrades.py

from plone import api
import logging

logger = logging.getLogger(__name__)


def upgrade_to_1001(context):
    """Upgrade to version 1001"""
    logger.info("Running upgrade to 1001")
    
    # Esempio: aggiorna il catalog se necessario
    catalog = api.portal.get_tool('portal_catalog')
    catalog.refreshCatalog()
    
    logger.info("Upgrade to 1001 completed")