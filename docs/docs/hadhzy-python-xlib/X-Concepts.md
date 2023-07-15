## What is a display server?

A [display server](https://en.wikipedia.org/wiki/Windowing_system#Display_server) is a program whose primary task is to coordinate the input and output of its clients to and from the rest of the operating system.

Every display server has its own [protocol](https://en.wikipedia.org/wiki/X_Window_System_core_protocol) for communication purposes. The word `display-server` can be more commonly referred on Linux.

Since Windows does not really have an independent display server, instead it is [built into](https://en.wikipedia.org/wiki/Desktop_Window_Manager) 

the operating system itself(kernel).

As you may be aware of, on Linux the kernel tends to be more modular, and thus the display server is a separate program.

It is really important to note the difference between a display server and its C library.


---

| Display Server                                            | C library                                              |
|-----------------------------------------------------------|--------------------------------------------------------|
| [X](https://gitlab.freedesktop.org/xorg/xserver)          | [Xlib](https://gitlab.freedesktop.org/xorg/lib/libx11) |
| [Wayland](https://gitlab.freedesktop.org/wayland/wayland) | *GTK/QT*                                               |


Xlib is a library that allows you to `communicate with the X display server`(aka X).

---

## X

X is a  [display server](#what-is-a-display-server) which runs on the port [6000](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers). 

Nowadays, it is more common to use [wayland](https://wayland.freedesktop.org/) instead of X, but X is still used by many applications.





