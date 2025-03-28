export default class Currency {
  constructor(name, code) {
    this._code = code;
    this._name = name;
  }

  // Code
  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code === 'string') {
      this.code = code;
    } else {
      throw new TypeError('Code must be a string');
    }
  }

  // Name
  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
