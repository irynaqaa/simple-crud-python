import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

// TransactionList component to display a list of transactions
const TransactionList = ({ transactions }) => {
    // Function to render each transaction
    const renderTransaction = ({ item }) => (
        <View style={styles.transactionItem}>
            <Text>{item.date} - {item.description}: ${item.amount} ({item.type})</Text>
        </View>
    );

    return (
        <FlatList data={transactions} renderItem={renderTransaction} keyExtractor={(item, index) => index.toString()} />
    );
};

const styles = StyleSheet.create({
    transactionItem: {
        padding: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#ccc'
    }
});

export default TransactionList;
