import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Loading from './Loading';

const Quests = () => {

  const [quests, setQuests] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true)
    const fetchQuests = async () => {
      try {

        const response = await fetch('/quest/all', {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          credentials: 'include', 
        });
        setIsLoading(false);
        if (response.ok) {
          const questsData = await response.json();
          setQuests(questsData);
        } else {
          console.error('Failed to fetch quests:', response.statusText);
        }
      } catch (error) {
        console.error('Error during quest fetch:', error.message);
      } finally {

      }
    };

    fetchQuests();
  }, []);

  if (isLoading) {
    return <Loading/>
  }

  return (
    <div className="container mx-auto mt-8 px-10 py-5 text-gray-600 text-xl">
      <h2 className="text-2xl font-bold mb-4">All Quests</h2>
      {quests && quests.length > 0 ? (
        quests.map((quest) => (
          <div key={quest.quest_id} className="mb-4">
            <Link to={`/quest/${quest.quest_id}`}>
              <p className="text-lg font-bold">{quest.title}</p>
            </Link>
          </div>
        ))
      ) : (
        <div>
          <p>No quests available.</p>
          <Link to='/play'>Click here to create one</Link>
        </div>
      )}
    </div>
  );
};

export default Quests;
