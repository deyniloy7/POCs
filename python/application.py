import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CC4ffV0IFmycQshDLIBRAs4om", "TqTGq20Gy58JRGD0SQHNyuHJuek71tJQegJpzECSUgcxkLm0VR")
auth.set_access_token("1001844758-pS5EsBx0P2kKltDaNx14bEWBtkTMsaxo73Jg5Sh", "S6GdOLCsirIWbrz8VkFoAN31nRnMZc9ffKGElvDLRMxgI")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# api.update_status("Test tweet from Tweepy!")

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} ------ said {tweet.text}")

# user = api.get_user("deyniloy7")
# print(user.name)
# print(user.description)
# print(user.location)

# for follower in user.followers():
#     print(follower.name)

# api.create_friendship("realpython")

# for block in api.blocks():
#     print(block.name)

for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")