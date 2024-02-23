<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import RpgLogo from '../assets/rpg-quest.svg'
    import { onMount } from 'svelte';
    import { checkUserStatus } from '../context/userContext';
    import user from '../context/userStore';

    onMount(() => {
      checkUserStatus();
    });
</script>

<Navbar let:NavContainer>
  <NavContainer class="border px-5 py-2 rounded-lg bg-white dark:bg-gray-600">
    <NavBrand href="/">
      <img src={RpgLogo} class="me-3 h-6 sm:h-9" alt="RPG Quest Logo" />
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">AI RPG Adventure</span>
    </NavBrand>
    <NavHamburger/>
    {#if $user.loggedIn}
    <NavUl class='font-bold' >
      <NavLi href="/about">About</NavLi>
      <NavLi href="/play">Play</NavLi>
      <NavLi href="/journey">View journey</NavLi>
      <NavLi href="/ranking">Ranking</NavLi>
      <NavLi href="/restart">Restart</NavLi>
      <NavLi href="/logout">Log out</NavLi>
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