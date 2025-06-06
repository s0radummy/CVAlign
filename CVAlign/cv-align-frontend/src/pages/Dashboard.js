
import React from 'react';
import UploadForm from './UploadForm';

const Dashboard = () => {
  return (
    <div className="p-8 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Recruiter Dashboard</h1>
      <UploadForm/>

      {}
      <section>
        <h2 className="text-xl font-semibold mb-2">Evaluated Candidates</h2>
        <p className="text-gray-500">Coming soon...</p>
      </section>
    </div>
  );
};

export default Dashboard;
