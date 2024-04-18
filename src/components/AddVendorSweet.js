import React, { useState } from 'react';
import axios from 'axios';

function AddVendorSweet() {
  const [price, setPrice] = useState('');
  const [vendorId, setVendorId] = useState('');
  const [sweetId, setSweetId] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();  // Prevents the default form submission behavior
    axios.post('http://localhost:5555/vendor_sweets', {
      price,
      vendor_id: vendorId,
      sweet_id: sweetId
    })
    .then(response => {
      alert('VendorSweet added successfully!');
      // Reset the form fields after successful submission
      setPrice('');
      setVendorId('');
      setSweetId('');
    })
    .catch(error => {
      alert('Failed to add VendorSweet');
      console.error('Error:', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Vendor Sweet Association</h2>
      <div>
        <label>
          Price:
          <input 
            type="number" 
            value={price} 
            onChange={e => setPrice(e.target.value)} 
            required 
          />
        </label>
      </div>
      <div>
        <label>
          Vendor ID:
          <input 
            type="number" 
            value={vendorId} 
            onChange={e => setVendorId(e.target.value)} 
            required 
          />
        </label>
      </div>
      <div>
        <label>
          Sweet ID:
          <input 
            type="number" 
            value={sweetId} 
            onChange={e => setSweetId(e.target.value)} 
            required 
          />
        </label>
      </div>
      <button type="submit">Add Association</button>
    </form>
  );
}

export default AddVendorSweet;
