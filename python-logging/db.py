import logging

logger = logging.getLogger(__name__)


def initialize_db():
    logger.info("Initializing Database Connection...")

    # Connect to db
    logger.debug("Connecting to database: http://localhost:49493")

    logger.info("Initialized Database Connection")


class SimulatedValueError(ValueError):
    pass


def simulate_error():
    try:
        raise SimulatedValueError("SimulatedValueError raised.")
    except ValueError:
        logger.error("ValueError raised.", exc_info=True)
        logger.exception("ValueError raised.")
