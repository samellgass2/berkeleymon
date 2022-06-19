"""All AI agents to play against the player."""
from game_utils.Encounter import *
from game_utils.GameBoard import GameBoard
from world.Location import Location

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

    def get_valid_actions(self, curr_mon = None, curr_trainer = None):
        """Returns all valid actions the agent may take."""
        if curr_mon is None:
            curr_mon = self.encounter.foe_current_pkmn
        if curr_trainer is None:
            curr_trainer = self.trainer
        valid_moves = [move for move in curr_mon.moveset if move.pp > 0]
        valid_switches = [mon for mon in curr_trainer.team if mon is not curr_mon and not mon.fainted]
        valid_items = [item for item in curr_trainer.items]

        all_actions = valid_moves
        all_actions.extend(valid_switches)
        all_actions.extend(valid_items)
        return all_actions

    def get_valid_adversary_actions(self, curr_mon = None, trainer = None):
        """Returns all valid actions the player may take"""
        if curr_mon is None:
            curr_mon = self.encounter.user_current_pkmn
        if trainer is None:
            trainer = self.encounter.trainer
        valid_moves = [move for move in curr_mon.moveset if move.pp > 0]
        valid_switches = [mon for mon in trainer.team if mon is not curr_mon and not mon.fainted]
        # ONLY consider battle items
        valid_items = [item for item in trainer.items if item.kind == 0]

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

