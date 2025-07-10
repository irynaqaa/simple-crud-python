import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AddTransaction from './AddTransaction';
import TransactionList from './TransactionList';
import Reports from './Reports';
import Settings from './Settings';

const Tab = createBottomTabNavigator();

const Navigation = () => {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Add Transaction" component={AddTransaction} />
        <Tab.Screen name="Transaction List" component={TransactionList} />
        <Tab.Screen name="Reports" component={Reports} />
        <Tab.Screen name="Settings" component={Settings} />
      </Tab.Navigator>
    </NavigationContainer>
  );
};

export default Navigation;