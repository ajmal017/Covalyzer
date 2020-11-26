import logging
import logging.handlers as handlers

class LoggingData:
	def __init__(self, name, filename, loglevel):
		self.logger = logging.getLogger(name)
		self.logger.setLevel(loglevel)
		self.formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)-8s [%(filename)-25s:%(lineno)-03d] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

		self.fh = handlers.TimedRotatingFileHandler(filename, when="midnight", interval=1,)
		self.fh.setFormatter(self.formatter)
		self.fh.setLevel(loglevel)
		self.logger.addHandler(self.fh)

		self.ch = logging.StreamHandler()
		self.ch.setFormatter(self.formatter)
		self.ch.setLevel(loglevel)
		self.logger.addHandler(self.ch)

		self.error_info = False

	def shutdown(self):
		self.fh.close()
		self.logger.removeHandler(self.fh)
		self.ch.close()
		self.logger.removeHandler(self.ch)

	def set_error(self):
		self.error_info = True

	def has_error(self):
		return self.error_info

	def set_level(self, debug):
		loglevel = logging.DEBUG if debug else logging.INFO

		self.fh.setLevel(loglevel)
		self.ch.setLevel(loglevel)
