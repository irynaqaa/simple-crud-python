import React, { useState } from 'react';
import { View, TextInput, Picker, DatePicker } from 'react-native';
import Validator from 'react-native-validator';
import SQLite from 'react-native-sqlite-storage';

const AddTransactionForm = () => {
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');

  const validateInput = () => {
    const validationRules = {
      amount: { required: true, numeric: true },
      category: { required: true },
      date: { required: true }
    };

    const errors = Validator.validate({ amount, category, date }, validationRules);

    if (errors) {
      alert('Invalid input');
    } else {
      // Save transaction data to local database
      const db = SQLite.openDatabase({ name: 'transactions.db' });
      db.transaction((tx) => {
        tx.executeSql('INSERT INTO transactions (amount, category, date) VALUES (?, ?, ?)', [amount, category, date]);
      });
    }
  };

  return (
    <View>
      <TextInput
        placeholder="Amount"
        value={amount}
        onChangeText={(text) => setAmount(text)}
      />
      <Picker
        selectedValue={category}
        onValueChange={(itemValue) => setCategory(itemValue)}
      >
        <Picker.Item label="Category" value="" />
        <Picker.Item label="Food" value="food" />
        <Picker.Item label="Transportation" value="transportation" />
      </Picker>
      <DatePicker
        date={date}
        onDateChange={(date) => setDate(date)}
      />
      <Button title="Add Transaction" onPress={validateInput} />
    </View>
  );
};

export default AddTransactionForm;
