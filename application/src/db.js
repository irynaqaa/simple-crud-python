import SQLite from 'react-native-sqlite-storage';

const db = SQLite.openDatabase({ name: 'transactions.db' }, () => {
  console.log('Database opened');
}, (err) => {
  console.error('Error opening database: ', err);
});

const createTable = () => {
  db.transaction((tx) => {
    tx.executeSql(`
      CREATE TABLE IF NOT EXISTS transactions
      (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, amount REAL, description TEXT, category TEXT);
    `);
  });
};

const insertTransaction = (transaction) => {
  db.transaction((tx) => {
    tx.executeSql(`
      INSERT INTO transactions (date, amount, description, category) VALUES (?, ?, ?, ?);
    `, [transaction.date, transaction.amount, transaction.description, transaction.category]);
  });
};

const getTransactions = () => {
  return new Promise((resolve, reject) => {
    db.transaction((tx) => {
      tx.executeSql('SELECT * FROM transactions;', [], (_, { rows }) => {
        resolve(rows._array);
      });
    }, (err) => {
      reject(err);
    });
  });
};

export { createTable, insertTransaction, getTransactions };
