import heapq
from collections import defaultdict
import itertools

class Twitter:

    def __init__(self):
        self.tweet_order = 0
        self.follow_relations = defaultdict(set) # follower -> followee
        self.user_posts = defaultdict(list) # user x -> all user x posts

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_order += 1
        self.user_posts[userId].append((self.tweet_order, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = {userId} | self.follow_relations[userId]
        heap = []
        for uid in followees:
            tweets = self.user_posts[uid]
            if tweets:
                idx = len(tweets)-1
                time, tweet_id = tweets[idx]
                heapq.heappush(heap, (-time, tweet_id, uid, idx))
        results = []
        while heap and len(results) < 10:
            neg_time, tweet_id, uid, idx = heapq.heappop(heap)
            results.append(tweet_id)
            if idx > 0:
                time, tweet_id = self.user_posts[uid][idx - 1]
                heapq.heappush(heap, (-time, tweet_id, uid, idx - 1))

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_relations[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_relations[followerId].discard(followeeId)
        
