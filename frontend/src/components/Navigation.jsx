import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

function Navigation({ isLoggedIn, setIsLoggedIn }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    setIsLoggedIn(false);
    navigate('/');
  };

  return (
    <nav className="bg-black text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-crimson">JobApp Portfolio</Link>
        <ul className="flex space-x-4">
          {isLoggedIn ? (
            <>
              <li><Link to="/portfolio" className="hover:text-crimson transition duration-200">Portfolio</Link></li>
              <li><Link to="/profile" className="hover:text-crimson transition duration-200">Profile</Link></li>
              <li><Link to="/interview-prep" className="hover:text-crimson transition duration-200">Interview Prep</Link></li>
              <li><Link to="/subscription" className="hover:text-crimson transition duration-200">Subscription</Link></li>
              <li><button onClick={handleLogout} className="hover:text-crimson transition duration-200">Logout</button></li>
            </>
          ) : (
            <>
              <li><Link to="/login" className="hover:text-crimson transition duration-200">Login</Link></li>
              <li><Link to="/register" className="hover:text-crimson transition duration-200">Register</Link></li>
              <li><Link to="/subscription" className="hover:text-crimson transition duration-200">Subscription</Link></li>
            </>
          )}
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;