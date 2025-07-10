import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import Share from 'react-native-share';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const ShareReports = () => {
  const [transactions, setTransactions] = useState([]);
  const [report, setReport] = useState('');

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

  const handleShareReport = () => {
    const reportData = transactions.map((transaction) => {
      return `${transaction.date},${transaction.amount},${transaction.category},${transaction.type}`;
    }).join('
');
    const shareOptions = {
      title: 'Share Report',
      message: 'Share your expense report',
      url: `data:text/csv;charset=utf-8,${reportData}`,
      subject: 'Expense Report',
    };
    Share.open(shareOptions)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        err && console.log(err);
      });
  };

  return (
    <View>
      <Text>Share Reports</Text>
      <Button title="Share Report" onPress={handleShareReport} />
    </View>
  );
};

export default ShareReports;