class NStepRolloutDamageAgent(PokemonAgent):
    def __init__(self, board, n: int, x: int):
        super().__init__(board)
        self.n = n
        self.x = x
        self.adversary_laplacian = 10

    def determine_order(self, user_move: PokemonMove, in_battle, adv_in_battle):
        """Determines who moves first"""
        if in_battle.status == "paralysis" and np.random.random() <= 0.25:
            user_stuck = 1
        elif in_battle.status == "sleep":
            user_stuck = 2
        elif "confusion" in [cond[:-2] for cond in in_battle.secondary_status]:
            if "confusion:0" in in_battle.secondary_status:
                user_stuck = 5
            elif np.random.random() <= 0.5:
                user_stuck = 3
            else:
                user_stuck = 4
        else:
            user_stuck = 0

        if adv_in_battle.status == "paralysis" and np.random.random() <= 0.25:
            foe_stuck = 1
        elif adv_in_battle.status == "sleep":
            foe_stuck = 2
        elif "confusion" in [cond[:-2] for cond in adv_in_battle.secondary_status]:
            if "confusion:0" in adv_in_battle.secondary_status:
                foe_stuck = 5
            elif np.random.random() <= 0.5:
                foe_stuck = 3
            else:
                foe_stuck = 4
        else:
            foe_stuck = 0

        if user_move.priority:
            return 0, user_stuck, foe_stuck
        # TODO: ADD PRIORITY OF AGENT MOVE INTO ROTATION
        if in_battle.status == "paralysis":
            user_speed = in_battle.stats["speed"] // 4
        else:
            user_speed = in_battle.stats["speed"]

        if adv_in_battle.status == "paralysis":
            foe_speed = adv_in_battle.stats["speed"] // 4
        else:
            foe_speed = adv_in_battle.stats["speed"]

        if user_speed == foe_speed:
            order = np.random.choice(range(0,2))
        elif user_speed > foe_speed:
            order = 0
        else:
            order = 1

        return order, user_stuck, foe_stuck

    def action(self):
        """Perform rollouts of len n and return the best expected outcome."""
        simulated_trainer = self.trainer.copy()
        simulated_trainer.set_board(None)
        simulated_adversary = self.encounter.trainer.copy()
        simulated_adversary.set_board(None)
        true_actions = self.get_valid_actions()
        simulated_actions = self.get_valid_actions(curr_mon=simulated_trainer.team[self.trainer.team.index(self.encounter.foe_current_pkmn)],
                                              curr_trainer=simulated_trainer)
        # ***** TODO: make sure that the outputs of true and simulated actions match exactly! *****
        actions_and_values = {}
        for action in simulated_actions:
            actions_and_values[action] = 0

        sim_to_real = {}
        for sim, real in zip(simulated_actions, true_actions):
            sim_to_real[sim] = real

        for simulated_action in actions_and_values:
            print("****** SIMULATING PAYOUT FOR ", simulated_action.name, "******")
            for i in range(self.x):
                print("Episode", i, ":")
                simulated_trainer = self.trainer.copy()
                simulated_trainer.set_board(None)
                simulated_adversary = self.encounter.trainer.copy()
                simulated_adversary.set_board(None)
                in_battle = simulated_trainer.team[self.trainer.team.index(self.encounter.foe_current_pkmn)]
                adv_in_battle = simulated_adversary.team[self.encounter.trainer.team.index(self.encounter.user_current_pkmn)]
                action = simulated_action
                j = 0
                battle_ended = False
                while j < self.n and not battle_ended:
                    print(in_battle.name, adv_in_battle.name)
                    adv_action = self.adversary_action(simulated_adversary, adv_in_battle, simulated_trainer, in_battle)
                    value, simulated_adversary, adv_in_battle, simulated_trainer, in_battle, battle_ended = self.run_turn(
                        simulated_adversary, adv_in_battle, simulated_trainer, in_battle, action, adv_action)
                    print("now:", in_battle.name, adv_in_battle.name)
                    # TODO: GET ALL LEGAL AND FOLLOWING ACTIONS BEFORE LOOPING

                    print("Agent chose:", action.name, "simulating adversary choosing:", adv_action.name, "for payout", value)

                    action = self.weighted_next_action(simulated_adversary, adv_in_battle, simulated_trainer, in_battle)
                    actions_and_values[simulated_action] += value
                    j += 1

            print(simulated_action.name, "RESULTED IN TOTAL VALUE", actions_and_values[simulated_action])
            print(" ")

        print([(action.name, actions_and_values.get(action)) for action in actions_and_values])
        return sim_to_real.get(max(actions_and_values, key=actions_and_values.get))


    def adversary_action(self, adversary_trainer, adv_in_battle, simulated_trainer, in_battle):
        all_adv_actions = self.get_valid_adversary_actions(curr_mon=adv_in_battle, trainer=adversary_trainer)
        raw_weights = [self.evaluate_step(action, adv_in_battle, in_battle)+self.adversary_laplacian for action in all_adv_actions]
        probabilities = [weight / sum(raw_weights) for weight in raw_weights]
        return np.random.choice(all_adv_actions, p=probabilities)

    def weighted_next_action(self, adversary_trainer, adv_in_battle, simulated_trainer, in_battle):
        all_actions = self.get_valid_actions(curr_mon= in_battle, curr_trainer=simulated_trainer)
        raw_weights = [self.evaluate_step(action, in_battle, adv_in_battle)+ self.adversary_laplacian for action in all_actions]
        probabilities = [weight / sum(raw_weights) for weight in raw_weights]
        return np.random.choice(all_actions, p=probabilities)

    def evaluate_step(self, action, user, opponent):
        # Case item
        if isinstance(action, Item):
            if isinstance(action, BattleItem):
                return action.healing
        # Case move
        elif isinstance(action, PokemonMove):
            is_crit, is_super_eff, is_hit, total_damage = action.use(opponent)
            return min(total_damage, opponent.hp)
        # Case switch
        elif isinstance(action, Pokemon):
            # TODO: evaluate strength of switch
            return 0
        return 0

    def run_turn(self, adversary_trainer, adv_in_battle, simulated_trainer, in_battle, action, adv_action):
        agent_moved = False
        adv_moved = False
        battle_ended = False
        value = 0

        if isinstance(adv_action, Pokemon):
            adv_in_battle = adv_action
            print("SWITCHED, NOW", adv_in_battle.name)
            adv_moved = True
        # TODO: do items later
        elif isinstance(adv_action, Item):
            adv_moved = True
            value -= adv_action.healing

        if isinstance(action, Pokemon):
            in_battle = action
            agent_moved = True
        # TODO: do items later
        elif isinstance(action, Item):
            agent_moved = True
            value += action.healing

        order = -1

        if not agent_moved and adv_moved:
            order = 1
        elif not adv_moved and agent_moved:
            order = 0

        if not agent_moved and not adv_moved or order != -1:
            if order == -1:
                order, adv_stuck, agent_stuck = self.determine_order(adv_action, in_battle, adv_in_battle)
            else:
                adv_stuck, agent_stuck = 0, 0

            # Case agent gets to move
            if order == 1:
                is_crit, is_super_eff, is_hit, total_damage = action.use(adv_in_battle)
                adv_in_battle.hp -= total_damage
                value += min(total_damage, adv_in_battle.hp)
                # Case opponent may move
                if adv_in_battle.hp > 0 and not adv_moved and adv_stuck not in [1,2,3]:
                    is_crit, is_super_eff, is_hit, total_damage = adv_action.use(in_battle)
                    in_battle.hp -= total_damage
                    value -= total_damage
                # Case opponent may move but is dead
                elif adv_in_battle.hp <= 0:
                    adv_in_battle.fainted = True
                    remaining = [mon for mon in adversary_trainer.team if not mon.fainted]
                    if len(remaining) == 0:
                        battle_ended = True
                    else:
                        adv_in_battle = remaining[0]
                # Else, opponent may not move

            # Case adversary gets to move first
            else:
                is_crit, is_super_eff, is_hit, total_damage = adv_action.use(in_battle)
                in_battle.hp -= total_damage
                value -= min(total_damage, in_battle.hp)
                # Case agent may move
                if in_battle.hp > 0 and not agent_moved and agent_stuck not in [1,2,3]:
                    is_crit, is_super_eff, is_hit, total_damage = action.use(adv_in_battle)
                    adv_in_battle.hp -= total_damage
                    value += total_damage
                # Case agent may move but is dead
                elif in_battle.hp <= 0:
                    in_battle.fainted = True
                    remaining = [mon for mon in simulated_trainer.team if not mon.fainted]
                    if len(remaining) == 0:
                        battle_ended = True
                    else:
                        in_battle = remaining[0]
                # Else agent chose switch / item

        return value, adversary_trainer, adv_in_battle, simulated_trainer, in_battle, battle_ended



# TODO: design hard agent (MINIMAX or EXPECTIMAX with limited depth / rollouts)