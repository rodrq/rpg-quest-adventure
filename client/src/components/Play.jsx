import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useHistory } from 'react-router-dom';


const Play = () => {
    const history = useHistory();
    const { authenticated } = useAuth();
    const [loading, setLoading] = useState(false);
    const [questData, setQuestData] = useState({
      map: '',
      title: '',
      description: '',
      rewards: '',
      experience: '',
    });
  
  
    const handleChange = (e) => {
      setQuestData({ ...questData, [e.target.name]: e.target.value });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      try {
        setLoading(true);
  
  
        const response = await fetch('/quest', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ map: questData.map }),
          credentials: 'include',
        });
        
        if (response.ok) {
          const questResult = await response.json();
          history.push('/created_quest', { questResult })

        } else {
          console.error('Quest request failed:', response.statusText);
        }
      } catch (error) {
        console.error('Error during quest request:', error.message);
      } finally {
        setLoading(false);
      }
    };
  

    return (
        <div className="container mx-auto mt-8 px-10 py-5 text-gray-600 text-xl">
          <h2 className="text-2xl font-bold mb-4">Play</h2>
          {authenticated ? (
            <form onSubmit={handleSubmit} className="max-w-md">
              <div className="mb-4">
                <label htmlFor="map" className="block text-sm font-medium text-gray-700">
                  Map
                </label>
                <select
                  id="map"
                  name="map"
                  value={questData.map}
                  onChange={handleChange}
                  required
                  className="mt-1 p-2 border border-gray-300 rounded-md w-full"
                >
                  <option value="" disabled>Select a map</option>
                  <option value="Forest">Forest</option>
                  <option value="City">City</option>
                  <option value="River">River</option>
                  <option value="Mountain">Mountain</option>
                  <option value="Desert">Desert</option>
                </select>
              </div>
              <button
                type="submit"
                className="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600"
                disabled={loading}
              >
                {loading ? 'Loading...' : 'Start Quest'}
              </button>
            </form>
          ) : (
            <p>Please log in to play.</p>
          )}
        </div>
      );
    };
    
    export default Play;