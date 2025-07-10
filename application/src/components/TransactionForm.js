import React, { useState } from 'react';
import { View, Text, TextInput, Picker, Button } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const TransactionForm = () => {
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');
  const [description, setDescription] = useState('');
  const [type, setType] = useState('');

  const handleAddTransaction = () => {
    if (!amount || !category || !date || !description || !type) {
      alert('Please fill in all fields');
      return;
    }

    db.transaction(tx => {
      tx.executeSql(
        'INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)',
        [amount, category, date, description, type],
        () => {
          alert('Transaction added successfully');
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  };

  return (
    <View>
      <Text>Add Transaction</Text>
      <TextInput
        placeholder="Amount"
        value={amount}
        onChangeText={text => setAmount(text)}
      />
      <Picker
        selectedValue={category}
        onValueChange={itemValue => setCategory(itemValue)}
      >
        <Picker.Item label="Select Category" value="" />
        <Picker.Item label="Food" value="food" />
        <Picker.Item label="Transportation" value="transportation" />
        <Picker.Item label="Entertainment" value="entertainment" />
      </Picker>
      <TextInput
        placeholder="Date"
        value={date}
        onChangeText={text => setDate(text)}
      />
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={text => setDescription(text)}
      />
      <Picker
        selectedValue={type}
        onValueChange={itemValue => setType(itemValue)}
      >
        <Picker.Item label="Select Type" value="" />
        <Picker.Item label="Income" value="income" />
        <Picker.Item label="Expense" value="expense" />
      </Picker>
      <Button title="Add Transaction" onPress={handleAddTransaction} />
    </View>
  );
};

export default TransactionForm;
