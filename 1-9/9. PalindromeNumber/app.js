/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    isPalindrome = x.toString().split("").reverse().join("");
    if (isPalindrome == x.toString()) return true;
    return false;
};

console.log(isPalindrome(121));