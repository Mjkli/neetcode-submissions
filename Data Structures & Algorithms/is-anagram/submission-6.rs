impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut count1 = [0; 26];
        let mut count2 = [0; 26];

        s.bytes().for_each(|b| count1[(b - b'a') as usize] += 1);
        t.bytes().for_each(|b| count2[(b - b'a') as usize] += 1);

        if count1 == count2 {
            return true
        }

        return false

    }
}
