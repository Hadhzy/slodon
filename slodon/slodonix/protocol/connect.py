# Inspired by: https://github.com/python-xlib/python-xlib/blob/master/Xlib/support/unix_connect.py
import socket
from slodon.slodonix.errors import *
import re
import os
from typing import Type
import uuid
# This project
from slodon.slodonix.utils.func import is_socket_connected


SUPPORTED_PROTOCOLS = (None, "tcp", "unix")


class _OPEN:
    """Opened connection"""
    pass


class _CLOSE:
    """Closed Connection"""
    pass


class _STATUS:
    """EITHER _OPEN or _CLOSE"""
    STATUS = Type[_OPEN] | Type[_CLOSE]


DISPLAY_RE = re.compile(r'^((?P<proto>tcp|unix)/)?(?P<host>[-:a-zA-Z0-9._]*):(?P<dno>[0-9]+)(\.(?P<screen>[0-9]+))?$')


def get_tcp(address: str, dno: int) -> socket.SocketType:
    """
    Return a TCP socket connection to address and port 6000 + dno
    :param address: str
    :param dno: int
    :return: TCP socket connection to address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("in case of tcp, address is: ", address)
    s.connect((address, 6000 + dno))
    return s


def get_unix(address: str) -> socket.SocketType:
    """
    Return a UNIX socket connection to address
    :param address: str
    :return: UNIX socket connection to address
    """
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(address)
    return s


def get_display(display) -> tuple[str, str, str, int, int]:
    # https://github.com/python-xlib/python-xlib/blob/master/Xlib/support/unix_connect.py#L40
    # display CAN'T be None in this case
    re_list = [(DISPLAY_RE, {})]

    for _re, defaults in re_list:
        m = _re.match(display)
        if m is not None:
            protocol, host, dno, screen = [
                m.groupdict().get(field, defaults.get(field))
                for field in ('proto', 'host', 'dno', 'screen')
            ]
            break
    else:
        raise DisplayNameError(display)

    if protocol == 'tcp' and not host:
        # Host is mandatory when protocol is TCP.
        raise DisplayNameError(display)

    dno = int(dno)
    if screen:
        screen = int(screen)
    else:
        screen = 0

    return display, protocol, host, dno, screen


def get_socket(display) -> socket.SocketType:
    """
         Make a connection to a display
    """
    print("display", display)
    display, protocol, host, dno, screen = display

    assert protocol in SUPPORTED_PROTOCOLS, f"Protocol {protocol} not supported"

    try:
        # TCP socket, note the special case: `unix:0.0` is equivalent to `:0.0`.
        if (protocol is None or protocol != 'unix') and host and host != 'unix':
            s = get_tcp(host, dno)
        else:
            address = '/tmp/.X11-unix/X%d' % dno
            if not os.path.exists(address):
                # Use abstract address.
                address = '\0' + address

            try:
                s = get_unix(address)
            except socket.error:
                if not protocol and not host:
                    # If no protocol/host was specified, fallback to TCP.
                    s = get_tcp(host, dno)
                else:
                    raise
    except socket.error as val:
        raise DisplayConnectionError(display, str(val))

    return s


class Connection:
    """Connection to a display"""
    CONNECTIONS = 0  # Number of connections

    def __init__(self, display: str = None) -> None:
        """
        Connection initialization

        ### Arguments
        - display (str): the full display name(string) -> protocol/hostname:number.screen_number
        ### Returns
        - None
        """

        Connection.CONNECTIONS += 1  # Increment number of connections
        self._pure_display = display
        self._display_info = get_display(display)
        self._connection = self._make_connection(self._display_info)
        self._status = is_socket_connected(self._connection)
        self._protocol = self._display_info[2]
        self._id = uuid.uuid4()

    # noinspection PyMethodMayBeStatic
    def _make_connection(self, display_info) -> socket.SocketType:
        return get_socket(display_info)

    def status(self) -> _STATUS.STATUS:
        """
        Return back the current status of the connection
        :return: _OPEN or _CLOSE
        """
        return _OPEN if self._status else _CLOSE

    def close(self):
        self._connection.close()
        self._status = is_socket_connected(self._connection)

    def __repr__(self) -> str:
        keys = ["display", "protocol", "host", "dno"]
        _text = ""
        for i in range(len(keys)):
            _text += f"{keys[i]}={self._display_info[i]} || "
        return _text

    def info(self) -> tuple:
        return self._display_info

    def __str__(self) -> str:
        return f"<Connection={self.status().__name__}|| protocol={self._protocol} || id={self._id}>"
