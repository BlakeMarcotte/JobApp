import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

function JobApplicationForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    company_id: '',
    position: '',
    description: '',
    application_date: '',
    status: 'APPLIED',
    salary: '',
    notes: ''
  });

  useEffect(() => {
    if (id) {
      const fetchApplication = async () => {
        try {
          const response = await axios.get(`${import.meta.env.VITE_API_URL}/job-applications/${id}/`);
          setFormData(response.data);
        } catch (error) {
          console.error('Error fetching job application:', error);
        }
      };

      fetchApplication();
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (id) {
        await axios.put(`${import.meta.env.VITE_API_URL}/job-applications/${id}/`, formData);
      } else {
        await axios.post(`${import.meta.env.VITE_API_URL}/job-applications/`, formData);
      }
      navigate('/');
    } catch (error) {
      console.error('Error saving job application:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="company_id" value={formData.company_id} onChange={handleChange} placeholder="Company ID" required />
      <input name="position" value={formData.position} onChange={handleChange} placeholder="Position" required />
      <textarea name="description" value={formData.description} onChange={handleChange} placeholder="Description" />
      <input type="date" name="application_date" value={formData.application_date} onChange={handleChange} required />
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="APPLIED">Applied</option>
        <option value="IN_PROGRESS">In Progress</option>
        <option value="REJECTED">Rejected</option>
        <option value="OFFER">Offer Received</option>
        <option value="ACCEPTED">Offer Accepted</option>
      </select>
      <input type="number" name="salary" value={formData.salary} onChange={handleChange} placeholder="Salary" />
      <textarea name="notes" value={formData.notes} onChange={handleChange} placeholder="Notes" />
      <button type="submit">Save</button>
    </form>
  );
}

export default JobApplicationForm;