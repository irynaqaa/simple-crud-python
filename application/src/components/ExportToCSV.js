import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import RNFS from 'react-native-fs';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const ExportToCSV = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    db.transaction(tx => {
      tx.executeSql(
        'SELECT * FROM transactions',
        [],
        (tx, results) => {
          const temp = [];
          for (let i = 0; i < results.rows.length; i++) {
            temp.push(results.rows.item(i));
          }
          setTransactions(temp);
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  }, []);

  const handleExportToCSV = () => {
    const csvData = transactions.map(transaction => [
      transaction.date,
      transaction.amount,
      transaction.category,
      transaction.type,
      transaction.description
    ]);
    const csvString = csvData.map(row => row.join(',')).join('
');
    const filePath = RNFS.ExternalStorageDirectoryPath + '/transactions.csv';
    RNFS.writeFile(filePath, csvString, 'utf8')
      .then(() => {
        alert('Transactions exported to CSV successfully');
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <View>
      <Text>Export to CSV</Text>
      <Button title="Export to CSV" onPress={handleExportToCSV} />
    </View>
  );
};

export default ExportToCSV;