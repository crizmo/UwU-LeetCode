/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    const com = {};
    for(let i=0; i < nums.length; i++){
        if(com[ nums[i] ]>=0){
            return [ com[nums[i] ] , i]
        }
        com[target-nums[i]] = i
    }
};