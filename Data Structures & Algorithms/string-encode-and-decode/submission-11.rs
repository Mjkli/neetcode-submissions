impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();
        for s in strs {
            encoded = format!("{}*!>{}", encoded, s)
        }
        encoded
    }

    pub fn decode(s: String) -> Vec<String> {
        let decoded: Vec<String> = s.split("*!>").map(|n| n.to_string()).collect::<Vec<String>>();

        decoded[1..].to_vec()
    }
}
