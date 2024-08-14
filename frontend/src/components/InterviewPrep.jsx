import React, { useState } from 'react';

const InterviewPrep = () => {
  const [jobDetails, setJobDetails] = useState({
    company: '',
    field: '',
    position: ''
  });
  const [questions, setQuestions] = useState([]);

  const handleChange = (e) => {
    setJobDetails({ ...jobDetails, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setQuestions([
      "Tell me about yourself.",
      `Why do you want to work at ${jobDetails.company}?`,
      `What experience do you have in ${jobDetails.field}?`,
      `What makes you a good fit for the ${jobDetails.position} role?`,
      "Where do you see yourself in 5 years?"
    ]);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-4 text-center">Interview Preparation</h1>
      <form onSubmit={handleSubmit} className="card space-y-4">
        <input
          type="text"
          name="company"
          value={jobDetails.company}
          onChange={handleChange}
          placeholder="Company"
          className="input"
        />
        <input
          type="text"
          name="field"
          value={jobDetails.field}
          onChange={handleChange}
          placeholder="Field"
          className="input"
        />
        <input
          type="text"
          name="position"
          value={jobDetails.position}
          onChange={handleChange}
          placeholder="Position"
          className="input"
        />
        <button type="submit" className="btn btn-primary w-full">Generate Practice Questions</button>
      </form>
      {questions.length > 0 && (
        <div className="card mt-8">
          <h2 className="text-2xl font-bold mb-4">Practice Questions:</h2>
          <ul className="list-disc pl-5 space-y-2">
            {questions.map((question, index) => (
              <li key={index}>{question}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default InterviewPrep;