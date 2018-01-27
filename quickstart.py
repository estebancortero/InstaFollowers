import argparse
from instapy import InstaPy


def parse_args():
    parser = argparse.ArgumentParser(description="Extract all of your followers as a csv file")
    parser.add_argument("-u", "--username", help="Instagram username", required=True, default=None, dest="username")
    parser.add_argument("-p", "--password", help="Instagram password", required=True, default=None, dest="password")
    return parser.parse_args()


args = parse_args()
while True:
	session = InstaPy(username=args.username, password=args.password, headless_browser=True)
	try:
		session.login()

		# settings
		session.set_lower_follower_count(limit = 50)
		session.set_upper_follower_count(limit = 5000)
		session.set_do_comment(enabled=True, percentage=50)
		session.set_comments(['Nice!', 'Love it :)', 'Perfect!', '@{} This is amazing!', 'Great picture! @{}'], media='Photo')
		session.set_do_follow(enabled=True, percentage=50, times=2)
		session.set_user_interact(amount=2, randomize=3, percentage=100, media="Photo")			# settings for interaction with users from tags or feed
		session.set_dont_unfollow_active_users(enabled=True, posts=10)

		# actions
		session.like_by_tags(['travel', 'goodlife', 'love'], amount=20, media='Photo', interact=True)	# interact=True => use interaction settings above
		session.like_by_feed(amount=30, randomize=True, unfollow=True, interact=True)	# unfollow inappropriate posts
		session.like_by_locations(["24960421/porto-portugal/"], amount=10, media="Photo")
		session.follow_by_tags(['travel', 'food', 'vegan'], amount=10, media="Photo")

		session.unfollow_users(amount=35, onlyInstapyFollowed=True, onlyNotFollowMe=True)

	finally:
		session.end()