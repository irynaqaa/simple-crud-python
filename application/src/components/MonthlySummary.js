import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import { getTransactions } from '../db';
import moment from 'moment';
import Chart from 'react-native-chartjs';

const MonthlySummary = () => {
  const [transactions, setTransactions] = useState([]);
  const [totalIncome, setTotalIncome] = useState(0);
  const [totalExpenses, setTotalExpenses] = useState(0);
  const [balance, setBalance] = useState(0);
  const [currentMonth, setCurrentMonth] = useState(moment().format('MMMM'));

  useEffect(() => {
    const fetchTransactions = async () => {
      const data = await getTransactions();
      setTransactions(data);
    };
    fetchTransactions();
  }, []);

  useEffect(() => {
    const calculateSummary = () => {
      const filteredTransactions = transactions.filter((transaction) => moment(transaction.date).format('MMMM') === currentMonth);
      const income = filteredTransactions.filter((transaction) => transaction.amount > 0);
      const expenses = filteredTransactions.filter((transaction) => transaction.amount < 0);
      const totalIncome = income.reduce((acc, curr) => acc + curr.amount, 0);
      const totalExpenses = expenses.reduce((acc, curr) => acc + curr.amount, 0);
      const balance = totalIncome + totalExpenses;
      setTotalIncome(totalIncome);
      setTotalExpenses(totalExpenses);
      setBalance(balance);
    };
    calculateSummary();
  }, [transactions, currentMonth]);

  const chartData = {
    labels: ['Income', 'Expenses'],
    datasets: [
      {
        label: 'Monthly Summary',
        data: [totalIncome, totalExpenses],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <View>
      <Text>Monthly Summary for {currentMonth}</Text>
      <Text>Total Income: {totalIncome}</Text>
      <Text>Total Expenses: {totalExpenses}</Text>
      <Text>Balance: {balance}</Text>
      <Chart
        type="pie"
        data={chartData}
        options={{
          title: {
            display: true,
            text: 'Monthly Summary',
          },
        }}
      />
    </View>
  );
};

export default MonthlySummary;
