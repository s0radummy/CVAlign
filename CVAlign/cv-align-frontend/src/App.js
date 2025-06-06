
import React from 'react';
import './index.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import UploadForm from './components/UploadForm';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100 p-8">
        <h1 className="text-4xl font-bold mb-6 text-center text-blue-600">CVAlign Evaluator</h1>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/" element={<UploadForm />} /> {}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
