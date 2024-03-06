<script>

    // TEST DATA
    let rankingData = [
        { ranking: 1, name: 'Roberto', honor: 1000, map: 4, state: 'dead' },
        { ranking: 2, name: 'Jorge', honor: 950, map: 3, state: 'resting' },
        { ranking: 3, name: 'Maria', honor: 900, map: 5, state: 'winner' },
        { ranking: 4, name: 'ElGoat', honor: 850, map: 3, state: 'resting' },
        { ranking: 5, name: 'Milei', honor: 800, map: 4, state: 'dead' },
        { ranking: 6, name: 'Cristina', honor: 750, map: 5, state: 'resting' },
        { ranking: 7, name: 'Maincra', honor: 700, map: 4, state: 'winner' },
        { ranking: 8, name: 'Celes', honor: 650, map: 3, state: 'dead' },
        { ranking: 9, name: 'Rodri', honor: 600, map: 5, state: 'resting' },
        { ranking: 10, name: 'Bass', honor: 550, map: 4, state: 'resting' },
    ];
</script>



<div class="container mx-auto px-10 text-gray-600 text-xl h-screen">
    <div class="text-2xl font-bold mb-4">
        Player Rankings
    </div>
    <h2 class="mb-2">
        * Click on anyone's name to see their journey
    </h2>

    <table class="min-w-full border border-gray-300">
    <thead>
        <tr class="bg-gray-100">
        <th class="py-2 px-4 border-b">Ranking</th>
        <th class="py-2 px-4 border-b">Name</th>
        <th class="py-2 px-4 border-b">Honor</th>
        <th class="py-2 px-4 border-b">Map</th>
        <th class="py-2 px-4 border-b">State</th>
        </tr>
    </thead>
    <tbody>
        {#each rankingData as { ranking, name, honor, map, state }}
        <tr class="{ranking % 2 === 0 ? 'bg-gray-50' : 'bg-white'}">
            <td class="py-2 px-4 border-b text-center">{ranking}</td>
            <td class="py-2 px-4 border-b text-center font-bold">
                <a href="/journey/{name}" class="hover:text-blue-500">
                    {name}
                </a>
            </td>
            <td class="py-2 px-4 border-b text-center">{honor}</td>
            <td class="py-2 px-4 border-b text-center">{map}</td>
            <td class="py-2 px-4 border-b text-center">{state}</td>
        </tr>
        {/each}
    </tbody>
    </table>
</div>