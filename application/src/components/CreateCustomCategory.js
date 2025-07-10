import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const CreateCustomCategory = () => {
  const [categoryName, setCategoryName] = useState('');

  const handleCreateCategory = () => {
    if (!categoryName) {
      alert('Please enter a category name');
      return;
    }

    db.transaction(tx => {
      tx.executeSql(
        'INSERT INTO categories (name) VALUES (?)',
        [categoryName],
        () => {
          alert('Category created successfully');
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  };

  return (
    <View>
      <Text>Create Custom Category</Text>
      <TextInput
        placeholder="Category Name"
        value={categoryName}
        onChangeText={text => setCategoryName(text)}
      />
      <Button title="Create Category" onPress={handleCreateCategory} />
    </View>
  );
};

export default CreateCustomCategory;
