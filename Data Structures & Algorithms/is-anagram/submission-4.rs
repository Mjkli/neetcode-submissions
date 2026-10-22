impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut count1 = [0; 26];
        let mut count2 = [0; 26];

        for b in s.bytes() {
            count1[(b - b'a') as usize] += 1;
        }
        for b in t.bytes() {
            count2[(b - b'a') as usize] += 1;
        }

        if count1 == count2 {
            return true
        }

        return false

    }
}
