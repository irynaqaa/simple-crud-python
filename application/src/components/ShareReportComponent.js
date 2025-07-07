import React, { useState } from 'react';
import { View, Button } from 'react-native';
import Share from 'react-native-share';

const ShareReport = () => {
  const [report, setReport] = useState('');

  const handleShare = async () => {
    try {
      const shareOptions = {
        title: 'Share Report',
        message: report,
        url: 'https://example.com',
        subject: 'Report',
      };
      await Share.open(shareOptions);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View>
      <Button title="Share Report" onPress={handleShare} />
    </View>
  );
};

export default ShareReport;