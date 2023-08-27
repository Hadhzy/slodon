import logging

slodon_logger = logging.getLogger("slodonixlogger")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler = logging.FileHandler("slodon.log")
handler.setFormatter(formatter)
slodon_logger.addHandler(handler)
