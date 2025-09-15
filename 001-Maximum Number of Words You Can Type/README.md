# 1935. [Maximum Number of Words You Can Type](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.  

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all distinct letter keys that are broken, return **the number of words in `text` you can fully type using this keyboard**.

---

### Solution Stats
- **Runtime:** 0 ms — Beats **100.00%** 🥇  
- **Memory Usage:** 17.84 MB — Beats **57.65%**  
- **Result:** Accepted (20/20 test cases passed)  
- **Submission Time:** Sep 15, 2025, 21:11  

---

### Example 1:
**Input:**  
`text = "hello world", brokenLetters = "ad"`  
**Output:**  
`1`  
**Explanation:**  
We cannot type `"world"` because the `'d'` key is broken.  

---

### Example 2:
**Input:**  
`text = "leet code", brokenLetters = "lt"`  
**Output:**  
`1`  
**Explanation:**  
We cannot type `"leet"` because the `'l'` and `'t'` keys are broken.  

---

### Example 3:
**Input:**  
`text = "leet code", brokenLetters = "e"`  
**Output:**  
`0`  
**Explanation:**  
We cannot type either word because the `'e'` key is broken.  

---

### Constraints:
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- `brokenLetters` consists of **distinct lowercase English letters**.
