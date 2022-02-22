/**
 * @param {string} s
 * @return {number}
 */
 var romanToInt = function(s) {
    const map = new Map([
        ['I' , 1],        
        ['IV' , 4],
        ['V' , 5],
        ['IX', 9],
        ['X', 10],
        ['XL', 40],
        ['L', 50],
        ['XC', 90],
        ['C', 100],        
        ['CD', 400],
        ['D', 500],        
        ['CM', 900],
        ['M', 1000]
    ]);

    let number = 0
    
    for (let i = 0 ; i < s.length ; i++)
    {
        value = map.get(s[i] + s[i+1]);
        if (value) i = i + 1 
        else {
            value = map.get(s[i])
        } 

        number += value
    }

    return number
};