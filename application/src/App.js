import React from 'react';
import TransactionManager from './components/TransactionManager';

// Main App component that renders the Transaction Manager
const App = () => {
    return (
        <div>
            <h1>Personal Expense Tracker</h1>
            <TransactionManager />
        </div>
    );
};

export default App;
