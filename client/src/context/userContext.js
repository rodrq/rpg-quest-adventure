import user from './userStore';

export async function checkUserStatus() {
  user.set({ ...userInitialState, loading: true });

  try {
    // Fetch the /user endpoint
    const response = await fetch('/char_data');
    const userData = await response.json();

    // Update user store with the fetched user data
    user.set({ loggedIn: true, user: userData, loading: false, error: null });
  } catch (error) {
    // Handle errors
    console.error('Error checking user status:', error);
    user.set({ ...userInitialState, error, loading: false });
  }
}
