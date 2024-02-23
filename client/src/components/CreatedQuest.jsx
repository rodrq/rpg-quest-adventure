import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';



const CreatedQuest = ({location}) => {
    const [activeTab, setActiveTab] = useState('parsed'); // 'parsed' or 'json'
    const history = useHistory();

    const questData = location.state?.questResult;

    const FormattedQuestData = () => {
        return <div>
                    <p className='text-3xl font-bold  mb-2'>{questData.quest.title}</p>
                    <p className='text-lg font-bold mb-4'>{questData.quest.description}</p>
                    <p className='text-lg'>Rewards: {questData.quest.rewards.join(', ')}</p>
                    <p className='text-lg'>Experience: {questData.quest.experience}</p>
                </div>;
    };

    const JSONQuestData = () => {
        return <pre style={{ whiteSpace: 'pre-wrap' }}>{JSON.stringify(questData, null, 2)}</pre>;
    };
    if (!questData) {
        return <p>No quest data available.</p>;
    }

    const handlePlayAgain = () => {
        history.replace('/play');
    };

    const handleQuests = () => {
        history.replace('/all_quests');
    };
    return (
        <div className='mx-auto max-w-7xl py-6 sm:px-6 lg:px-8'>
            <div className="flex space-x-4">
                <button
                onClick={() => setActiveTab('parsed')}
                className={`${
                    activeTab === 'parsed'
                    ? 'bg-blue-500 text-white'
                    : 'bg-gray-300 text-gray-700'
                } px-4 py-2 rounded-md focus:outline-none`}
                >
                Formatted Quest Data
                </button>
                <button
                onClick={() => setActiveTab('json')}
                className={`${
                    activeTab === 'json'
                    ? 'bg-blue-500 text-white'
                    : 'bg-gray-300 text-gray-700'
                } px-4 py-2 rounded-md focus:outline-none`}
                >
                Parsed JSON Quest Data
                </button>
            </div>

            <div className="container mt-12 bg-gray-200 p-10 rounded-lg">
                {activeTab === 'parsed' && <FormattedQuestData />}
                {activeTab === 'json' && <JSONQuestData />}
            </div>
            <button onClick={handlePlayAgain} 
                    className="bg-blue-600 text-white p-2 rounded-md mt-8 hover:bg-blue-500">
                    Try Again
            </button>
            <button onClick={handleQuests} 
                    className="bg-blue-500 text-white p-2 rounded-md mt-8 ml-2 hover:bg-blue-600">
                    View quests
            </button>
        </div>
    );
};





export default CreatedQuest;
