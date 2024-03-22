const containsDuplicate = (nums) => {
    const scanned = {};

    while (nums.length) {
    	console.log(nums);
        const num = nums.pop();
        if (!scanned[num]) {
            scanned[num] = true;
        } else {
        	console.log(num);
            return true;
        }
    }

    return false;
}

const nums = [1,2,3,4];
console.log(containsDuplicate(nums));




// const testFunction = () => {
// 	const nums = [1,2,3];
// 	
// 	while (nums) {
// 		const num = nums.pop();
// 		if (num === 2) return num;	
// 	}
// 	return nums;
// }
// 
// console.log(testFunction());






// var containsDuplicate = function(nums) {
//     // first: brute force / naive approach
//     const scanned = [];
//     let isDup = false;
//     nums.forEach(num=>{
//         if (!isDup && !scanned.includes(num)) {
//             scanned.push(num)
//         } else {
// 					isDup = true;
//         }
//     })
//     return isDup;
// };
// 
// const nums = [1,2,3,1,2];
// 
// console.log(containsDuplicate(nums));

