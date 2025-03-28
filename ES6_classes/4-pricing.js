import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // amount
  get ampount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount === 'number') {
      this._amount = amount;
    } else {
      throw new TypeError('Amount must be a number');
    }
  }

  // Currency
  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (typeof currency === 'string') {
      this._currency = currency;
    } else {
      throw new TypeError('Currency must be a string');
    }
  }

  // Methods
  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  // Static methods
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    if (typeof conversionRate !== 'number') {
      throw new TypeError('ConversionRate must be a number');
    }
    return amount * conversionRate;
  }
}
