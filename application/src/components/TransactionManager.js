import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList, TextInput, StyleSheet } from 'react-native';

// TransactionManager component to handle adding, viewing, and managing transactions
const TransactionManager = () => {
    const [transactions, setTransactions] = useState([]);
    const [amount, setAmount] = useState('');
    const [category, setCategory] = useState('');
    const [date, setDate] = useState('');
    const [description, setDescription] = useState('');
    const [type, setType] = useState('Income');

    // Function to add a transaction
    const addTransaction = () => {
        if (!amount || !category || !date || !description) {
            alert('Please fill all fields.');
            return;
        }
        const newTransaction = { amount, category, date, description, type };
        setTransactions([...transactions, newTransaction]);
        // Reset fields
        setAmount('');
        setCategory('');
        setDate('');
        setDescription('');
    };

    // Function to render each transaction
    const renderTransaction = ({ item }) => (
        <View style={styles.transactionItem}>
            <Text>{item.date} - {item.description}: ${item.amount} ({item.type})</Text>
        </View>
    );

    return (
        <View>
            <TextInput placeholder="Amount" value={amount} onChangeText={setAmount} keyboardType="numeric" />
            <TextInput placeholder="Category" value={category} onChangeText={setCategory} />
            <TextInput placeholder="Date" value={date} onChangeText={setDate} />
            <TextInput placeholder="Description" value={description} onChangeText={setDescription} />
            <Button title="Add Transaction" onPress={addTransaction} />
            <FlatList data={transactions} renderItem={renderTransaction} keyExtractor={(item, index) => index.toString()} />
        </View>
    );
};

const styles = StyleSheet.create({
    transactionItem: {
        padding: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#ccc'
    }
});

export default TransactionManager;
