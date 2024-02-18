import React, { createContext, useContext, useState , useEffect} from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

  const apiUrl = import.meta.env.VITE_APP_API_URL;
  
  const [authenticated, setAuthenticated] = useState(false);

  const login = () => setAuthenticated(true);

  const logout = () => setAuthenticated(false);

  useEffect(() => {
    const checkAuthentication = async () => {
      try {
        const response = await fetch((apiUrl + '/auth/is_logged'), {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          credentials: 'include', 
        });

        if (response.ok) {
          const data = await response.json();
          if (data.message) {
            setAuthenticated(true);
          }
        } else {
          setAuthenticated(false)
          console.error('Failed to check authentication:', response.statusText);
        }
      } catch (error) {
        console.error('Error during authentication check:', error.message);
      }
    };

    checkAuthentication();
  }, []);

  return (
    <AuthContext.Provider value={{ authenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
