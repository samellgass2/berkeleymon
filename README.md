# Berkeleymon
An infinite, pseudorandom Pokemon-style top-down 2D game

# Goals
- **Traversability**: the game world should be interactive and traversable, as in Pokemon games
- **Pokemon Encounter System**: wild Pokemon should be pulled from some encounter table based on area, and trainer pokemon should be appropriate as well
- **Saving and Loading**: the game state should be able to be saved and loaded in a MINIMAL state representation 
- **Procedural Generation**: the game should be able to generate an infinite number of trainers and enemy pokemon, all tuned to be challenging based on the player's level
  - But pseudorandom and recreatable given a seed.

## Progress
- **5/19/22**:
  - Created system to store locations and parse them for screen-sized presentation
  - Created system to render tiles to screen and completed player animation and representation
  - Set flags and infrastructure for transitioning between areas by repopulating BOARD.location

- **5/20/22**:
  - Added start of pokemon generation, pokemon object, pokemonmove object
  - Added the base of an encounter system with booleans to cede rendering to the current battle 

- **5/21/22**
  - Added sketch of encounter menu and some mouse functionality 
  - Added layering sprites and batching by layer (z-value)

- **5/24/22**
  - Added text boxes that scroll in both overworld and encounter 
  - Added some pokemon sprites and coloring based on pokemons' types 
  - Created constants to be imported to the entire project 
  - Made pokemon move tables generate correctly based on most recently learned at a given level
  - Implemented HP bars

- **5/26/22**
  - Added functionality for damage calculation, fainting, and teams
  - Implemented first AI agent, LegalRandomAgent, to play against a user by choosing a random legal action at all appropriate time steps 
  - Added animation in battle, support for moves that don't do damage
  - Added damage formulas, critical hit rates, type supereffectiveness
  - Added fainting and ending of battle appropriately and with correct text pop ups 
  - Added switching menu and mandatory switch on current 'mon death
  - Started Item infrastructure, allowing AI to use items, and player item management
