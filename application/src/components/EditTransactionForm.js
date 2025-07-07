import React, { useState } from 'react';
import { View, TextInput, Picker, DatePicker } from 'react-native';

const EditTransactionForm = ({ transaction, onUpdate }) => {
  const [amount, setAmount] = useState(transaction.amount);
  const [category, setCategory] = useState(transaction.category);
  const [date, setDate] = useState(transaction.date);
  const [description, setDescription] = useState(transaction.description);

  const handleUpdate = () => {
    const updatedTransaction = { ...transaction, amount, category, date, description };
    onUpdate(updatedTransaction);
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
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={(text) => setDescription(text)}
      />
      <Button title="Update Transaction" onPress={handleUpdate} />
    </View>
  );
};

export default EditTransactionForm;
