impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i, val) in nums.iter().enumerate() {
            for (j, val2) in nums.iter().enumerate() {
                if i == j {
                    continue
                }
                if (val + val2) == target.try_into().unwrap() {
                    return vec![i.try_into().unwrap(),j.try_into().unwrap()]
                }
            }
        }

        vec![]
    }
}
