import React from 'react';
import { DatePicker as RNDatePicker } from 'react-native';

const DatePicker = ({ date, onDateChange }) => {
  return (
    <RNDatePicker
      date={date}
      onDateChange={onDateChange}
    />
  );
};

export default DatePicker;