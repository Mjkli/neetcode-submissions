impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_chars: Vec<char> = s.as_str().chars().collect::<Vec<char>>();
        let mut t_chars: Vec<char> = t.as_str().chars().collect::<Vec<char>>();
        s_chars.sort();
        t_chars.sort();
        if s_chars != t_chars {
            return false
        }
        return true


    }
}
