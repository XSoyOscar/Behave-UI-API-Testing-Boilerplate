import logging
from utils.config import Config


def setup_logger():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_file = "test_execution.log"

    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format=log_format,
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )

    return logging.getLogger(__name__)


logger = setup_logger()
