import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Register from './components/Register';
import { AuthProvider } from './context/AuthContext';
import Login from './components/Login';
import Play from './components/Play';
import CreatedQuest from './components/CreatedQuest';
import Quests from './components/Quests';
import Quest from './components/Quest';
import About from './components/About';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/play" component={Play} />
          <Route path="/created_quest" component={CreatedQuest} />
          <Route path="/all_quests" component={Quests} />
          <Route path="/quest/:id" component={Quest} />
          <Route path="/about" component={About} />

        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
