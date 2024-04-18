import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Sweets() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5555/sweets')
      .then(response => {
        setSweets(response.data);
      })
      .catch(error => console.error('Error fetching sweets:', error));
  }, []);

  return (
    <div>
      <h2>Sweets</h2>
      <ul>
        {sweets.map(sweet => (
          <li key={sweet.id}>{sweet.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Sweets;
