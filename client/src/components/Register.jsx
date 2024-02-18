import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useHistory } from 'react-router-dom';
import Loading from './Loading';
const Register = () => {
  const apiUrl = import.meta.env.VITE_APP_API_URL;

  const [isLoading, setIsLoading] = useState(false);

  const history = useHistory();

  const { login } = useAuth();

  const [formData, setFormData] = useState({
    username: '',
    password: '',
    class_: 'Warrior',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true)
    try {
      const response = await fetch(apiUrl + '/character', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },  
        body: JSON.stringify(formData),
        credentials: 'include',
      });
      setIsLoading(false)
      if (response.ok) {
        login();
        history.push('/play');
      } else {
        console.error('Registration failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error during registration:', error.message);
    }
  };

  return (
    <div className="container mx-auto mt-8 px-10 py-5">
      <h2 className="text-2xl font-bold mb-4">Register</h2>
      <form onSubmit={handleSubmit} className="max-w-md">
        <div className="mb-4">
          <label htmlFor="username" className="block text-sm font-medium text-gray-700">
            Username
          </label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            className="mt-1 p-2 border border-gray-300 rounded-md w-full"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password" className="block text-sm font-medium text-gray-700">
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            className="mt-1 p-2 border border-gray-300 rounded-md w-full"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="class_" className="block text-sm font-medium text-gray-700">
            Class
          </label>
          <select
            id="class_"
            name="class_"
            value={formData.class_}
            onChange={handleChange}
            className="mt-1 p-2 border border-gray-300 rounded-md w-full"
          >
            <option value="Warrior">Warrior</option>
            <option value="Mage">Mage</option>
            <option value="Archer">Archer</option>
            <option value="Cleric">Cleric</option>
            <option value="Warlock">Warlock</option>
            <option value="Paladin">Paladin</option>
          </select>
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600"
        >
          Register
        </button>
      </form>
      {isLoading && <Loading/>}
    </div>
  );
};

export default Register;
