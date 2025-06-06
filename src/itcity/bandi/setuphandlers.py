# src/itcity/bandi/setuphandlers.py

import logging
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

logger = logging.getLogger(__name__)


@implementer(INonInstallable)
class HiddenProfiles:
    """Hide profiles from the add-ons control panel."""

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from Plone's add-on control panel."""
        return [
            'itcity.bandi:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    logger.info("itcity.bandi: Post install script completed")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    logger.info("itcity.bandi: Uninstall script completed")