import React, { useState } from 'react';

const JobForm = ({ addJob, setShowForm }) => {
  const [job, setJob] = useState({
    company: '', position: '', location: '', time: '', description: '', importantPeople: ''
  });

  const handleChange = (e) => setJob({ ...job, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    addJob(job);
    setJob({ company: '', position: '', location: '', time: '', description: '', importantPeople: '' });
    setShowForm(false);
  };

  return (
    <form onSubmit={handleSubmit} className="card space-y-4">
      <input
        type="text" name="company" value={job.company} onChange={handleChange}
        placeholder="Company" className="input"
      />
      <input
        type="text" name="position" value={job.position} onChange={handleChange}
        placeholder="Position" className="input"
      />
      <div className="flex space-x-4">
        <input
          type="text" name="location" value={job.location} onChange={handleChange}
          placeholder="Location" className="input flex-1"
        />
        <input
          type="text" name="time" value={job.time} onChange={handleChange}
          placeholder="Time" className="input flex-1"
        />
      </div>
      <textarea
        name="description" value={job.description} onChange={handleChange}
        placeholder="Description" className="input h-24"
      />
      <textarea
        name="importantPeople" value={job.importantPeople} onChange={handleChange}
        placeholder="Important People" className="input h-24"
      />
      <div className="flex space-x-2">
        <button type="submit" className="btn btn-primary">Add Job</button>
        <button type="button" className="btn btn-secondary" onClick={() => setShowForm(false)}>Cancel</button>
      </div>
    </form>
  );
};

const JobList = ({ jobs }) => (
  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {jobs.map((job, index) => (
      <div key={index} className="card">
        <h3 className="text-xl font-bold text-crimson">{job.position}</h3>
        <p className="text-gray-600">{job.company}</p>
        <p className="text-sm text-gray-500">{job.location} - {job.time}</p>
        <p className="mt-2 text-sm">{job.description}</p>
        <p className="mt-2 text-sm"><strong>Important People:</strong> {job.importantPeople}</p>
      </div>
    ))}
  </div>
);

const Portfolio = ({ userTier }) => {
  const [jobs, setJobs] = useState([]);
  const [showForm, setShowForm] = useState(false);

  const addJob = (job) => setJobs([...jobs, job]);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4 text-center">Job Application Portfolio</h1>
      <p className="text-center mb-4">Current Plan: <span className="capitalize font-bold">{userTier}</span></p>
      {!showForm && (
        <div className="text-center mb-8">
          <button onClick={() => setShowForm(true)} className="btn btn-primary">
            Add New Job
          </button>
        </div>
      )}
      {showForm && <JobForm addJob={addJob} setShowForm={setShowForm} />}
      <JobList jobs={jobs} />
    </div>
  );
};

export default Portfolio;