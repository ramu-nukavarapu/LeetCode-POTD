# 3100. [Water Bottles II](https://leetcode.com/problems/water-bottles-ii)

**Medium**

You are given two integers `numBottles` and `numExchange`.

- `numBottles` represents the number of full water bottles that you initially have.  
- In one operation, you can perform one of the following operations:
  - Drink any number of full water bottles, turning them into empty bottles.
  - Exchange `numExchange` empty bottles with one full water bottle. Then, increase `numExchange` by one.

Note: You cannot exchange multiple batches of empty bottles for the same value of `numExchange`.  
For example, if `numBottles == 3` and `numExchange == 1`, you cannot exchange `3` empty water bottles for `3` full bottles.

Return the **maximum number of water bottles you can drink**.

---

### Example 1:

**Input:**  
`numBottles = 13, numExchange = 6`  

**Output:**  
`15`  

**Explanation:**  
Initially 13 bottles are drunk (now 13 empty).  
- Exchange 6 empty → 1 full, left with 7 empty. (`numExchange = 7`)  
- Exchange 7 empty → 1 full, left with 0 empty. (`numExchange = 8`)  
- Drink 2 more bottles.  

Total drunk = `15`.

---

### Example 2:

**Input:**  
`numBottles = 10, numExchange = 3`  

**Output:**  
`13`  

**Explanation:**  
Initially 10 bottles are drunk (now 10 empty).  
- Exchange 3 empty → 1 full, left with 7 empty. (`numExchange = 4`)  
- Exchange 4 empty → 1 full, left with 3 empty. (`numExchange = 5`)  
- Drink 2 more bottles (total 12).  
- Exchange 5 empty → 1 full, left with 0 empty. (`numExchange = 6`)  
- Drink 1 more bottle.  

Total drunk = `13`.

---

### Constraints:

- `1 <= numBottles <= 100`  
- `1 <= numExchange <= 100`

        