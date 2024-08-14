import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold mb-4">Welcome to Job Application Portfolio</h1>
      <p className="mb-4">Track your job applications, prepare for interviews, and manage your career journey.</p>
      <div className="space-x-4">
        <Link to="/login" className="bg-crimson text-white px-4 py-2 rounded hover:bg-red-700">Login</Link>
        <Link to="/subscription" className="bg-black text-white px-4 py-2 rounded hover:bg-gray-800">View Subscriptions</Link>
      </div>
    </div>
  );
};

export default LandingPage;