<p align="center">
<img src="https://github.com/Hadhzy/slodon/blob/main/_static/images/slodonix_logo.png" alt="" width="70%">
</p>

<br/>
<br/>
<br/>

## What is Slodonix?

Slodonix is a python library which has a couple of dependencies:
<br/>
<br/>

- <a href="https://github.com/Hadhzy/hzy" target="_blank"><code>hzy</code></a>
- <a href="https://pypi.org/project/hadhzy-python-xlib/" target="_blank">hadhzy-python-xlib</a>

Slodonix uses the underlying api of the current operating system like using windows api through ctypes. It is important to note that this "API(windows api through ctypes)" is the same on every operating systems, only the underlying protocol changes.

Slodonix is responsible for doing emulated input by using low-level APIs specialized on the current operating system display server(on Linux), or communicating directly to the API(win32 on windows).

This library puts all these together and offers an easy API e.g. (mouse click, mouse move), which can be used in a lot of different ways(context manager, inheriting from meta class).

Slodonix plays a vital role and can be used independently under the slodon package.

Now let's see how to use it and see how it works.

## How to use it?

One way of using Slodonix, is by inheritence following these steps:

**Step 1**. **Create Your Class and Inherit [DisplayAsParent]()**:
Start by making your own class. In this class, you should use the DisplayAsParent class as a starting point. This inheritance will give you access to an abstract method called body, which you'll need to fill in.

**Step 2**. **Fill in the body Method**:
Inside the body method, you get to decide what your program should do. You can think of it as a place to write down all the actions your program will take. These actions are based on the capabilities provided by the Display class, which, in turn, uses the Interact class to handle things like button clicks, mouse movements, and so on.

**Step 3**. **Run Your Program**:
Once you've defined your program's actions within the body method. You'd have to somehow need to execute it, you do this by calling the run method. This method, which is part of the DisplayAsParent class, takes care of executing your program's main defined instructions. It essentially executes and runs out all the actions you specified in the body method. Additionally, it might set up event listeners if there is any.

---

The active development is in the [slodon/slodonix](https://github.com/Hadhzy/slodon/tree/main/slodon/slodonix)
