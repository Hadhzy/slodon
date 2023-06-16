#: https://tronche.com/gui/x/xlib/event-handling/protocol-errors/default-handlers.html
from dataclasses import dataclass


class XError(Exception):
    """Main error class for x errors"""
    pass
