import logging
from logging.handlers import RotatingFileHandler


def init_logging_configurations(tenant, model):
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s --- %(message)-100s (%(name)s:%(lineno)d)")

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_name = f"{tenant}_{model}.log"

    file_handler = RotatingFileHandler(file_name)
    file_handler.backupCount = 3
    file_handler.maxBytes = 10000   # ~ 10kb
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)
