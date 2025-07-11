const express = require('express');
const router = express.Router();
const db = require('../db');

router.get('/', async (req, res) => {
  try {
    const transactions = await db.query('SELECT * FROM transactions');
    res.json(transactions);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching transactions' });
  }
});

router.post('/', async (req, res) => {
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
});

module.exports = router;