import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import Portfolio from './components/Portfolio';
import Profile from './components/Profile';
import InterviewPrep from './components/InterviewPrep';
import Login from './components/Login';
import Register from './components/Register';
import Subscription from './components/Subscription';
import LandingPage from './components/LandingPage';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userTier, setUserTier] = useState('free');

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <Router>
      <div className="min-h-screen bg-gray-100 flex flex-col">
        <Navigation isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
        <main className="container mx-auto p-4 flex-grow">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<Login setIsLoggedIn={setIsLoggedIn} />} />
            <Route path="/register" element={<Register />} />
            <Route path="/subscription" element={<Subscription setUserTier={setUserTier} />} />
            <Route
              path="/portfolio"
              element={isLoggedIn ? <Portfolio userTier={userTier} /> : <Navigate to="/login" />}
            />
            <Route
              path="/profile"
              element={isLoggedIn ? <Profile /> : <Navigate to="/login" />}
            />
            <Route
              path="/interview-prep"
              element={isLoggedIn ? <InterviewPrep /> : <Navigate to="/login" />}
            />
          </Routes>
        </main>
        <footer className="bg-gray-200 text-center py-4">
          <p>&copy; 2024 Job Application Portfolio. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;