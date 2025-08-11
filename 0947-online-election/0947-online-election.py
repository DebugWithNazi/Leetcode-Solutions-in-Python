class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_count = {}
        leader = -1
        leader_count = 0

        for p in persons:
            vote_count[p] = vote_count.get(p,0) + 1

            if vote_count[p] >= leader_count:
                leader = p
                leader_count = vote_count[p]

            self.leaders.append(leader)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times,t) - 1
        return self.leaders[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)