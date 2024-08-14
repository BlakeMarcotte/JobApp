import React from 'react';
import { useNavigate } from 'react-router-dom';

const Subscription = ({ setUserTier }) => {
  const navigate = useNavigate();

  const handleSubscribe = (tier) => {
    setUserTier(tier);
    navigate('/');
  };

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h2 className="text-3xl mb-6 text-center font-bold">Choose Your Subscription</h2>
      <div className="flex justify-between">
        {['free', 'plus', 'pro'].map((tier) => (
          <div key={tier} className="w-1/3 p-4">
            <div className="bg-white shadow-md rounded-lg p-6">
              <h3 className="text-xl font-bold mb-4 capitalize">{tier}</h3>
              <p className="mb-4">
                {tier === 'free' && 'Basic features'}
                {tier === 'plus' && 'Advanced features'}
                {tier === 'pro' && 'All features included'}
              </p>
              <button
                onClick={() => handleSubscribe(tier)}
                className="bg-crimson hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
              >
                {tier === 'free' ? 'Select' : 'Subscribe'}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Subscription;