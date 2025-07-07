import React, { useState, useEffect } from 'react';
import { View, Text, Picker, Modal } from 'react-native';
import _ from 'lodash';
import { getTransactions } from '../db';

const FilteringComponent = () => {
  const [transactions, setTransactions] = useState([]);
  const [filteredTransactions, setFilteredTransactions] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    const fetchTransactions = async () => {
      const data = await getTransactions();
      setTransactions(data);
    };
    fetchTransactions();
  }, []);

  const handleCategoryChange = (itemValue) => {
    setSelectedCategory(itemValue);
    const filteredData = _.filter(transactions, (transaction) => transaction.category === itemValue);
    setFilteredTransactions(filteredData);
  };

  return (
    <View>
      <Picker
        selectedValue={selectedCategory}
        onValueChange={handleCategoryChange}
      >
        <Picker.Item label="Select a category" value="" />
        <Picker.Item label="Food" value="food" />
        <Picker.Item label="Transportation" value="transportation" />
      </Picker>
      <Modal
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View>
          <Text>Filtered Transactions:</Text>
          {filteredTransactions.map((transaction) => (
            <Text key={transaction.id}>{transaction.date} - {transaction.amount}</Text>
          ))}
        </View>
      </Modal>
      <Button title="Show Filtered Transactions" onPress={() => setModalVisible(true)} />
    </View>
  );
};

export default FilteringComponent;
