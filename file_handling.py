import os, atexit
from tempfile import NamedTemporaryFile

class FileHandler():

    def __init__(self):
        self.file = NamedTemporaryFile()
        # register function called when quit
        atexit.register(self._cleanup)

    def write_into(self, btext):
        self.file.write(btext)

    def _cleanup(self):
        # because self.file has been created without delete=False, closing the file causes its deletion
        self.file.close()

# create new instance and do whatever you need
fh = FileHandler()
fh.write_into(b'Hi happy developer!')