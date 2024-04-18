import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Vendors() {
  const [vendors, setVendors] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5555/vendors')
      .then(response => {
        setVendors(response.data);
      })
      .catch(error => console.error('Error fetching vendors:', error));
  }, []);

  return (
    <div>
      <h2>Vendors</h2>
      <ul>
        {vendors.map(vendor => (
          <li key={vendor.id}>{vendor.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Vendors;
