class Solution {
    public int search(int[] nums, int target) {
        int L = 0;
        int R = nums.length;

        int mid;
        while (L < R) {
            mid = (L + R) / 2;
            if (nums[mid] < target) {       // we are too small
                L = mid + 1;                // make nums bigger
            }
            else if (nums[mid] > target) {  // we are too big
                R = mid;                    // make nums smaller; R is exclusive
            }
            else {
                return mid;
            }
        }
        return -1;
    }
}