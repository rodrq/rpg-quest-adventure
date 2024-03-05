<script>
    export let data;
    const quests = data.data;
</script>
  
<div>
    <h1>Quests</h1>
    <div>
        {#each quests as quest (quest.id)}
            <p>{quest.title}</p>
        {/each}
    </div>
</div>