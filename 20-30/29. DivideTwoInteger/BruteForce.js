/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
 var divide = function(dividend, divisor) {
    let sign = (dividend < 0 || divisor < 0)  ? -1 : 1
    if (dividend < 0 && divisor < 0) sign = 1

    if (divisor === 0 || dividend === 0) return 0

    if (dividend > 2147483648) return 2147483647 * sign
    else if (dividend <= -2147483648 && divisor === -1) return 2147483647
    
    dividend = Math.abs(dividend) , divisor = Math.abs(divisor)   

    let step = 0
    while (dividend >= divisor)
    {
        dividend = dividend - divisor
        step++
    }

    return step * sign
};

console.log(divide(-2147483648,-1))