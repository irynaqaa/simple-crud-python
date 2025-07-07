import React, { useState, useEffect } from 'react';
import { View, Button } from 'react-native';
import { getTransactions } from '../db';
import { CSV } from 'react-native-csv';
import { writeFile } from 'react-native-fs';

const ExportToCSV = () => {
  const [transactions, setTransactions] = useState([]);
  const [csvData, setCsvData] = useState('');

  useEffect(() => {
    const fetchTransactions = async () => {
      const data = await getTransactions();
      setTransactions(data);
    };
    fetchTransactions();
  }, []);

  const handleExport = async () => {
    const csv = new CSV();
    const data = transactions.map((transaction) => [
      transaction.date,
      transaction.amount,
      transaction.description,
    ]);
    const csvData = csv.stringify(data);
    setCsvData(csvData);
    await writeFile('transactions.csv', csvData);
  };

  return (
    <View>
      <Button title="Export to CSV" onPress={handleExport} />
    </View>
  );
};

export default ExportToCSV;
