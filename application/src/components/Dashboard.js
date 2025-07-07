import React from 'react';
import { View, Text } from 'react-native';
import { Line } from 'react-native-chartjs';

const Dashboard = () => {
  return (
    <View>
      <Text>Dashboard</Text>
      <Line
        data={{
          labels: ['January', 'February', 'March'],
          datasets: [
            {
              label: 'Expenses',
              data: [100, 200, 300],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
            },
          ],
        }}
        options={{
          title: {
            display: true,
            text: 'Expenses',
          },
        }}
      />
    </View>
  );
};

export default Dashboard;