/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var nums = [-3, 4, 3, 90];
var target = 0;
var twoSum = function(nums, target) {
    var originalNums = JSON.parse(JSON.stringify(nums));
    sortedList = nums.sort(function(a, b){return a-b});
    var answerList = [];
    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (sortedList[i] + sortedList[j] == target) {
                answerList[0] = findIndex(originalNums, sortedList[i], -1);
                answerList[1] = findIndex(originalNums, sortedList[j], answerList[0]);
            }
        }
    }
    return answerList;
};

function findIndex(originalNums, value, existIndex) {
    if (existIndex >= 0) {
        for (var i = 0; i < originalNums.length; i++) {
            if (value == originalNums[i] && existIndex != i) {
                return i;
            }
        }
    }
    else {
        for (var i = 0; i < originalNums.length; i++) {
            if (value == originalNums[i]) {
                return i;
            }
        }
    }
    return -1;
}

function binarySearch(sortedList, target, begin, end) {
var length = end - begin + 1;

    if (end > begin) {
        var mid = Math.floor(length / 2 + begin);
        if (target < sortedList[mid]) {
            return binarySearch(sortedList, target, begin, mid - 1);
        }
        else if (target > sortedList[mid]){
            return binarySearch(sortedList, target, mid + 1, end);
        }
        else { // found it!
            return mid + 1;
        }
    }
    else {
        if (sortedList[end] == target) { // found it!
            return end + 1;
        }
        else {// not found!
            return end + 1;
        }
    }
}