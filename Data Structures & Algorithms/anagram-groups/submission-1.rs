impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut word_map: HashMap<[u32;26], Vec<String>> = HashMap::new();

        for s in strs {
            let mut count = [0;26];
            for b in s.bytes() {
                let index = (b - b'a') as usize;
                count[index] += 1
            }
            word_map.entry(count).or_default().push(s);
        }
        
        let out = word_map.into_values().collect();
        return out
    }
}
