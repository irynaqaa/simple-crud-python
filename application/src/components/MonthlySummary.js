import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

// MonthlySummary component to display total income, expenses, and balance
const MonthlySummary = ({ transactions }) => {
    const totalIncome = transactions
        .filter(t => t.type === 'Income')
        .reduce((acc, t) => acc + parseFloat(t.amount), 0);
    const totalExpenses = transactions
        .filter(t => t.type === 'Expense')
        .reduce((acc, t) => acc + parseFloat(t.amount), 0);
    const balance = totalIncome - totalExpenses;

    return (
        <View style={styles.summaryContainer}>
            <Text>Total Income: ${totalIncome}</Text>
            <Text>Total Expenses: ${totalExpenses}</Text>
            <Text>Balance: ${balance}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    summaryContainer: {
        padding: 10,
        backgroundColor: '#f9f9f9',
        borderRadius: 5,
        marginVertical: 10
    }
});

export default MonthlySummary;
