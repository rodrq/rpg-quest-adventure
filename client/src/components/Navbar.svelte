<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import RpgLogo from '../assets/rpg-quest.svg'
    import { characterData, clearCharacterData } from '../stores/characterData'; 
    import toast from 'svelte-french-toast';
    import { navigate } from 'svelte-navigator';

    const logOutHandler = async () => {
      try {
          const response = await fetch('http://localhost:8000/api/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              },
              credentials: 'include', 
            });

          if (response.ok) {
              toast.success('Logged out');
              clearCharacterData();
              navigate('/')
          } else {
              console.error('Logout went wrong:', response.statusText);
              toast.error('Logout went wrong');
          }
      } catch (error) {
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
      <NavLi on:click={logOutHandler}>Log out</NavLi>
    </NavUl>
    {:else}
    <NavUl class='font-bold'>
      <NavLi href="/about">About</NavLi>
      <NavLi href="/ranking">Ranking</NavLi>
      <NavLi href="/register">Create Character</NavLi>
      <NavLi href="/login">Log in</NavLi>
    </NavUl>
    {/if}
  </NavContainer>
</Navbar>