<script>
    export let data;
    const quests = data.data;
</script>

<head>
    <title>RPG Quest - Journey</title>
</head>

<div class="container mx-auto px-10 text-gray-600 text-xl">
    <h1 class="text-2xl font-bold mb-4">{quests[0].character_username} journey</h1>
    <div>
        {#each quests as quest (quest.quest_id)}
            <a href="/journey" class="hover:text-red-500">
                - {quest.title}
            </a>
        {/each}
    </div>
</div>