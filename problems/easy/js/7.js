/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    var result = 0;
    var sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    while(x > 0) {
        result = result * 10 + x % 10;
        console.log("ans: " + result);
        x = Math.floor(x / 10);
        console.log(x);
    }
    if(result > 2147483647 || result < -2147483648) {
        return 0;
    }
    return result * sign;
};

reverse(-123);