"""Keyboard and Pointer Events"""

#-----------------------------------------------------------------------
# Event names:
#
# 0 and 1 are reserved for errors and replies in the protocol

_KeyPress               = 2
_KeyRelease             = 3
_ButtonPress            = 4
_ButtonRelease          = 5
_MotionNotify           = 6
_EnterNotify            = 7
_LeaveNotify            = 8
_FocusIn                = 9
_FocusOut               = 10
_KeymapNotify           = 11
_Expose                 = 12
_GraphicsExpose         = 13
_NoExpose               = 14
_VisibilityNotify       = 15
_CreateNotify           = 16
_DestroyNotify          = 17
_UnmapNotify            = 18
_MapNotify              = 19
_MapRequest             = 20
_ReparentNotify         = 21
_ConfigureNotify        = 22
_ConfigureRequest       = 23
_GravityNotify          = 24
_ResizeRequest          = 25
_CirculateNotify        = 26
_CirculateRequest       = 27
_PropertyNotify         = 28
_SelectionClear         = 29
_SelectionRequest       = 30
_SelectionNotify        = 31
_ColormapNotify         = 32
_ClientMessage          = 33
_MappingNotify          = 34
LASTEvent              = 35


class KeyPress:
    _code = _KeyPress
    pass


class KeyRelease:
    _code = _KeyRelease
    pass


class ButtonPress:
    _code = _ButtonPress
    pass


class ButtonRelease:
    _code = _ButtonRelease
    pass


class MotionNotify:
    _code = _MotionNotify
    pass


class EnterLeave:
    _code = None
    pass


class EnterNotify(EnterLeave):
    _code = _EnterNotify


class LeaveNotify(EnterLeave):
    _code = _LeaveNotify


class Focus:
    _code = None
    pass


class FocusIn(Focus):
    _code = _FocusIn


class FocusOut(Focus):
    _code = _FocusOut


class Expose:
    _code = _Expose
    pass


class GraphicsExpose:
    _code = _GraphicsExpose
    pass


class NoExpose:
    _code = _NoExpose
    pass


class VisibilityNotify:
    _code = _VisibilityNotify
    pass


class CreateNotify:
    _code = _CreateNotify
    pass


class DestroyNotify:
    _code = _DestroyNotify
    pass


class UnmapNotify:
    _code = _UnmapNotify
    pass


class MapNotify:
    _code = _MapNotify
    pass


class MapRequest:
    _code = _MapRequest
    pass


class ReparentNotify:
    _code = _ReparentNotify
    pass


class ConfigureNotify:
    _code = _ConfigureNotify
    pass


class ConfigureRequest:
    _code = _ConfigureRequest
    pass


class GravityNotify:
    _code = _GravityNotify
    pass


class ResizeRequest:
    _code = _ResizeRequest
    pass


class Circulate:
    _code = None
    pass


class CirculateNotify(Circulate):
    _code = _CirculateNotify


class CirculateRequest(Circulate):
    _code = _CirculateRequest


class PropertyNotify:
    _code = _PropertyNotify
    pass


class SelectionClear:
    _code = _SelectionClear
    pass


class SelectionRequest:
    _code = _SelectionRequest
    pass


class SelectionNotify:
    _code = _SelectionNotify
    pass


class ColormapNotify:
    _code = _ColormapNotify
    pass


class MappingNotify:
    _code = _MappingNotify
    pass


class ClientMessage:
    _code = _ClientMessage
    pass


class KeymapNotify:
    _code = _KeymapNotify
    pass
