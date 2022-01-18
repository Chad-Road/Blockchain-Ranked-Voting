from datetime import datetime
from hashlib import sha256
from msilib.schema import Class

class VoteBlock:
    def __init__(self, *votes_for, prev_hash):
        self.votes_for = votes_for
        self.prev_hash = prev_hash
        self.vote_time = datetime.now()
        self.cur_hash = self.current_hash()

    def block_values(self):
        num_votes = len(self.votes)
        block_contents = "At time", self.timestamp,\
            "there were", num_votes, "votes",\
            "the votes were for", self.votes,\
            "the hash for the previous vote is", self.prev_hash,\
            "the hash for the current vote is", self.cur_hash
        return block_contents

    # def current_hash(self):

    


# class ElectionBlock:
#     def __init__(self):


# class VoteChain:
#     def __init__(self):
#         self.chain = []
#         self.all_votes = []
#         self.genesis_block()

#     def genesis_block(self):
#         self.chain.apend(VoteBlock(["none"], 0))