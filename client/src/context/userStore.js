import { writable } from 'svelte/store';

// Initial state
const userInitialState = {
  loggedIn: false,
  user: null,
  loading: false,
  error: null,
};

// Create a writable store
const user = writable(userInitialState);

export default user;
