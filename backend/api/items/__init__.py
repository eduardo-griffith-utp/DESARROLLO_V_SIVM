import logging
import django

logger = logging.getLogger(__name__)

try:
    django.setup()
    logger.info("Django setup")
except Exception as e:
    logger.warning("Django fallo setup: %s", e)