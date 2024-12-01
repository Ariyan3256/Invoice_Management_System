import React, { useState } from 'react';
import axios from 'axios';

const CreateInvoice = () => {
  const [invoice, setInvoice] = useState({
    invoice_number: '',
    customer_name: '',
    date: '',
    details: []
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:8000/api/invoices/', invoice)
      .then(response => {
        console.log('Invoice created:', response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={invoice.invoice_number}
        onChange={e => setInvoice({ ...invoice, invoice_number: e.target.value })}
        placeholder="Invoice Number"
        required
      />
      <input
        type="text"
        value={invoice.customer_name}
        onChange={e => setInvoice({ ...invoice, customer_name: e.target.value })}
        placeholder="Customer Name"
        required
      />
      <input
        type="date"
        value={invoice.date}
        onChange={e => setInvoice({ ...invoice, date: e.target.value })}
        required
      />
      <button type="submit">Create Invoice</button>
    </form>
  );
};

export default CreateInvoice;