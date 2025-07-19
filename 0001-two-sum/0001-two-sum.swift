class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    /*
        for i in 0..<nums.count {
            for j in i+1..<nums.count {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return [-1, -1]
    */

        var complementsIndex: [Int: Int] = [:]  // map complement to its index
        for (index, num) in nums.enumerated() {
            let complement = target - num
            if let indexOfComplement = complementsIndex[complement] {
                return [index, indexOfComplement]
            }

            complementsIndex[num] = index
        }

        return [-1, -1]
    }
}