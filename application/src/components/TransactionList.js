import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import { getTransactions } from '../db';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      const data = await getTransactions();
      setTransactions(data);
    };
    fetchTransactions();
  }, []);

  const renderItem = ({ item }) => {
    return (
      <TouchableOpacity style={{ padding: 10, borderBottomWidth: 1, borderBottomColor: '#ccc' }}>
        <Text>{item.date}</Text>
        <Text>{item.amount}</Text>
        <Text>{item.description}</Text>
        <Text>{item.category}</Text>
      </TouchableOpacity>
    );
  };

  return (
    <View>
      <FlatList
        data={transactions}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default TransactionList;
