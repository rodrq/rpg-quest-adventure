import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import Loading from './Loading';

const Quest = () => {
  const apiUrl = import.meta.env.VITE_APP_API_URL;
  const { id } = useParams();
  const [quest, setQuest] = useState(null);

  useEffect(() => {
    const fetchQuest = async () => {
        try {
    
            const response = await fetch((`${apiUrl}/quest/${id}`), {
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              },
              credentials: 'include', 
            });
        if (response.ok) {
          const questData = await response.json();
          setQuest(questData);
        } else {
          console.error('Failed to fetch quest details:', response.statusText);
        }
      } catch (error) {
        console.error('Error during quest details fetch:', error.message);
      }
    };

    fetchQuest();
  }, [id]);

  if (!quest) {
    return <Loading />;
  }

  return (
    <div className='mx-auto max-w-7xl py-6 sm:px-6 lg:px-8'>
      <div className="container mt-10 bg-gray-200 p-10 rounded-lg">
        <h2 className="text-2xl font-bold mb-4 ">Quest Details</h2>
        <div className="mt-4">
          <p className='text-3xl font-bold  mb-2'>{quest.title}</p>
          <p className='text-lg font-bold mb-4'>{quest.description}</p>
          <p className='text-lg'>Rewards: {quest.rewards.join(', ')}</p>
          <p className='text-lg'>Experience: {quest.experience}</p>
        </div>
        <button className="bg-blue-600 text-white p-2 rounded-md mt-8 hover:bg-blue-600">
          <Link to="/all_quests">Go back</Link>
        </button>
        
      </div>
    </div>
  );
  
};

export default Quest;
