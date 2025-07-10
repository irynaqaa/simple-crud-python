import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expense_tracker.db' });

const DeleteTransaction = ({ navigation, route }) => {
  const handleDeleteTransaction = () => {
    db.transaction(tx => {
      tx.executeSql(
        'DELETE FROM transactions WHERE id = ?',
        [route.params.transaction.id],
        () => {
          alert('Transaction deleted successfully');
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
      <Text>Delete Transaction</Text>
      <Button title="Delete Transaction" onPress={handleDeleteTransaction} />
    </View>
  );
};

export default DeleteTransaction;
