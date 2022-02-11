from datetime import datetime
from hashlib import sha256

"""There are several advantages and disadvantages to this
proof of work or proof of stake is difficult for voting machines if they are air gapped
air gapping is probably necessary
how do you verify voters if airgapped
there shoudl always be hard copies
"""

#origin bloc
# new block with hash and link to prev block hash


#way to create individual blocks
class VoteBlock:
    def __init__(self, user_num, *user_votes, prev_hash):
        self.user_num = user_num
        self.user_votes = user_votes
        self.prev_hash = prev_hash
        self.cur_hash = self.current_hash()

    def to_string(self):
        self.str_user_num = str(self.user_num)
        self.str_timestamp = str(datetime.datetime.now())
        self.str_user_votes = str(self.user_votes)
        self.str_prev_hash = str(self.prev_hash)
        self.block_contents = self.str_user_num + self.str_timestamp
        return 

    


        # num_votes = len(self.votes)
        # block_contents = "At time", self.timestamp,\
        #     "User number", self.user_num,\
        #     "voted for", self.votes,\
        #     "the hash for the previous vote is", self.prev_hash,\
        #     "the hash for the current vote is", self.cur_hash
        # return block_contents

    def current_hash(self):
        to_hash = str(self.user_num) + str(datetime.datetime.now())\
             + str(self.votes_for) + str(self.prev_hash)
        vote_block_hash = sha256(to_hash.encode())
        return vote_block_hash.hexdigest()
    

#chain of all transactions
class ElectChain: # ElectChain, get it?
    def __init__(self):
        self.new_vote = []
        self.chain = []
        self.genesis_vote()

    def genesis_vote(self):
        self.chain.append(VoteBlock("0", "No Votes", ""))

    def now_vote_link(self):
        pass

    def validate_block(self):
        # if oldblock != newblock prevhash
        pass

# verify that only people on an approved list have voted
class VerifyVotes:
    def __init__(self, voter_number_list):
        self.voter_list = voter_number_list

    def check_votes(self):
        #if 
        vote_checker = "At time:", self.str_timestamp, "\r\n",\
            "User Number:", self.str_user_num, "\r\n",\
            "voted for:", self.str_user_votes, "\r\n",\
            "Is this correct?", 


class ProofStakeVote:
    def __init__(self):
        pass



# Class VoteChain:
#     def __init__(self):
#         self.chain = []
#         self.all_votes = []
#         self.genesis_block()

#     def genesis_block(self):
#         self.chain.apend(VoteBlock(["none"], 0))




if __name__=="__main__":
    pass