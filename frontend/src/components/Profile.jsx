import React, { useState } from 'react';

const Profile = () => {
  const [profile, setProfile] = useState({
    name: '',
    email: '',
    phone: '',
    resume: '',
    coverLetter: '',
    about: ''
  });

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Profile saved:', profile);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-4 text-center">Your Profile</h1>
      <form onSubmit={handleSubmit} className="card space-y-4">
        <input
          type="text"
          name="name"
          value={profile.name}
          onChange={handleChange}
          placeholder="Full Name"
          className="input"
        />
        <input
          type="email"
          name="email"
          value={profile.email}
          onChange={handleChange}
          placeholder="Email"
          className="input"
        />
        <input
          type="tel"
          name="phone"
          value={profile.phone}
          onChange={handleChange}
          placeholder="Phone"
          className="input"
        />
        <textarea
          name="resume"
          value={profile.resume}
          onChange={handleChange}
          placeholder="Paste your resume here"
          className="input h-40"
        />
        <textarea
          name="coverLetter"
          value={profile.coverLetter}
          onChange={handleChange}
          placeholder="Paste your cover letter template here"
          className="input h-40"
        />
        <textarea
          name="about"
          value={profile.about}
          onChange={handleChange}
          placeholder="Tell us about yourself"
          className="input h-40"
        />
        <button type="submit" className="btn btn-primary w-full">Save Profile</button>
      </form>
    </div>
  );
};

export default Profile;