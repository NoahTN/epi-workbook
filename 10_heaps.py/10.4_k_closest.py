# https://leetcode.com/problems/k-closest-points-to-origin/
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
# O(klogk), O(k)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
      heap = []
      for p in points:
         # Use negative dist on min heap to create max heap
         dist = -(p[0]**2+p[1]**2)
         # Pop out smallest (technically largest) distance and push 
         if len(heap) == K:
            heappushpop(heap, (dist, p))
         # Push to heap using dist
         else:
            heappush(heap, (dist, p))

        return [p for (dist, p) in heap]