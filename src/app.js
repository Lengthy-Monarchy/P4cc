import React from 'react';
import Vendors from './components/Vendors';
import Sweets from './components/Sweets';
import AddVendorSweet from './components/AddVendorSweet';

function App() {
  return (
    <div className="App">
      <h1>Sweets Vendors App</h1>
      <Vendors />
      <Sweets />
      <AddVendorSweet />
    </div>
  );
}

export default App;
