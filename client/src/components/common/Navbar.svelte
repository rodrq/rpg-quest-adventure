<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import RpgLogo from '../../assets/favicon.svg'
    import { characterData, clearCharacterData } from '$lib/stores/characterData'; 
    import { Button, Modal } from 'flowbite-svelte';
    import toast from 'svelte-french-toast';
    import { goto } from '$app/navigation';
    import LoadingSpinner from './LoadingSpinner.svelte';
    
    let openLogoutModal = false;
    let isLoading = false;

    const logOutHandler = async () => {
      try {
          isLoading = true;
          const response = await fetch('http://localhost:8000/api/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              },
              credentials: 'include', 
            });
          isLoading=false;
          if (response.ok) {
              toast.success('Logged out');
              clearCharacterData();
              goto('/');
              
          } else {
              console.error('Logout went wrong:', response.statusText);
              toast.error('Logout went wrong');
          }
      } catch (error) {
          isLoading=false;
          console.error('Error during logout:', error);
          toast.error('Error during logout');
      }
  };

</script>

<Navbar let:NavContainer>
  <NavContainer class="border px-5 py-2 rounded-lg bg-white dark:bg-gray-600">
    <NavBrand href="/">
      <img src={RpgLogo} class="me-3 h-6 sm:h-9" alt="RPG Quest Logo" />
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">AI RPG Adventure</span>
    </NavBrand>
    <NavHamburger/>
    {#if $characterData.username}
    <NavUl class='font-bold' >
      <NavLi href="/about">About</NavLi>
      <NavLi href="/play">Play</NavLi>
      <NavLi href="/journey">View journey</NavLi>
      <NavLi href="/ranking">Ranking</NavLi>
      <NavLi href="/restart">Restart</NavLi>
      <NavLi on:click={() => (openLogoutModal = true)}>Log out</NavLi>
    </NavUl>
    {:else}
    <NavUl class='font-bold'>
      <NavLi href="/">Home</NavLi>
      <NavLi href="/about">About</NavLi>
      <NavLi href="/ranking">Ranking</NavLi>
      <NavLi href="/register">Create Character</NavLi>
      <NavLi href="/login">Log in</NavLi>
    </NavUl>
    {/if}
  </NavContainer>

  {#if openLogoutModal === true}
    <Modal title="Terms of Service" bind:open={openLogoutModal} autoclose>
      <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
        Are you sure you want to log out?
      </p>
      
      <svelte:fragment slot="footer">
        <Button on:click={logOutHandler}>Yes</Button>
        <Button color="alternative" on:click={openLogoutModal=false}>Cancel</Button>
      </svelte:fragment>
    </Modal>
  {/if}

  {#if isLoading === true}
    <LoadingSpinner/>
  {/if}

</Navbar>