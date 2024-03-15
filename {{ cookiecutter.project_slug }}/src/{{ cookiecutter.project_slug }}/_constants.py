import os


class SystemDefs:
    LOGGING_FILE_PATH = os.path.join("logging", "log.log")
    os.makedirs(os.path.dirname(LOGGING_FILE_PATH), exist_ok=True)
