import React, { useContext, useEffect } from 'react';
import axios from 'axios';
import InvoiceContext from '../context/InvoiceContext';

const InvoiceList = () => {
  const { invoices, setInvoices, loading, setLoading } = useContext(InvoiceContext);

  useEffect(() => {
    setLoading(true);
    axios.get('http://127.0.0.1:8000/api/invoices/')
      .then(response => {
        setInvoices(response.data.results);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
        setLoading(false);
      });
  }, [setInvoices, setLoading]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Invoice List</h2>
      <ul>
        {invoices.map(invoice => (
          <li key={invoice.id}>Invoice #{invoice.invoice_number} for {invoice.customer_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default InvoiceList;