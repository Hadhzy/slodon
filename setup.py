from setuptools import setup

about = {}
with open("_version.py") as fp:
    exec(fp.read(), about)

setup(
    name="slodon",
    version=about["__version__"],
    python_requires=">=3.11",
    description="Emulated input for Wayland in python",
    long_description="Emulated input for Wayland in python",
    url="https://github.com/Hadhzy/hzy",
    license="Apache 2.0",
    packages=["slodon"],
    author="Hadhzy Organisation"
)
