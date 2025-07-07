import React from 'react';
import FilteringComponent from './components/FilteringComponent';
import AddTransactionForm from './components/AddTransactionForm';
import TransactionList from './components/TransactionList';
import MonthlySummary from './components/MonthlySummary';
import ExportToCSV from './components/ExportToCSV';
import ShareReportComponent from './components/ShareReportComponent';
import Dashboard from './components/Dashboard';

const App = () => {
  const [amount, setAmount] = React.useState('');
  const [category, setCategory] = React.useState('');
  const [date, setDate] = React.useState('');

  const validateInput = () => {
    const validationRules = {
      amount: { required: true, numeric: true },
      category: { required: true },
      date: { required: true }
    };

    const errors = Validator.validate({ amount, category, date }, validationRules);

    if (errors) {
      alert('Invalid input');
    } else {
      // Save transaction data to local database
      const db = SQLite.openDatabase({ name: 'transactions.db' });
      db.transaction((tx) => {
        tx.executeSql('INSERT INTO transactions (amount, category, date) VALUES (?, ?, ?)', [amount, category, date]);
      });
    }
  };

  return (
    <>
      <FilteringComponent />
      <AddTransactionForm />
      <TransactionList />
      <MonthlySummary />
      <ExportToCSV />
      <ShareReportComponent />
      <Dashboard />
      <TextInput
        placeholder="Amount"
        value={amount}
        onChangeText={(text) => setAmount(text)}
      />
      <Picker
        selectedValue={category}
        onValueChange={(itemValue) => setCategory(itemValue)}
      >
        <Picker.Item label="Category" value="" />
        <Picker.Item label="Food" value="food" />
        <Picker.Item label="Transportation" value="transportation" />
      </Picker>
      <DatePicker
        date={date}
        onDateChange={(date) => setDate(date)}
      />
      <Button title="Add Transaction" onPress={validateInput} />
    </>
  );
};

export default App;