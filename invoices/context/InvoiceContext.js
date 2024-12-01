import React, { createContext, useState } from "react";

const InvoiceContext = createContext();

export const InvoiceProvider = ({ children }) => {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(false);

  return (
    <InvoiceContext.Provider value={{ invoices, setInvoices, loading, setLoading }}>
      {children}
    </InvoiceContext.Provider>
  );
};

export default InvoiceContext;