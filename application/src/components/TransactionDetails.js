import React from 'react';
import { View, Text } from 'react-native';

const TransactionDetails = ({ navigation, route }) => {
  return (
    <View>
      <Text>Transaction Details</Text>
      <Text>Date: {route.params.transaction.date}</Text>
      <Text>Amount: {route.params.transaction.amount}</Text>
      <Text>Category: {route.params.transaction.category}</Text>
      <Text>Type: {route.params.transaction.type}</Text>
      <Text>Description: {route.params.transaction.description}</Text>
    </View>
  );
};

export default TransactionDetails;
