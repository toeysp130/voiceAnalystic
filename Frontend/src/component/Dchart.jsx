import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
ChartJS.register(ArcElement, Tooltip, Legend);

const Dchart = ({ sentiment }) => {
  return <Doughnut data={getData(sentiment)} />;
}


function getData(sentiment) {

  return {
    labels: ['Pos', 'Neu', 'Nag'],
    datasets: [
      {
        label: '# of Score',
        data: [sentiment.pos, sentiment.neu, sentiment.neg],
        backgroundColor: [
          'rgba(90, 210, 25, 0.5)',
          'rgba(240, 230, 35, 0.5)',
          'rgba(235, 35, 35, 0.5)',
        ],
        borderColor: [
          'rgba(90, 210, 25, 1)',
          'rgba(240, 230, 35, 1)',
          'rgba(235, 35, 35, 1)',
        ],
        borderWidth: 1,
      },
    ],
    options: {
      plugins: {
          title: {
              display: true,
              text: 'Custom Chart Title'
          }
      }
  }
  }

}


export default Dchart

export const data = {
  labels: ['Pos', 'Neu', 'Nag'],
  datasets: [
    {
      label: '# of Score',
      data: [12, 25, 30],
      backgroundColor: [
        'rgba(90, 210, 25, 0.5)',
        'rgba(240, 230, 35, 0.5)',
        'rgba(235, 35, 35, 0.5)',
      ],
      borderColor: [
        'rgba(90, 210, 25, 1)',
        'rgba(240, 230, 35, 1)',
        'rgba(235, 35, 35, 1)',
      ],
      borderWidth: 1,
    },
  ],
};
