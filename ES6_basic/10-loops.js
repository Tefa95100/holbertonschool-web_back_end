export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, value] of array) {
    // eslint-disable-next-line no-param-reassign
    array[idx] = appendString + value;
  }

  return array;
}
