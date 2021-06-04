from typing import Counter

def can_palin_permute(s):
   return sum(count % 2 for count in Counter(s).values()) <= 1