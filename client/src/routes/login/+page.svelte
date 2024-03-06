<script>
	import { goto } from '$app/navigation';
    import LoadingSpinner from "../../components/common/LoadingSpinner.svelte";
    import toast from "svelte-french-toast";
    import { initializeCharacterData } from "../../lib/stores/characterData";

    let username;
    let password;
    let isLoading = false;

    const handleSubmit = async (event) => {
      isLoading = true;
      try {
        const formData = new URLSearchParams();

        formData.append('username', username);
        formData.append('password', password);

        const response = await fetch('http://localhost:8000/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData.toString(),
            credentials: 'include'
        });

        const responseData = await response.json();

        isLoading = false;

        if (response.ok) {
            isLoading = true;
            initializeCharacterData()
            isLoading= false;
            toast.success('Logged in succesfuly: ', responseData);
            goto("/play")
            
        } else {
            toast.error(responseData.detail);

        }
        } catch (error) {
            isLoading = false;
            toast.error(error.message);
            console.log('Login failed:', error)
        }
    };

</script>

<head>
  <title>RPG Quest - Login</title>
</head>


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
        
      </div>
      {#if (isLoading === true)}
        <LoadingSpinner/>
      {/if}
      <button type="submit" class="bg-blue-500 text-white py-2 px-4 mb-10 rounded">Log in</button>
    </form>
  </div>