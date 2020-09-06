from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''



# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    #session.set_relationship_bounds(enabled=True,
                                    #delimit_by_numbers=True,
                                    #max_followers=4590,
                                    #min_followers=45,
                                    #min_following=77)

    #session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["pizza", "#store"])

    # activity

    session.set_do_follow(enabled=False, percentage=50)
    session.set_comments(["Dear Friend this is not real insta User! This is testing bot of @user"])
    session.set_do_comment(enabled=True, percentage=80)
    session.set_do_like(True, percentage=70)
    session.interact_by_users(['user'], amount=5, randomize=True, media='Photo')
