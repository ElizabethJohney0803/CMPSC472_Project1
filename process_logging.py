
import logging

logging.basicConfig(filename='process_manager.log', level=logging.INFO)

def log_event(event):
    logging.info(event)
