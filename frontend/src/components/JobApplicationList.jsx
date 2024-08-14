import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function JobApplicationList() {
  const [applications, setApplications] = useState([]);

  useEffect(() => {
    const fetchApplications = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/job-applications/`);
        setApplications(response.data);
      } catch (error) {
        console.error('Error fetching job applications:', error);
      }
    };

    fetchApplications();
  }, []);

  return (
    <div>
      <h1>Job Applications</h1>
      <Link to="/add">Add New Application</Link>
      <ul>
        {applications.map(app => (
          <li key={app.id}>
            {app.position} at {app.company.name} - {app.status}
            <Link to={`/edit/${app.id}`}>Edit</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default JobApplicationList;