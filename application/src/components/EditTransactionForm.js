import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Picker, Button } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const EditTransactionForm = ({ navigation, route }) => {
  const [amount, setAmount] = useState(route.params.transaction.amount);
  const [category, setCategory] = useState(route.params.transaction.category);
  const [date, setDate] = useState(route.params.transaction.date);
  const [description, setDescription] = useState(route.params.transaction.description);
  const [type, setType] = useState(route.params.transaction.type);

  const handleEditTransaction = () => {
    if (!amount || !category || !date || !description || !type) {
      alert('Please fill in all fields');
      return;
    }

    db.transaction(tx => {
      tx.executeSql(
        'UPDATE transactions SET amount = ?, category = ?, date = ?, description = ?, type = ? WHERE id = ?',
        [amount, category, date, description, type, route.params.transaction.id],
        () => {
          alert('Transaction updated successfully');
          navigation.goBack();
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  };

  return (
    <View>
      <Text>Edit Transaction</Text>
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
      <Button title="Edit Transaction" onPress={handleEditTransaction} />
    </View>
  );
};

export default EditTransactionForm;
