impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut word_map: HashMap<[u32;26], Vec<String>> = HashMap::new();

        for s in strs {
            let mut count = [0;26];
            for b in s.bytes() {
                let index = (b - b'a') as usize;
                count[index] += 1
            }
            word_map.entry(count).and_modify(|list| list.push(s.clone())).or_insert(vec![s.clone()]);
        }
        
        let out = word_map.values().cloned().collect();
        return out
    }
}
