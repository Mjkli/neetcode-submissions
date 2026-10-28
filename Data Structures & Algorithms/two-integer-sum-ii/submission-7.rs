impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut out: Vec<i32> = vec![0; 2];

        let mut left = 0;
        let mut right = numbers.len() - 1;
        while left < right {
            let poss_sum = numbers[left] + numbers[right];
            if poss_sum == target {
                return vec![left as i32 + 1, right as i32 + 1]
            }

            if poss_sum > target {
                right -= 1;
            } else if poss_sum < target {
                left += 1;
            }


        }

        out
    }
}
