export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, value] of array.entries()) {
    /* eslint-disable-next-line no-param-reassign, no-console */
    array[idx] = appendString + value;
  }

  return array;
}
