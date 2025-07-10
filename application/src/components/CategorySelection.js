import React, { useState, useEffect } from 'react';
import { View, Text, Picker, Button } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const CategorySelection = () => {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');

  useEffect(() => {
    db.transaction(tx => {
      tx.executeSql(
        'SELECT * FROM categories',
        [],
        (tx, results) => {
          const temp = [];
          for (let i = 0; i < results.rows.length; i++) {
            temp.push(results.rows.item(i));
          }
          setCategories(temp);
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  }, []);

  const handleCategorySelection = (category) => {
    setSelectedCategory(category);
  };

  const handleAddCategory = () => {
    db.transaction(tx => {
      tx.executeSql(
        'INSERT INTO categories (name) VALUES (?)',
        [selectedCategory],
        () => {
          alert('Category added successfully');
        },
        (tx, error) => {
          console.error(error);
        }
      );
    });
  };

  return (
    <View>
      <Text>Category Selection</Text>
      <Picker
        selectedValue={selectedCategory}
        onValueChange={itemValue => handleCategorySelection(itemValue)}
      >
        <Picker.Item label="Select Category" value="" />
        {categories.map((category) => (
          <Picker.Item label={category.name} value={category.name} key={category.id} />
        ))}
      </Picker>
      <Button title="Add Category" onPress={handleAddCategory} />
    </View>
  );
};

export default CategorySelection;
