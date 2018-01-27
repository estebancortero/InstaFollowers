import csv
import argparse
from instapy import InstaPy
from instapy.unfollow_util import get_given_user_followers


def parse_args():
    parser = argparse.ArgumentParser(description="Extract all of your followers as a csv file")
    parser.add_argument("-u", "--username", help="Instagram username", required=True, default=None, dest="username")
    parser.add_argument("-p", "--password", help="Instagram password", required=True, default=None, dest="password")
    return parser.parse_args()


# login info as command line arguments
args = parse_args()

# export all your followers as a list in a txt file
session = InstaPy(username=args.username, password=args.password, headless_browser=True)
session.login()
# change session.username to another user to export their followers
followers = get_given_user_followers(session.browser, session.username, 30, session.dont_include, session.username,
                                     False, session.logger, get_all=True)
print(followers)

# export to file
with open("followers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(followers)
print("Wrote all {} followers into followers.csv".format(len(followers)))
