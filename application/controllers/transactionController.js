const db = require('../db');

const getTransactions = async (req, res) => {
  try {
    const transactions = await db.query('SELECT * FROM transactions');
    res.json(transactions);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching transactions' });
  }
};

const createTransaction = async (req, res) => {
  try {
    const { amount, category, date, description, type } = req.body;
    const result = await db.query(
      'INSERT INTO transactions (amount, category, date, description, type) VALUES ($1, $2, $3, $4, $5) RETURNING *',
      [amount, category, date, description, type]
    );
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error creating transaction' });
  }
};

module.exports = { getTransactions, createTransaction };