# src/itcity/bandi/__init__.py

import logging
from zope.i18nmessageid import MessageFactory

logger = logging.getLogger('itcity.bandi')
_ = MessageFactory('itcity.bandi')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""