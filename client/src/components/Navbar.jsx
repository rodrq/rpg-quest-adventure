import React, { useState } from 'react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import HomeIconSvg from '../assets/rpg-quest.svg';
import { Link, useHistory } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Modal from './Modal';
import Loading from './Loading';

const noAuthNavigation = [
  { name: 'Home', href: '/'},
  { name: 'About', href: '/about'},
  { name: 'Create Character', href: '/register'},
  { name: 'Login', href: '/login'},
]

const authNavigation = [
    { name: 'Home', href: '/'},
    { name: 'About', href: '/about'},
    { name: 'Play', href: '/play'},
    { name: 'Quests', href: '/all_quests'},
  ]
  
const apiUrl = import.meta.env.VITE_APP_API_URL;

export default function Navbar() {
  const { authenticated, logout } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const history = useHistory()

  const [open, setOpen] = useState(false);

  const handleLogout = () => {
    setLogoutModalOpen(true);
  };

  const [isLogoutModalOpen, setLogoutModalOpen] = useState(false);

  const confirmLogout = async () => {
    setOpen(false)
    setIsLoading(true)
    try {
      const response = await fetch(apiUrl + '/auth/logout', {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        credentials: 'include', 
      });
      setIsLoading(false)
      if (response.ok) {
        logout();
        setLogoutModalOpen(false);
        history.push('/');
      } else {
        console.error('Logout failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error during logout:', error.message);
    }
  }

  const cancelLogout = () => {
    setLogoutModalOpen(false);
  };

    
  return (
      <nav className="bg-gray-800">
        <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
          <div className="relative flex h-16 items-center justify-between">
            <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
              {/* Mobile menu button*/}
              <button
                onClick={() => setOpen(!open)}
                className="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
              >
                <span className="absolute -inset-0.5" />
                <span className="sr-only">Open main menu</span>
                {open ? (
                  <XMarkIcon className="block h-6 w-6" aria-hidden="true" />
                ) : (
                  <Bars3Icon className="block h-6 w-6" aria-hidden="true" />
                )}
              </button>
            </div>
            <div className="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
              <Link to='/' className="flex flex-shrink-0 items-center">
                <img
                  className="h-8 w-auto"
                  src={HomeIconSvg}
                  alt="RPG AI quest creator"
                />
              </Link>
              <div className="hidden sm:ml-6 sm:block">
                <div className="flex space-x-4 items-center">
                  {authenticated ? (
                    <>
                      {authNavigation.map((item) => (
                        <div key={item.name}>
                          <Link
                            to={item.href}
                            className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-lg font-bold"
                          >
                            {item.name}
                          </Link>
                        </div>
                      ))}
                      <div>
                        <button
                          onClick={handleLogout}
                          className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-lg font-bold"
                        >
                          Logout
                        </button>
                      </div>
                    </>
                  ) : (
                    noAuthNavigation.map((item) => (
                      <div key={item.name}>
                        <Link
                          to={item.href}
                          className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-lg font-bold"
                        >
                          {item.name}
                        </Link>
                      </div>
                    ))
                  )}
                </div>
              </div>
            </div>
            <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0 text-gray-100"></div>
          </div>
        </div>
        <div className={`sm:hidden ${open ? 'block' : 'hidden'}`}>
          <div className="space-y-1 px-2 pb-3 pt-2">
            {authenticated ? (
              <>
                {authNavigation.map((item) => (
                  <div key={item.name}>
                    <Link
                      onClick={() => setOpen(!open)}
                      to={item.href}
                      className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-xl font-bold"
                    >
                      {item.name}
                    </Link>
                  </div>
                ))}
                <div>
                  <button
                    onClick={handleLogout}
                    className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-xl font-bold"
                  >
                    Logout
                  </button>
                </div>
              </>
            ) : (
              noAuthNavigation.map((item) => (
                <div key={item.name}>
                  <Link
                    onClick={() => setOpen(!open)}
                    to={item.href}
                    className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-xl font-bold"
                  >
                    {item.name}
                  </Link>
                </div>
              ))
            )}
          </div>
        </div>
        <Modal
          isOpen={isLogoutModalOpen}
          onClose={cancelLogout}
          onConfirm={confirmLogout}
          message="Are you sure you want to log out?"
        />
        {isLoading && <Loading/>}
      </nav>
    );
  }