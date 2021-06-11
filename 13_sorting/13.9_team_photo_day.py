class Team:
   Player = namedtuple("Player", ("height"))
   def __init__(self, height):
      self._players = [Team.Player(h) for h in height]
   # O(nlogn) + O(mlogm), O(1)
   def has_valid_placement(A, B):
      return all(a < b for a,b in zip(sorted(A._players), sorted(B._players)))