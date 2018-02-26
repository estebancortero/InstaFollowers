# InstaFollowers

This is a stand-alone InstaPy fork, focusing on one simple task: Quickly extract your current followers.

## Setup and installation

Follow the instructions from [InstaPy](https://github.com/timgrossmann/InstaPy#getting-started). Basically, install the Python packages  with `setup.py`, install Chrome (or Firefox), download and copy chromedriver (or geckodriver) into the `assets` directory.

## Usage

Simply run `python3 get_followers.py -u your_username -p your_password`. Your followers are printed on screen and exported to `followers.csv` for further usage.

If you're running Firefox on Raspberry Pi, use `get_followers_pi.py` instead.
