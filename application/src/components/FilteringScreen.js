import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const FilteringScreen = () => {
  const [transactions, setTransactions] = useState([]);
  const [filter, setFilter] = useState('');
  const [sort, setSort] = useState('asc');

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

  const handleFilter = (filterType) => {
    setFilter(filterType);
    db.transaction(tx => {
      tx.executeSql(
        `SELECT * FROM transactions WHERE type = ?`,
        [filterType],
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
  };

  const handleSort = (sortType) => {
    setSort(sortType);
    if (sortType === 'asc') {
      transactions.sort((a, b) => a.amount - b.amount);
    } else {
      transactions.sort((a, b) => b.amount - a.amount);
    }
    setTransactions([...transactions]);
  };

  const renderItem = ({ item }) => {
    return (
      <TouchableOpacity>
        <View>
          <Text>Date: {item.date}</Text>
          <Text>Amount: {item.amount}</Text>
          <Text>Category: {item.category}</Text>
          <Text>Type: {item.type}</Text>
        </View>
      </TouchableOpacity>
    );
  };

  return (
    <View>
      <Text>Filtering Screen</Text>
      <FlatList
        data={transactions}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
      />
      <TouchableOpacity onPress={() => handleFilter('income')}>
        <Text>Filter by Income</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => handleFilter('expense')}>
        <Text>Filter by Expense</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => handleSort('asc')}>
        <Text>Sort by Ascending</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => handleSort('desc')}>
        <Text>Sort by Descending</Text>
      </TouchableOpacity>
    </View>
  );
};

export default FilteringScreen;
