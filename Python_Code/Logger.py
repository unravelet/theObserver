import logging

class Logger:
    logger = ""

    def __init__(self, context: str):
        self.logger = logging.getLogger(context)
        self.logger.setLevel(logging.DEBUG)

        loggingFormat = logging.Formatter(f'%(asctime)s - {context} - %(levelname)s - %(message)s')

        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)
        c_handler.setFormatter(loggingFormat)
        self.logger.addHandler(c_handler)

        f_handler = logging.FileHandler('file.log')
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(loggingFormat)
        self.logger.addHandler(f_handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)
