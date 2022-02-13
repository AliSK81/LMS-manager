# LMS-manager

This script helps you log in to your [LMS](http://lms.ui.ac.ir/) account and enter the currently running session, all in a second.
</br>
## Install packages
First, make sure `Python 3` is installed on your system. Open the terminal and run:
```
python --version
```
You should get a message like `"Python 3.8.5."` otherwise, download it from [here.](https://www.python.org/downloads/) </br>

Before anything, it is good to check that you are working with the most recent version of `pip`:
```
pip install --upgrade pip
```
With pip installed, the installation is straightforward, run:
```
pip install -r req.txt
```

## Get started
Create file `config.py` and put the following properties in it:
```
USERNAME = 'YOUR_USER_NAME'
PASSWORD = 'YOUR_PASSWORD'
```
So, the project structure will be:
```
|-- config.py
|-- driver.py
|-- main.py
|-- meeting.py
|-- req.txt
```

Now run:
```
python main.py
```

**Note:** Make sure you run this script when a meeting begins.
Otherwise, you have to enter the session yourself or run `main.py` again. </br>
**Note:** Once you install packages, you can double-click on `main.py` to run the script next time.
