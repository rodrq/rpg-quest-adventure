<script>
    import PromptImage from '../../assets/prompt.png'
</script>


<div class="container mx-auto px-10 text-gray-600 text-xl">
    <h1 class="text-2xl font-bold mb-4">
        About the project.
    </h1>
    <p class='my-2'>Given enough context, the Language Model can create amazing stuff. You could tell it all about the lore of the game, the places,
      the animals and monsters of each place, the character coded capabilities and actions; and would end with a real-time generated
      JSON representing a quest that was requested by the videogame NPC you just talked to.</p>
    <p class='my-2'>
      This project just accepts 'class' and 'map' as context to save on infra costs, but still the results are pretty good.
    </p>
    <p>
      Prompt used is:
    </p>
    <img class='my-3'src={PromptImage} alt="prompt">
    <p>Project made with FastAPI, React, and OpenAI API.</p>
    <p>Check the whole project here: <a href='https://github.com/rodrq/rpg-quest' class='underline'target="_blank" rel="noopener noreferrer">https://github.com/rodrq/rpg-quest</a></p>
</div>