const mult = function(n, mult_of) {
    let total = 0;
    for (let i = 0; i < n; i++) {
        if (mult_of.some(m => {
            return i % m == 0
        })) {
            total += i;
        }
    }
    console.log(`Sum of all multiples of ${mult_of} in the numbers 1..${n} is: ${total}`);
};

mult(1000, [3,5]);