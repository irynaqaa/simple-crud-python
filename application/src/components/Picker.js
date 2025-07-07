import React from 'react';
import { Picker as RNPickerr } from 'react-native';

const Picker = ({ selectedValue, onValueChange }) => {
  return (
    <RNPickerr
      selectedValue={selectedValue}
      onValueChange={onValueChange}
    >
      <RNPickerr.Item label="Category" value="" />
      <RNPickerr.Item label="Food" value="food" />
      <RNPickerr.Item label="Transportation" value="transportation" />
    </RNPickerr>
  );
};

export default Picker;