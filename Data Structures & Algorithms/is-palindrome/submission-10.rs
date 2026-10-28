impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        if s.len() == 1 {
            return true
        }
        let out = s.chars().filter(|c| c.is_alphanumeric()).collect::<String>().to_lowercase();
        out.to_lowercase();
        if out.len() == 0 {
            return true
        }


        println!("{}", out);
        let mut left: usize = 0;
        let mut right: usize = out.len() - 1;

        while left < right {
            let lchar = out.as_bytes()[left] as char;
            let rchar = out.as_bytes()[right] as char;

            if lchar != rchar {
                println!("{} :: {}", lchar, rchar);
                return false
            }

            left += 1;
            right -= 1;
        }
        
        return true
    }
}
