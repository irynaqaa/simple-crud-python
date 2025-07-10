import React, { useState, useEffect } from 'react';
import { View, Text, FlatList } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const Dashboard = () => {
  const [transactions, setTransactions] = useState([]);
  const [totalIncome, setTotalIncome] = useState(0);
  const [totalExpenses, setTotalExpenses] = useState(0);
  const [balance, setBalance] = useState(0);

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

  useEffect(() => {
    let totalIncome = 0;
    let totalExpenses = 0;
    transactions.forEach((transaction) => {
      if (transaction.type === 'income') {
        totalIncome += transaction.amount;
      } else {
        totalExpenses += transaction.amount;
      }
    });
    setTotalIncome(totalIncome);
    setTotalExpenses(totalExpenses);
    setBalance(totalIncome - totalExpenses);
  }, [transactions]);

  const renderItem = ({ item }) => {
    return (
      <View>
        <Text>Date: {item.date}</Text>
        <Text>Amount: {item.amount}</Text>
        <Text>Category: {item.category}</Text>
        <Text>Type: {item.type}</Text>
      </View>
    );
  };

  return (
    <View>
      <Text>Dashboard</Text>
      <Text>Total Income: {totalIncome}</Text>
      <Text>Total Expenses: {totalExpenses}</Text>
      <Text>Balance: {balance}</Text>
      <FlatList
        data={transactions}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default Dashboard;
