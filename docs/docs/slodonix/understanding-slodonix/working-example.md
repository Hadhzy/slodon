## What this chapter will cover?

In this chapter we are going to look at a working code snippet example to demonstrate what slodonix is capable of. Then we are going to discuss how it works **under the hood**. We will break down the explanations into different chapters to fully understand what is going on. Let's dive in!

## Working Example

this code can be found at: [slodon/slodon/slodonix/examples/windows/example_1.py](https://github.com/Hadhzy/slodon/blob/main/slodon/slodonix/examples/windows/example_1.py)

```python
import slodon.slodonix as slodonix


class MyApp(slodonix.DisplayAsParent):
    def __init__(self):
        super().__init__()

    def body(self):
        self.move_to(10, 0)

    def trigger_mouse(self, event):
        print("Moving")


MyApp().run()
```

As you can see this code is very simple, it is a class that inherits from `slodonix.DisplayAsParent` and overrides the `body` and `trigger_mouse` methods. In the body method all we are doing is calling `self.move_to(10,0)` and giving in the positons, to run our app let's call `Myapp().run()`. **_Note that this is a really simple example just to see how slodonix works, you can do much more complicated actions which we are going to cover later_** but for now if you run the code this is what you are going to get as a result:

```bash
Moving
```

In this example we are seeing the `Moving` printed out which is because the `trigger_mouse` method was called **under the hood**, you also see that our mouse has moved to the position `10, 0`. Now let's break down what is going on in this code.

## What will the next chapter cover?

In the next chapter we are going to take a look at the structure of slodonix. We are going to take a look at the different files that are associated with it and discuss what they are for. Hopefully you now see how easy it is to try out slodonix.

[Edit this page on Github](https://github.com/Hadhzy/slodon/tree/main/docs/docs/slodonix/understanding-slodonix/working-example.md)
