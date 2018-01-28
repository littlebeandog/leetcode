class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        ml, mr, nl, nr = 0, 0, 0, 0
        start = 0
        end = 2 * m
        
        while start <= end:
            m_cut = (end + start) / 2
            n_cut = m + n - m_cut
            ml = 0 if m_cut == 0 else nums1[(m_cut - 1) / 2]
            mr = nums2[-1] if m_cut == 2 * m else nums1[m_cut / 2]
            nl = 0 if n_cut == 0 else nums2[(n_cut - 1) / 2]
            nr = nums1[-1] if n_cut == 2 * n else nums2[n_cut / 2]
            
            if ml > nr:
                end = m_cut - 1
            elif mr < nl:
                start = m_cut + 1
            else:
                break
        
        return (min(nr, mr) + max(nl, ml)) / 2.0
        