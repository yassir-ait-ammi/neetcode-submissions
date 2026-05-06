class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        while (stones.length > 1) {
            stones.sort((a, b) => b - a); // sort descending

            let y = stones.shift(); // largest
            let x = stones.shift(); // second largest

            if (y !== x) {
                stones.push(y - x);
            }
        }

        return stones.length ? stones[0] : 0;
    }
}
