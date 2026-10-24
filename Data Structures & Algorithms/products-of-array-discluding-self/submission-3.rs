impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut out: Vec<i32> = Vec::new();
        let mut prod: i32 = 1;
        
        for num in nums.iter() {
            out.push(prod);
            prod *= num;
        }
        
        let mut suffix: Vec<i32> = Vec::new();
        prod = 1;
        
        for num in nums.iter().rev() {
            suffix.push(prod);
            prod *= num;
        }
        suffix.reverse();

        for (i, num) in out.iter_mut().enumerate() {
            *num *= suffix[i];
        }

        out
    }
}
