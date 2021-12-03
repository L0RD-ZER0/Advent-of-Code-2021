/*

--- Part Two ---

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

*/

const readFileSync = require("fs").readFileSync;

// Type: string
const input = readFileSync('./Input-1.txt', 'utf8');  // Input hasn't changed

// Type: number[]
const data = input.split('\n').map(Number);

// Returns result; True = Increased; False = decrased; undefined = N/A
function chart_depths(data) {
    let depths = [];
    let lastWindow, thisWindow;
    for (let i = 0; i < data.length - 2; i++) {
        thisWindow = data[i] + data[i + 1] + data[i + 2];
        if (i===0) {
            depths.push('N/A');
        } else {
            let comparison;
            
            if (thisWindow === lastWindow) {
                comparison = 'Same';
            } else if (thisWindow > lastWindow) {
                comparison = 'Increased';
            } else if (thisWindow < lastWindow) {
                comparison = 'Decreased';
            }
            depths.push( comparison );
        }
        lastWindow = thisWindow;
    }
    return depths;
}

// Returns count of elements in an array
function count(data) {
    let counts = {};
    for (let i = 0; i < data.length; i++) {
        counts[data[i]] = counts[data[i]] ? counts[data[i]] + 1 : 1;
    }
    return counts;
}

console.log(count(chart_depths(data)));
