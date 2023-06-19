# https://tronche.com/gui/x/xlib/window/
# https://tronche.com/gui/x/xlib/window/attributes

__all__ = ["create_window", "destroy_window", "XWindow"]


class XWindow:
    """
    Represents an X window.
    """

    # Todo: Type annotations for all arguments based on the above links.(most of them are not defined yet)
    def __init__(
        self,
        background_pixmap,  # background pixmap
        background_pixel,  # background pixel value
        border_pixmap,  # border of the window
        border_pixel,  # border pixel value
        bit_gravity,  # one of the bit gravity values
        win_gravity,  # one of the window gravity values
        backing_store,
        backing_planes,  # planes to be preserved if possible
        backing_pixel,  # value to use in restoring planes
        save_under,  # should bits under be saved
        event_mask,  # set of events that should be saved
        do_not_propagate_mask,  # set of event that should propagate
        override_redirect,  # boolean value for override-redirect
        colormap,  # color map to be associated with window
        cursor,  # cursor to be displayed (or None)
    ):
        self.background_pixmap = background_pixmap
        self.background_pixel = background_pixel
        self.border_pixmap = border_pixmap
        self.border_pixel = border_pixel
        self.bit_gravity = bit_gravity
        self.win_gravity = win_gravity
        self.backing_store = backing_store
        self.backing_planes = backing_planes
        self.backing_pixel = backing_pixel
        self.save_under = save_under
        self.event_mask = event_mask
        self.do_not_propagate_mask = do_not_propagate_mask
        self.override_redirect = override_redirect
        self.colormap = colormap
        self.cursor = cursor


# Todo: Return a simple or a normal window based on the argument.
def create_window(simple=False):
    """
    Return an XWindow object.
    reference: https://tronche.com/gui/x/xlib/window/XCreateWindow.html
    """

    if simple:
        # return a simple window
        pass
    # return normal window


def destroy_window():
    # https://tronche.com/gui/x/xlib/window/destroy.html
    pass
