from logging import Logger
import requests
import json

class ops_tracker(Logger):

    def __init__(self, id, tracker_address, project=None):
        self.id = id
        self.project = project
        self.tracker_address = tracker_address

    ### Utils ###

    def generateTimestamp(self):
        return
    
    def sendCall(self, level, timestamp):
        payload = {
            "id": self.id,
            "project": self.project,
            "level": level,
            "timestamp": timestamp
        }

        r = requests.put(url=self.tracker_address, data=json.dumps(payload))
        print("Status code: ", r.status_code)
        print("Resp: ", r.text)

    ### Trackers ###

    def debug(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='DEBUG', timestamp=timestamp)
        super.debug(msg=message, *args, **kwargs)

    def info(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='INFO', timestamp=timestamp)
        super.info(message, *args, **kwargs)

    def warning(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='WARNING', timestamp=timestamp)
        super.warning(message, *args, **kwargs)
    
    def warning(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='WARNING', timestamp=timestamp)
        super.warning(message, *args, **kwargs)

    def error(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='ERROR', timestamp=timestamp)
        super.error(message, *args, **kwargs)

    def critical(self, message=None, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='CRITICAL', timestamp=timestamp)
        super.critical(message, *args, **kwargs)

    def start(self, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='START', timestamp=timestamp)

    def end(self, *args, **kwargs):
        timestamp = self.generateTimestamp()
        self.sendCall(level='END', timestamp=timestamp)

    
