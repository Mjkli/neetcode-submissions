impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut count1 = [0; 26];
        let mut count2 = [0; 26];

        for b in s.bytes() {
            let index = (b - b'a') as usize;
            count1[index] += 1;
        }
        for b in t.bytes() {
            let index = (b - b'a') as usize;
            count2[index] += 1;
        }

        if count1 == count2 {
            return true
        }

        return false

    }
}
