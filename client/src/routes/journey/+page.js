export const load = async (loadEvent) => {
    const { fetch } = loadEvent;
    const response = await fetch('http://localhost:8000/api/quest/all', {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    const data = await response.json();
  
    return {
        data
    };
}