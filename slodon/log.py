# RUN THIS SCRIPT IF YOU WANT TO SEE LOGS, DO NOT PUSH IT TO THE REPO.
# TODO: DEFINE THE LOGGING SYSTEM WHICH HELPS UNDERSTAND THE INTERACTIONS
import logging
import sys

file_path = sys.argv[1]

logging.basicConfig(filename=file_path or "slodon.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

