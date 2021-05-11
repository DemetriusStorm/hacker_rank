/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
const getSecondLargest = (nums) => {
  const sortedArray = nums.sort((a, b) => a - b);
  let secondMaxNumber = sortedArray[sortedArray.length - 1];

  for (let i = sortedArray.length - 1; i > 0; i -= 1) {
    const currentNum = sortedArray[i];
    if (currentNum >= secondMaxNumber) {
    secondMaxNumber = currentNum;
    } else {
      return currentNum;
    }
  }
};
