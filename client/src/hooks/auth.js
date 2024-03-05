import { writable } from 'svelte/store';

async function fetchCharacterData() {
    try {
        const response = await fetch('http://localhost:8000/api/character/data', {
            credentials: 'include',
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching character data:', error);
        return null;
    }
}

export const characterData = writable({});

export async function initializeCharacterData() {
    const data = await fetchCharacterData();
    characterData.set(data);
}

export function clearCharacterData() {
    characterData.set({});
}