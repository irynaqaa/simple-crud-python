import React from 'react';
import { View, TextInput, Button, StyleSheet } from 'react-native';

// AddTransactionForm component to handle adding a new transaction
const AddTransactionForm = ({ onAddTransaction }) => {
    const [amount, setAmount] = React.useState('');
    const [category, setCategory] = React.useState('');
    const [date, setDate] = React.useState('');
    const [description, setDescription] = React.useState('');
    const [type, setType] = React.useState('Income');

    const handleSubmit = () => {
        onAddTransaction({ amount, category, date, description, type });
        // Reset fields
        setAmount('');
        setCategory('');
        setDate('');
        setDescription('');
    };

    return (
        <View>
            <TextInput placeholder="Amount" value={amount} onChangeText={setAmount} keyboardType="numeric" />
            <TextInput placeholder="Category" value={category} onChangeText={setCategory} />
            <TextInput placeholder="Date" value={date} onChangeText={setDate} />
            <TextInput placeholder="Description" value={description} onChangeText={setDescription} />
            <Button title="Add Transaction" onPress={handleSubmit} />
        </View>
    );
};

const styles = StyleSheet.create({
    // Add styles here
});

export default AddTransactionForm;
