const db = require('../db');

class Transaction {
  constructor(id, amount, category, date, description, type) {
    this.id = id;
    this.amount = amount;
    this.category = category;
    this.date = date;
    this.description = description;
    this.type = type;
  }

  static async findAll() {
    const results = await db.query('SELECT * FROM transactions');
    return results.map((row) => new Transaction(row.id, row.amount, row.category, row.date, row.description, row.type));
  }

  static async create(amount, category, date, description, type) {
    const result = await db.query(
      'INSERT INTO transactions (amount, category, date, description, type) VALUES ($1, $2, $3, $4, $5) RETURNING *',
      [amount, category, date, description, type]
    );
    return new Transaction(result.id, result.amount, result.category, result.date, result.description, result.type);
  }
}

module.exports = Transaction;