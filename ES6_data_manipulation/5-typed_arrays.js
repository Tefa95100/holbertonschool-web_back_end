export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const arrayBuffer = new DataView(new ArrayBuffer(length));
  arrayBuffer.setInt8(position, value);
  return arrayBuffer;
}
