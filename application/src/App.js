import React from 'react';
import { View, Text } from 'react-native';
import TransactionForm from './components/TransactionForm';
import TransactionList from './components/TransactionList';

const App = () => {
  return (
    <View>
      <TransactionForm />
      <TransactionList />
    </View>
  );
};

export default App;
