<script>
	  import { goto } from '$app/navigation';
    import classesData from '$lib/data/classes.json';
    import virtuesData from '$lib/data/virtues.json';
    import flawsData from '$lib/data/flaws.json';
    import toast from 'svelte-french-toast';
    import LoadingSpinner from '../../components/common/LoadingSpinner.svelte';
    import { initializeCharacterData } from '$lib/stores/characterData'

    let classes = Object.keys(classesData);
    let flaws = Object.keys(flawsData);
    let virtues = Object.keys(virtuesData);

    let username = '';
    let password = '';
    let selectedClass = '';
    let selectedVirtue = '';
    let selectedFlaw = '';

    let isLoading = false;

    const handleSubmit = async (event) => {
      isLoading = true;
      try {
      const formData ={
        "username": username.toLowerCase(),
        "password": password.toLowerCase(),
        "class_":selectedClass.toLowerCase(),
        "virtue":selectedVirtue.toLowerCase(),
        "flaw":selectedFlaw.toLowerCase(),
      };
      const response = await fetch('http://localhost:8000/api/character/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
        credentials: 'include'
      });

      const responseData = await response.json();

      isLoading = false;

      if (response.ok) {
        isLoading = true;
        initializeCharacterData()
        isLoading= false;
        toast.success('Character created successfully: ', responseData);
        goto("/play")
        
      } else {
        toast.error(responseData.detail);

      }
      } catch (error) {
        toast.error(error.message);
        console.log('Registration failed:', error)
      }
    };

  </script>
  
  <div class="container mx-auto px-10 py-5 text-gray-600 text-xl ">
    <h1 class="text-2xl font-bold mb-4">Character Creation</h1>
    <form class="w-50" on:submit|preventDefault={handleSubmit}>
      <div class="mb-4">
        <label for="username" class="block text-sm font-bold mb-2">Character Name:</label>
        <input type="text" id="username" bind:value={username} class="border p-2 lg:w-[20vw] w-[50vw]" />
      </div>
  
      <div class="mb-4">
        <label for="password" class="block text-sm font-bold mb-2">Password:</label>
        <input type="password" id="password" bind:value={password} class="border p-2 lg:w-[20vw] w-[50vw]" />
      </div>
      <div class="flex flex-col justify-between">
        <div class="mb-4">
            <label for="class" class="block text-sm font-bold mb-2">Class:</label>
            <select id="class" bind:value={selectedClass} class="border p-2 lg:w-[12vw] w-[30vw]">
            {#each classes as className (className)}
                <option value={className}>{className}</option>
            {/each}
            </select>
        </div>

        <div class="mb-4">
            <label for="virtue" class="block text-sm font-bold mb-2">Virtue:</label>
            <select id="virtue" bind:value={selectedVirtue} class="border p-2 lg:w-[12vw] w-[30vw]">
            {#each virtues as virtueName (virtueName)}
                <option value={virtueName}>{virtueName}</option>
            {/each}
            </select>
        </div>

        <div class="mb-4">
            <label for="flaw" class="block text-sm font-bold mb-2">Flaw:</label>
            <select id="flaw" bind:value={selectedFlaw} class="border p-2 lg:w-[12vw] w-[30vw]">
            {#each flaws as flawName (flawName)}
                <option value={flawName}>{flawName}</option>
            {/each}
            </select>
        </div>
        
      </div>
      {#if (isLoading === true)}
      <LoadingSpinner/>
      {/if}
      <button type="submit" class="bg-blue-500 text-white py-2 px-4 mb-10 rounded">Create Character</button>
    </form>
  </div>
  