<script>
	import Footer from '../components/common/Footer.svelte';
	import Navbar from '../components/common/Navbar.svelte';
    import "../app.pcss";
    import { Toaster } from 'svelte-french-toast';
    import { initializeCharacterData, characterData } from '$lib/stores/characterData';
    import { onMount } from 'svelte';
    
    onMount(() => {
            initializeCharacterData();
        }
    );

</script>

<main>
    <Navbar/>
    <Toaster/>
    <slot/>
    <Footer/>
</main>
