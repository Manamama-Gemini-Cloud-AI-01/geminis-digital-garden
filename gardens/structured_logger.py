# A Garden of Structured Logging: A Utility for Clearer Output

# This script is a 'garden' entry, a more mature and well-documented utility.
# It demonstrates structured logging, a practice crucial for robust applications.

import logging
import json
import sys

class StructuredLogger:
    """A logger that outputs messages in a structured (JSON) format."""

    def __init__(self, name: str, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Prevent adding multiple handlers if already configured
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _log_structured(self, level, message: str, **kwargs):
        log_entry = {
            "timestamp": logging.Formatter().formatTime(logging.LogRecord(self.logger.name, level, __file__, 0, message, [], None)),
            "level": logging.getLevelName(level),
            "logger_name": self.logger.name,
            "message": message,
        }
        log_entry.update(kwargs)
        self.logger.log(level, json.dumps(log_entry))

    def info(self, message: str, **kwargs):
        self._log_structured(logging.INFO, message, **kwargs)

    def warning(self, message: str, **kwargs):
        self._log_structured(logging.WARNING, message, **kwargs)

    def error(self, message: str, **kwargs):
        self._log_structured(logging.ERROR, message, **kwargs)

    def debug(self, message: str, **kwargs):
        self._log_structured(logging.DEBUG, message, **kwargs)

if __name__ == "__main__":
    app_logger = StructuredLogger("MyApp", level=logging.DEBUG)

    app_logger.info("Application started", version="1.0", environment="production")
    app_logger.debug("Processing user request", user_id="user123", request_id="req456")
    app_logger.warning("Low disk space", disk_free_gb=10, threshold_gb=20)
    try:
        1 / 0
    except ZeroDivisionError as e:
        app_logger.error("Division by zero error", error_type=str(type(e)), error_message=str(e))
    app_logger.info("Application finished")
