import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}       # userId -> [(time, tweetId)]
        self.following = {}    # userId -> set of followees
        self.time = 0

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        users = {userId}

        if userId in self.following:
            users.update(self.following[userId])

        heap = []

        # Add all tweets from user and followed users
        for user in users:
            if user in self.tweets:
                for time, tweetId in self.tweets[user]:
                    heapq.heappush(heap, (-time, tweetId))

        # Get 10 most recent tweets
        result = []

        for _ in range(10):
            if not heap:
                break

            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId, followeeId):
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)