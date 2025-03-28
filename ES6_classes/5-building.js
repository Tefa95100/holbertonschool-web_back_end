export default class Building {
    constructor(sqft) {
        this._sqft = sqft;
    
        if (this.constructor !== Building
          && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
          throw new Error('Class extending Building must override evacuationWarningMessage');
        }
      }

  // Sqft
  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    if (typeof sqft === 'number') {
      this._sqft = sqft;
    } else {
      throw new TypeError('Sqft must be a number');
    }
  }

  // eslint-disable-next-line
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
