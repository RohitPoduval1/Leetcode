class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var num_index: [Int: Int] = [:]
        for i in stride(from: 0, to: nums.count, by: 1) {
            let curr_num: Int = nums[i]
            let needed_complement: Int = target - curr_num
            if let complement_index: Int = num_index[needed_complement] {
                return [i, complement_index]
            }
            num_index[curr_num] = i
        }
        return [-1, -1]
    }

    // Brute Force
    /*
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0...nums.count-1 {
            for j in i+1...nums.count-1 {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return [-1, -1]
    }
    */
}