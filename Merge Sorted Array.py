# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums[]=new int[m+n];
        int i=0,j=0,k=0;
        while(i<m && j<n)
        {
            if(nums1[i]<=nums2[j]){
                nums[k++]=nums1[i++];
                // System.out.println(nums1[k-1]+" "+nums[i-1]);

            }
            else{
                nums[k++]=nums2[j++];
            }
        }
        if(i<m){
            for(;i<m;i++){
                nums[k++]=nums1[i];
            }
        }
        else{
            for(;j<n;j++)
            {
                nums[k++]=nums2[j];
            }
        }
        
        for(int l=0;l<m+n;l++){
            
            nums1[l]=nums[l];
        }
    }
}


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
