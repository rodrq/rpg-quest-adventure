<script>
    import { characterData } from "$lib/stores/characterData";
</script>

<div class='flex flex-col px-10'>
    <h1>Survive the journey and claim victory. Choose between different approaches to achieve your goal, etc.</h1>
    <p>Create a character and play</p>
    <p>Check the best scores</p>
    {#if $characterData.username}
    <p>{$characterData.username}</p>
    {/if}
</div>