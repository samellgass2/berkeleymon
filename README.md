# Berkeleymon
An infinite, pseudorandom Pokemon-style top-down 2D game

# Goals
- **Traversability**: the game world should be interactive and traversable, as in Pokemon games
- **Pokemon Encounter System**: wild Pokemon should be pulled from some encounter table based on area, and trainer pokemon should be appropriate as well
- **Saving and Loading**: the game state should be able to be saved and loaded in a MINIMAL state representation 
- **Procedural Generation**: the game should be able to generate an infinite number of trainers and enemy pokemon, all tuned to be challenging based on the player's level

## Progress
- **5/19/22**:
  - Created system to store locations and parse them for screen-sized presentation
  - Created system to render tiles to screen and completed player animation and representation
  - Set flags and infrastructure for transitioning between areas by repopulating BOARD.location

