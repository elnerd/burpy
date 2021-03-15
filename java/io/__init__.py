try:
    from typing import Union, List, Optional
except ImportError:
    pass

class OutputStream(object):
    def close(self):
        pass
    def flush(self):
        pass
    def write(self, b, off=None, len=None):
        # type: (Union[bytearray, int], Optional[int], Optional[int]) -> ()
        pass
