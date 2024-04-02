from TweeterHateSpeech.logger import logging
from TweeterHateSpeech.exception import CustomException
import sys

logging.info("Welcome to Project")
try:
    a=7/0
except Exception as e:
    raise CustomException(e,sys)