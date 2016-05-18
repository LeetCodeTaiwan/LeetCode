const testProblems = [{
  input: [1, 1, 1],
  output: [1, 1]
}, {
  input: [1, 1, 1, 2, 2, 2, 3],
  output: [1, 1, 2, 2, 3]
}, {
  input: [1, 2, 3, 4, 5, 6, 7],
  output: [1, 2, 3, 4, 5, 6, 7]
}, {
  input: [1, 1, 1, 1],
  output: [1, 1]
}, {
  input: [1, 1, 1, 1, 2],
  output: [1, 1, 2]
}]

var removeDuplicates = function(nums) {
  var indexsToBeRemoved = []
  var deleteMode = false
  var alreadyDelete = 0
  nums.reduce((prev, cur, curIdx) => {
    if (prev === cur && deleteMode) {
      indexsToBeRemoved.push(curIdx)
    } else if (prev === cur) {
      deleteMode = true
    } else {
      deleteMode = false
    }
    return cur
  }, 'x')
  indexsToBeRemoved.map((idx, shift) => nums.splice(idx - shift, 1))
  return nums.length
};

testProblems.map(problem => {
  var answer = removeDuplicates(problem.input)
  console.log(`Answer: ${JSON.stringify(answer)} | Expected: ${JSON.stringify(problem.output)}`)
})
