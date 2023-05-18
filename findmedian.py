#!/usr/local/bin/python3

def find_median_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total_length = m + n

    # Ensure nums1 is the smaller array for ease of implementation
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    # Initialize the search range for binary search
    imin, imax = 0, m

    while imin <= imax:
        # Partition positions for both arrays
        i = (imin + imax) // 2
        j = (total_length + 1) // 2 - i

        # Binary search criteria
        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        else:
            # Median elements
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])

            if total_length % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

    # Execution should not reach this point if input arrays are sorted correctly
    raise ValueError("Input arrays are not sorted correctly.")


# Example usage
nums1 = [3, 5, 7]
nums2 = [6, 8, 9]
median = find_median_sorted_arrays(nums1, nums2)
print("Median:", median)
