"""All AI agents to play against the player."""
from game_utils.Encounter import *

class PokemonAgent:
    """An AI to do battle with a Pokemon team"""
    ### NOTE: AN AGENT WILL ALWAYS BE GIVEN A TRAINER OBJECT, EVEN AS A WILD MON ###
    def __init__(self, board):
        """Create an agent with a policy but no information."""
        self.board = board
        self.trainer = None
        self.encounter = None

    def enter_battle(self, trainer: PokemonTrainer, encounter: Battle):
        """Set an agent to take actions as trainer in encounter."""
        self.trainer = trainer
        self.encounter = encounter

    def get_valid_actions(self):
        """Returns all valid actions the agent may take."""
        curr_mon = self.encounter.foe_current_pkmn
        valid_moves = [move for move in curr_mon.moveset if move.pp > 0]
        valid_switches = [mon for mon in self.trainer.team if mon is not curr_mon and not mon.fainted]
        valid_items = [item for item in self.trainer.items if self.trainer.items[item] > 0]

        all_actions = valid_moves
        all_actions.extend(valid_switches)
        all_actions.extend(valid_items)
        return all_actions

    def action(self):
        """Based on AI policy, take a legal action."""
        all_actions = self.get_valid_actions()
        return np.random.choice(all_actions)

    def switch(self):
        """Based on AI policy, make a legal switch."""
        valid_switches = [mon for mon in self.trainer.team if not mon.fainted]
        return np.random.choice(valid_switches)

class RandomLegalAgent(PokemonAgent):
    """The default agent with no methods overriden."""
    def __init__(self, board):
        super().__init__(board)

# TODO: design medium agent (good heuristic, i.e. use supereffective moves, switch when optimal)

# TODO: design hard agent (MINIMAX or EXPECTIMAX with limited depth / rollouts)