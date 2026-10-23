impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut out: Vec<i32> = Vec::new();
        // first pass
        let mut forward_vec: Vec<i32> = Vec::new();
        let mut reverse_vec: Vec<i32> = Vec::new();
        let mut prod: i32 = 1;
        for num in nums.iter() {
            forward_vec.push(prod);
            prod *= num;
        }
        prod = 1;
        for num in nums.iter().rev() {
            reverse_vec.push(prod);
            prod *= num;
        }
        reverse_vec.reverse();

        for (forward, rev) in forward_vec.iter_mut().zip(reverse_vec) {
            out.push(*forward * rev);
        }
        out
    }
}
