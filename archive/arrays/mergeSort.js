const mergeSort = (array) => {
  if (array.length <= 1) return array;

  const midpoint = Math.floor(array.length / 2);

  const leftArray = array.slice(0, midpoint);
  const rightArray = array.slice(midpoint);

  const sortedLeft = mergeSort(leftArray);
  const sortedRight = mergeSort(rightArray);
  return merge(sortedLeft, sortedRight);

  console.log(leftArray, rightArray);
  const merged = merge(leftArray, rightArray);
  console.log(merged);
};

const merge = (leftArray, rightArray) => {
  const merged = [];
  while (leftArray.length > 0 && rightArray.length > 0) {
    if (leftArray[0] < rightArray[0]) {
      merged.push(leftArray.shift());
    } else {
      merged.push(rightArray.shift());
    }
  }
  return merged.concat(leftArray, rightArray);
  // return merged.concat(leftArray).concat(rightArray);
};

let array = [1, 2, 3];
array = [5, 2, 9, 3];
console.log(mergeSort(array));
