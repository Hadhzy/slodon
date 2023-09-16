<div style="text-align:center;">
  <img src="https://github.com/Hadhzy/slodon/blob/main/_static/images/slodon_logo.png?raw=true" alt="" width="45%">
</div>
<br />

## What is Slodonix?

Welcome to Slodonix Documentation!

[Slodonix](https://github.com/Hadhzy/slodon/tree/main/slodon/slodonix) is a crucial **_sub-package_** within the [Slodon](https://github.com/Hadhzy/slodon) _ecosystem_, dedicated to [emulated input](https://en.wikipedia.org/wiki/Emulator) operations. It leverages low-level APIs that are tailored for specific operating system **display servers**, such as [hadhzy-python-xlib](https://github.com/Hadhzy/hadhzy-python-xlib) on x-based distributions(most Linux distributions), or communicates directly with the `Win32 API on the Windows platform`. Slodonix achieves this functionality by `interfacing with the underlying operating system's APIs`.

In other words [Slodonix](https://github.com/Hadhzy/slodon/tree/main/slodon/slodonix) is a `Python package` that can be used to `perform and automate user actions` such as keyboard input and mouse events, etc... using the low-level APIs as mentioned above.

We strongly believe that `cross-platform` support is the way to go, we are supporting: `Windows, Linux(x), Linux(Wayland), and
macOS`.

In order to achieve these supports, [ctypes](https://docs.python.org/3/library/ctypes.html) are being used in Windows as mentioned earlier, we are using [python-xlib](https://github.com/Hadhzy/hadhzy-python-xlib) on x-based distributions, and our custom [hzy](https://github.com/Hadhzy/hzy) library is being used for Wayland. In regards of macOS, we are using [AppKit](https://developer.apple.com/documentation/appkit/).

<br />

## What to expect from this documentation?

In this documentation, we will leave **_no stone unturned_** as we explore Slodonix's functionality. We believe that the best way to understand something is to actually see what it is capable of and then discussing and analysing how it works, therefore we will first look into a `simple working example` and then we will see exactly how it works **_under the hood_**. By the end of this guide, you will have a deep understanding of Slodonix's inner workings and see how exactly you can try it out and improve it.

<br />

## Let's Begin

Without further ado, let's take this journey into the world of Slodonix!

---

<br />

[Edit this page on Github](https://github.com/Hadhzy/slodon/blob/main/docs/docs/slodonix/introduction.md)
