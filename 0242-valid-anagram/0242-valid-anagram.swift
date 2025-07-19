class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var charOccurences: [Character: Int] = [:]  // tracks the number of occurences of each char in s
        for char in s {
            charOccurences[char, default:0] += 1
        }

        for char in t {
            charOccurences[char, default:0] -= 1
        }

        for numOccurences in charOccurences.values {
            if numOccurences != 0 {
                return false
            }
        }

        return true
    }
}