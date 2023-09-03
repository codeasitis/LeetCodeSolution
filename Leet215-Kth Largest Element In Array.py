import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == []:
            return nums
        else:
            heap = []
            for i in range(0, k):
                heapq.heappush(heap, (nums[i], i))
            for j in range(k, len(nums)):
                root_element = [entries for entries in heapq.nsmallest(1, heap)][0]
                index_root_element = heap.index(root_element)
                if nums[j] > root_element[0]:
                    heap[index_root_element] = (nums[j], j)
                    heapq.heapify(heap)
        return heapq.heappop(heap)[0]
