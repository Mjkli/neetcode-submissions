impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut count: HashMap<i32, usize> = HashMap::new();

        for num in nums {
            count.entry(num).and_modify(|count| *count += 1).or_insert(1);
        }

        let mut count_vec: Vec<_> = count.iter().collect();
        count_vec.sort_by(|k,v| v.1.cmp(&k.1));
        count_vec.resize(k as usize, (&0,&(0 as usize)));
        println!("{:?}", count_vec);

        let mut out: Vec<i32> = vec![0;k as usize];
        for (i, pair) in count_vec.into_iter().enumerate() {
            out[i] = pair.0.to_owned();
        }

        out
    }
}
