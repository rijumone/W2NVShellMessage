import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='W2NVShellMessage',
    version='0.1',
    description='A package to display quotes from "Welcome to Night Vale" whenever a new terminal window is launched',
    url='https://github.com/rijumone/W2NVShellMessage',
    author='Rijumone Choudhuri',
    author_email='mailmeonriju@gmail.com',
    license='MIT',
    packages=['w2nvshellmsg'],
    zip_safe=False,
    install_requires=[
        'requests',
        'loguru',
        'bs4',
        'colorama',
        ],

)
