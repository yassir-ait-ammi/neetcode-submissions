class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    peek() {
        return this.heap[0];
    }

    push(val) {
        this.heap.push(val);
        this.bubbleUp();
    }

    pop() {
        if (this.size() === 1) return this.heap.pop();

        const top = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown();
        return top;
    }

    bubbleUp() {
        let i = this.heap.length - 1;

        while (i > 0) {
            let p = Math.floor((i - 1) / 2);
            if (this.heap[p] <= this.heap[i]) break;

            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
            i = p;
        }
    }

    bubbleDown() {
        let i = 0;
        let n = this.heap.length;

        while (true) {
            let left = 2 * i + 1;
            let right = 2 * i + 2;
            let smallest = i;

            if (left < n && this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }
            if (right < n && this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }

            if (smallest === i) break;

            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            i = smallest;
        }
    }
}

class KthLargest {
    constructor(k, nums) {
        this.k = k;
        this.heap = new MinHeap();

        for (let num of nums) {
            this.heap.push(num);
            if (this.heap.size() > k) {
                this.heap.pop();
            }
        }
    }

    add(val) {
        this.heap.push(val);
        if (this.heap.size() > this.k) {
            this.heap.pop();
        }
        return this.heap.peek();
    }
}
