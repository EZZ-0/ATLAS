"""
CENTRALIZED LOGGING MODULE
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional
import warnings
warnings.filterwarnings('ignore')


class EngineLogger:
    _loggers = {}
    
    @staticmethod
    def setup_logger(name: str = "AtlasEngine", log_level: str = "INFO", 
                     log_to_file: bool = True, log_to_console: bool = True, 
                     log_dir: str = "logs") -> logging.Logger:
        if name in EngineLogger._loggers:
            return EngineLogger._loggers[name]
        
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        
        if logger.hasHandlers():
            logger.handlers.clear()
        
        formatter = logging.Formatter(
            fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        if log_to_file:
            log_path = Path(log_dir)
            log_path.mkdir(parents=True, exist_ok=True)
            log_file = log_path / f"{name.lower()}.log"
            file_handler = RotatingFileHandler(
                filename=log_file, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8'
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        if log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.WARNING)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        EngineLogger._loggers[name] = logger
        return logger
    
    @staticmethod
    def get_logger(name: str = "AtlasEngine") -> logging.Logger:
        if name in EngineLogger._loggers:
            return EngineLogger._loggers[name]
        return EngineLogger.setup_logger(name)
    
    @staticmethod
    def log_security_event(event_type: str, details: str, severity: str = "WARNING"):
        logger = EngineLogger.get_logger("SecurityLog")
        log_method = getattr(logger, severity.lower(), logger.warning)
        log_method(f"[{event_type}] {details}")


def get_logger(name: str = "AtlasEngine") -> logging.Logger:
    return EngineLogger.get_logger(name)

def log_error(message: str, exception: Optional[Exception] = None, logger_name: str = "AtlasEngine"):
    logger = EngineLogger.get_logger(logger_name)
    if exception:
        logger.error(f"{message}: {str(exception)}", exc_info=True)
    else:
        logger.error(message)

def log_warning(message: str, logger_name: str = "AtlasEngine"):
    logger = EngineLogger.get_logger(logger_name)
    logger.warning(message)

def log_info(message: str, logger_name: str = "AtlasEngine"):
    logger = EngineLogger.get_logger(logger_name)
    logger.info(message)
