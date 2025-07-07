import React, { useState, useEffect } from 'react';
import { View, Picker } from 'react-native';
import { getCategories } from '../db';

const CategorySelection = () => {
  const [category, setCategory] = useState('');
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      const data = await getCategories();
      setCategories(data);
    };
    fetchCategories();
  }, []);

  const handleCategoryChange = (itemValue) => {
    setCategory(itemValue);
  };

  return (
    <View>
      <Picker
        selectedValue={category}
        onValueChange={handleCategoryChange}
      >
        <Picker.Item label="Select a category" value="" />
        {categories.map((category) => (
          <Picker.Item label={category.name} value={category.name} key={category.id} />
        ))}
      </Picker>
    </View>
  );
};

export default CategorySelection;
