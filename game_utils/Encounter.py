"""Battle Interface, dispatched by GameBoard."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
from data.Constants import *
from game_utils.Cutscene import *
import math

class PokemonMove:
    def __init__(self, type: int, name: str, power: int, physical: bool, accuracy: int, pp: int, priority: bool=False, is_status=False):
        """Initialize a pokemon move archetype."""
        self.user = None
        self.type = type
        self.name = name
        self.power = power
        self.priority = priority
        self.physical = physical
        self.accuracy = accuracy
        self.max_pp = pp
        self.pp = pp
        self.is_status = is_status

    def use(self, opponent):
        """Dispatches the given move on opponent from user - returns is_crit (bool) and is_super_eff in {-2, -1, 0, 1}."""
        # TODO: implement "stages" of crits after focus energy, etc.
        crit_multiplier = 1 + 0.5 * int(np.random.random() < (1/16))
        if crit_multiplier > 1:
            is_crit = True
        else:
            is_crit = False

        super_eff_multiplier = math.prod([EFFECTIVENESS(self.type, other) for other in opponent.types])
        if super_eff_multiplier == 0:
            is_super_eff = -2
        elif super_eff_multiplier < 1:
            is_super_eff = -1
        elif super_eff_multiplier == 1:
            is_super_eff = 0
        else:
            is_super_eff = 1

        STAB_multiplier = 1 + 0.5 * int(self.type in self.user.types)

        rand_multiplier = np.random.choice(range(85, 101)) / 100

        if self.physical:
            attack_defense_ratio = self.user.stats["attack"] / opponent.stats["defense"]
        else:
            attack_defense_ratio = self.user.stats["special_attack"] / opponent.stats["special_defense"]

        # TODO: implement other multipliers: weather, burn, specific 'other' cases

        damage = (((2 * self.user.level / 5 + 2) * self.power * attack_defense_ratio / 50) + 2) * \
                 crit_multiplier * rand_multiplier * STAB_multiplier * super_eff_multiplier

        hit_prob = np.random.choice(range(0, 101))
        if hit_prob <= self.accuracy:
            is_hit = True
            total_damage = min(damage, opponent.hp)
        else:
            is_hit = False
            total_damage = 0

        self.pp -= 1
        # TODO: return if crit or not to print to screen and is not very / super effective, and missed or not
        return is_crit, is_super_eff, is_hit, total_damage

    def set_user(self, pkmn):
        """Sets user for use to know typing and speed."""
        self.user = pkmn


    # TODO: implement as object that can be dispatched accurately in battle

class Pokemon:
    """The general, archetypal Pokemon class to create most of the skeleton for actions."""
    def __init__(self, name: str, nickname: str, types: [int], level: int, xp: float, movetable: {int, PokemonMove}, moveset: [PokemonMove],
                 defense: int, attack: int, special_defense: int, special_attack: int, hp: int, speed: int, gender: int,
                 front_sprite: pg.sprite.Sprite, back_sprite: pg.sprite.Sprite, exp_yield: int, evolutions: {int, any}):

        # To allow for generation of a mon by either total xp OR level, the other is filled in if not provided.
        if level is None:
            self.xp = xp
            self.level = self.xp_to_level()
        if xp is None:
            self.level = level
            self.xp = self.level_to_xp()
        if gender is None:
            gender = np.random.choice(range(2))

        self.movetable = movetable
        self.moveset = moveset
        if moveset is None:
            self.moveset = []
            self.get_most_recent_moves()

        for move in self.moveset:
            move.set_user(self)

        self.name = name
        if nickname:
            self.display_name = nickname
        else:
            self.display_name = name

        self.types = types
        self.gender = gender
        self.exp_yield = exp_yield
        self.tier = 'NA'
        self.number = -1


        self.base_stats = {}
        self.base_stats["defense"] = defense
        self.base_stats["attack"] = attack
        self.base_stats["special_defense"] = special_defense
        self.base_stats["special_attack"] = special_attack
        self.base_stats["max_hp"] = hp
        self.base_stats["speed"] = speed

        self.front_sprite = front_sprite
        self.back_sprite = back_sprite

        self.stats = {}
        self.calculate_stats()
        self.hp = self.stats["max_hp"]

        self.status = -1
        self.fainted = False
        self.seen = []
        self.move_queue = []

    def get_most_recent_moves(self):
        """Retrieves the up to 4 most recent moves a Pokemon would have learned."""
        level = self.level
        while level > 0 and len(self.moveset) < 4:
            if self.movetable.get(level) is not None:
                self.moveset.append(self.movetable.get(level)())
                # TODO: set user for all moves to self
            level -= 1

    def calculate_stats(self):
        """Update in place a pokemon's functional stats at a given level."""
        self.stats["max_hp"] = math.floor(0.01 * (2 * self.base_stats["max_hp"] * self.level)) + self.level + 10

        for stat in self.base_stats:
            self.stats[stat] = math.floor(0.01 * (2 * self.base_stats[stat]) * self.level) + 5

    def take_damage(self, damage: int):
        """Logic to take damage and note if the user is fainted."""
        if damage < self.hp:
            self.hp -= damage
        else:
            self.hp = 0
            self.fainted = True

    def level_up(self):
        """Called on level, automatically updates stats."""
        self.level += 1
        self.calculate_stats()
        # TODO: check if new_move exists and send text out if so

    def new_move(self, move: PokemonMove):
        """Begins the dialogue for learning a new move."""
        if len(self.moveset) < 4:
            self.moveset.append(move)
        else:
            self.move_queue.append(move)

    ##### TODO: NOTE ONLY THE FAST EXPERIENCE FAMILY IS IMPLEMENTED #####
    def xp_to_level(self, xp: int=None):
        """Calculates the level of a pokemon with some total XP."""
        if xp is None:
            return math.floor((5 * self.xp / 4) ** (1/3))
        else:
            return math.floor((5 * xp / 4) ** (1 / 3))


    def level_to_xp(self, level: int=None):
        """Calculates the total XP a pokemon has earned to reach exactly their current level"""
        if level is None:
            return math.floor(4 * (self.level ** 3) / 5)
        else:
            return math.floor(4 * (level ** 3) / 5)

    def gain_xp(self, xp: int) -> bool:
        """Gain xp, update appropriate params."""
        leveled = False
        if self.level == 100:
            return leveled
        self.xp += xp
        new_level = self.xp_to_level(self.xp)
        while new_level > self.level:
            self.level_up()
            leveled = True
            if self.movetable.get(self.level) is not None:
                self.new_move(self.movetable.get(self.level)())

        return leveled

    def replace_move(self, old_move: str):
        """Replaces the given move with the most recent new move learned"""
        new_move = self.move_queue.pop()
        i = 0
        while i < len(self.moveset):
            if self.moveset[i].name == old_move:
                self.moveset[i] = new_move
            i += 1

class PokemonGenerator:
    def __init__(self, pkmn_and_odds: list, min_level: int, max_level: int):
        self.encounter_table = pkmn_and_odds
        self.min_level = min_level
        self.max_level = max_level

    def encounter(self):
        """Generate a wild pokemon to pass out to Location --> tile --> Board to fight."""
        pokemon = self.choose_wild_pkmn()
        # Then, from this, choose an appropriate level based on distribution
        level = np.random.choice(np.arange(self.min_level, self.max_level+1))
        # Then, generate the pokemon's correct stats by keeping a big lookup table
        # TODO: randomly assign a gender and nature when nature is done
        return pokemon(level = level)



    def choose_wild_pkmn(self):
        """Randomly generate a pokemon to encounter based on encounter rates."""
        roll = np.random.random() - self.encounter_table[0][1]
        i = 0
        while roll > 0:
            roll -= self.encounter_table[i+1][1]
            i += 1
        return self.encounter_table[i][0]

class Item:
    """A usable in-game item."""
    def __init__(self, kind: int, value: int, owner, name):
        self.kind = kind
        self.owner = owner
        self.name = name

    def use(self, target: Pokemon):
        return

    def sell(self):
        self.owner.items.remove(self)



# TODO: implement all items in subclasses of Item
class KeyItem(Item):
    def __init__(self, owner, name):
        """A key item is type 0, has no value, and an owner."""
        super().__init__(0, 0, owner, name)

    def sell(self):
        """A key item may not be sold"""
        return

class PokeballItem(Item):
    def __init__(self, value, owner, name):
        super().__init__(1, value, owner, name)

    def use(self, target: Pokemon):
        # Do self.owner.battle.catch() --> attempt catch
        return


# TODO: implement the TRAINER class, make it agnostic for use by an AGENT or by a PLAYER
class PokemonTrainer:
    """A container to keep track of a trainer's pokemon and items."""
    def __init__(self, pokemon: [Pokemon], items: {Item, int}, money: int):
        self.team = pokemon
        self.items = items
        self.money = money

    def use_item(self, item: Item):
        """Use a given item from inventory. *NOT SAFE*"""
        self.items[item].use()
        if self.items[item] == 0:
            self.items.pop(item)


# TODO: implement the BATTLE class, figure out how to flag in main render loop --> do encounter UI
class Battle:
    """The renderer and logic for pokemon battles"""
    def __init__(self, trainer: PokemonTrainer, opponent, board, wild):
        self.trainer = trainer
        self.player_may_take_action = False
        self.layers = 6
        self.batches = [graphics.Batch() for i in range(self.layers)]
        self.board = board

        # The active pokemon should be the first non-fainted mon
        self.user_current_pkmn = None
        i = 0
        while i < len(trainer.team) and self.user_current_pkmn is None:
            if not trainer.team[i].fainted:
                self.user_current_pkmn = trainer.team[i]
            else:
                i+=1

        self.is_wild = wild

        ##### GRAPHICS PARAMS #####
        self.battle_button_bottom_left = (9*TILE_WIDTH, 2*TILE_HEIGHT)
        self.battle_button_top_right = (15*TILE_WIDTH, 5*TILE_WIDTH)

        self.run_button_bottom_left = (9.5 * TILE_WIDTH, 0.5 * TILE_HEIGHT)
        self.run_button_top_right = (14.5 * TILE_WIDTH, 1.5 * TILE_WIDTH)

        self.items_button_bottom_left = (2 * TILE_WIDTH, 2 * TILE_HEIGHT)
        self.items_button_top_right = (7 * TILE_WIDTH, 4 * TILE_HEIGHT)

        self.pokemon_button_bottom_left = (17 * TILE_WIDTH, 2 * TILE_HEIGHT)
        self.pokemon_button_top_right = (22 * TILE_WIDTH, 4 * TILE_HEIGHT)

        self.move_box_width = 8 * TILE_WIDTH
        self.move_box_height = 2.5 * TILE_HEIGHT

        self.switch_box_width = 5 * TILE_WIDTH
        self.switch_box_height = 2.5 * TILE_HEIGHT

        self.shapes = []
        ##### END GRAPHICS PARAMS #####

        ##### BATTLE VARS #####
        self.curr_menu = 0
        # 0 for player, 1 for agent
        self.curr_turn = None
        self.curr_user_move = None
        self.curr_agent_move = None
        self.is_hit = None
        self.is_crit = None
        self.effectiveness = None
        self.curr_total_damage = None
        self.curr_damage = None
        self.turn_counter = 0
        self.battle_ended_bool = False
        self.shown_effectiveness = False
        self.switch_forced = False
        self.user_switched_bool = False
        self.mid_switch = False
        self.recently_deceased = None
        self.mon_learning_new_move = None
        ##### END BATTLE VARS #####


        ##### INIT AGENT #####
        # If wild, 'opponent' is a list of 1 mon
        if self.is_wild:
            self.agent = self.board.wild_agent
            ai_trainer = PokemonTrainer(opponent, items={}, money=0)

        # If trainer, 'opponent' is a set PokemonTrainer object
        else:
            self.agent = self.board.trainer_agent
            ai_trainer = opponent

        self.opponent = ai_trainer
        self.foe_current_pkmn = self.opponent.team[0]

        # Set the appropriate AI agent up
        self.agent.enter_battle(self.opponent, self)
        ##### END INIT AGENT #####

        self.user_current_pkmn.seen.append(self.foe_current_pkmn)

        self.initialize()

    def intro_animation(self):
        """Should start an intro animation that is unskippable and begins the battle."""
        # TODO: make the animation
        intro_text = TextBox("A wild "+str(self.foe_current_pkmn.display_name)+" appeared!", overworld=False)
        self.board.display_text(intro_text)
        return

    def outro_animation(self):
        """Should execute an outro animation that is unskippable and ends the battle."""
        # TODO: make the animation
        return

    def initialize(self):
        """Sets up all objects and important pointers as attributes of the Battle."""
        self.render()

        # animate stuff
        self.intro_animation()

        # Allow player to move
        self.player_may_take_action = True
        return

    def render(self):
        """Main battle update look called at every frame."""
        # TODO: optimize to ONLY make new objects when necessary (something changes)
        self.shapes = []
        self.batches = [graphics.Batch() for i in range(self.layers)]
        background = pg.shapes.Rectangle(0,0, width=24*TILE_WIDTH, height=16*TILE_HEIGHT, color=(255,255,255), batch=self.batches[0])
        menu = pg.shapes.Rectangle(0,0, width=24*TILE_WIDTH, height=6*TILE_HEIGHT, color=(255,255,255), batch=self.batches[2])
        menu_divider = pg.shapes.Line(x=0, y=6*TILE_HEIGHT, x2=24*TILE_WIDTH, y2=6*TILE_HEIGHT, width=4, color=(0,0,0), batch=self.batches[2])

        self.render_pkmn_plates()
        self.render_hp_bars()
        self.render_sprites()

        self.battle_update_logic()

        if self.curr_menu == 0:
            self.render_buttons()

        elif self.curr_menu == 1:
            self.render_items_menu()

        elif self.curr_menu == 2:
            self.render_battle_menu()

        elif self.curr_menu == 3:
            self.render_pokemon_menu()

        for batch in self.batches:
            batch.draw()

    def battle_update_logic(self):
        """Contains the hierarchical logical structure of the within a turn in battle."""
        # If a move is being learned or another interactive dialogue is open, handle that before all else
        if self.board.last_choice is not None:
            self.handle_interactive_dialogue()
            return

        # Edge case multiple new moves at once
        if self.user_current_pkmn is not None and self.user_current_pkmn.move_queue:
            self.new_move_dialogue(self.user_current_pkmn)

        # If skippable text is being displayed, update NONE of the battle params
        if self.board.text_timer > 0:
            self.player_may_take_action = False

        else:
            # If a switch is underway, allow it to continue:
            if self.mid_switch:
                if self.user_current_pkmn is None:
                    self.user_switched(-1)
                else:
                    self.opponent_switched(-1)

            # Case battle ended
            if self.battle_ended_bool and self.board.current_text is None:
                self.battle_ended()

            # Case move animation
            if not self.battle_ended_bool and self.curr_turn is not None:
                self.animate_turn()

            # Case user switched, turn has ended
            if self.user_switched_bool and not self.switch_forced:
                self.user_switched_bool = False
                self.curr_turn = 0
                self.turn_counter = 0
                self.shown_effectiveness = True
                self.switch_turn()

        # If the turn has come to an end, force the text to end and let the player move
        if self.curr_turn is None:
            # if not self.user_switched_bool:
            #     self.board.end_text()
            self.player_may_take_action = True
        else:
            self.player_may_take_action = False

    def award_xp(self):
        """Dispatch xp gains to all """
        participants = sum([1 for mon in self.trainer.team if not mon.fainted and self.recently_deceased in mon.seen])

        for mon in self.trainer.team:
            old_level = mon.level
            if not mon.fainted and self.recently_deceased in mon.seen:
                mon.seen.remove(self.recently_deceased)
                xp = self.calculate_xp(self.recently_deceased, participants)
                leveled_up = mon.gain_xp(xp)
                got_xp = True
            elif self.recently_deceased in mon.seen:
                mon.seen.remove(self.recently_deceased)
                got_xp = False
                leveled_up = False
            else:
                leveled_up = False
                got_xp = False

            if got_xp:
                message = mon.name+" gained "+str(xp)+" xp"
                self.board.display_text(TextBox(message, overworld=False, unskippable=False))

            if leveled_up:
                for new_level in range(old_level+1, mon.level+1):
                    message = mon.name+" grew to level "+str(new_level)+"!"
                    self.board.display_text(TextBox(message, overworld=False, unskippable=False))

            if mon.move_queue:
                self.new_move_dialogue(mon)

    def handle_interactive_dialogue(self):
        # Case ready to forget a move
        if self.board.last_choice == "Forget an old move":
            options = [move.name for move in self.mon_learning_new_move.moveset]
            options.append("GIVE UP?")
            self.board.display_text(DialogueBox("Which move should be forgotten?", options, overworld=False), skip_queue=True)
            self.board.last_choice = None

        # Case not forgetting a move
        elif self.mon_learning_new_move is not None and ("Give up on learning" in self.board.last_choice or "GIVE UP?" in self.board.last_choice):
            message = self.mon_learning_new_move.name+" gave up on learning "+self.mon_learning_new_move.move_queue[-1].name+"."
            self.board.display_text(TextBox(message, overworld=False, unskippable=False), skip_queue=True)
            self.mon_learning_new_move = None
            self.board.last_choice = None

        # Case a move has been chosen
        elif self.mon_learning_new_move is not None and self.board.last_choice in [move.name for move in self.mon_learning_new_move.moveset]:
            forgotten = self.board.last_choice
            message = self.mon_learning_new_move.name + " forgot how to use " + forgotten + " and learned " +self.mon_learning_new_move.move_queue[-1].name+" instead!"
            self.mon_learning_new_move.replace_move(forgotten)
            self.board.display_text(TextBox(message, overworld=False, unskippable=False), skip_queue=True)
            self.board.last_choice = None

    def new_move_dialogue(self, mon: Pokemon):
        """Trigger dialogue for learning a new move"""
        new_move = mon.move_queue[-1]
        self.mon_learning_new_move = mon
        message = mon.name+" wants to learn "+new_move.name+", but it already knows 4 moves. Should it forget another to learn "+new_move.name+"?"
        self.board.display_text(DialogueBox(message, options=["Forget an old move", "Give up on learning "+new_move.name], overworld=False))
        self.board.last_choice = None

    def calculate_xp(self, foe_mon: Pokemon, participants: int):
        a = 1 + 0.5 * int(self.is_wild)
        b = foe_mon.exp_yield
        e = 1 # TODO: + 0.5 * int(user_mon.item.name == "Lucky Egg")
        f = 1 # TODO: + 0.2 * int(user_mon.affection >= x)
        L = foe_mon.level

        return math.floor(a * b * e * L * f / (7 * participants))

    def render_pkmn_plates(self):
        """Renders plates beneath Pokemon."""
        # TODO: fill the plates
        plate = pg.shapes.Ellipse(x=16.5*TILE_WIDTH, y=12*TILE_HEIGHT,
                                  a=4*TILE_WIDTH, b=1.5*TILE_HEIGHT, color=(0,0,0), batch=self.batches[1])

        friendly_plate = pg.shapes.Ellipse(x=6*TILE_WIDTH, y=5*TILE_HEIGHT,
                                           a=6.5*TILE_WIDTH, b=3*TILE_HEIGHT, color=(0,0,0), batch=self.batches[1])
        self.shapes.extend([plate, friendly_plate])

    def render_hp_bars(self):
        """Renders the HP bars correctly with respect to current health."""
        if self.user_current_pkmn is not None:

            health_bar1 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=7.5*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            health_bar2 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=8*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            health_bar3 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=16.5*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            health_bar4 = pg.shapes.Line(x=23*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            pkmn_name = pg.text.Label(text=self.user_current_pkmn.display_name, font_size=10, x=16.5*TILE_WIDTH, y=8.3*TILE_HEIGHT,
                                      color=(0,0,0,255), batch=self.batches[2])

            friendly_mon_percent = self.user_current_pkmn.hp / self.user_current_pkmn.stats["max_hp"]
            healthbarfill = pg.shapes.Rectangle(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, height=0.5*TILE_HEIGHT, width=6.5*TILE_WIDTH*friendly_mon_percent,
                                                color=(0, 255, 0), batch=self.batches[3])

            friendly_level = pg.text.Label(text="Lv. "+str(self.user_current_pkmn.level), font_size=10, x=21.5*TILE_WIDTH, y=8.3*TILE_HEIGHT,
                                      color=(0,0,0,255), batch=self.batches[2])

            health_counter = pg.text.Label(text=str(math.ceil(self.user_current_pkmn.hp)) + " / "+str(self.user_current_pkmn.stats["max_hp"]), font_size=10, x=19*TILE_WIDTH, y=7.08*TILE_HEIGHT,
                                      color=(0,0,0,255), batch=self.batches[2])

            main_bar = pg.shapes.Rectangle(x=16*TILE_WIDTH, y=7 * TILE_HEIGHT, width=8 * TILE_WIDTH, height=2 * TILE_HEIGHT,
                                           batch=self.batches[1], color=(200,200,200))
            f_triangle = pg.shapes.Triangle(x=16 * TILE_WIDTH, y=7 * TILE_HEIGHT, x2=16 * TILE_WIDTH, y2=9 * TILE_HEIGHT,
                                            x3=15 * TILE_WIDTH, y3=9 * TILE_HEIGHT,
                                            batch=self.batches[1], color=(200,200,200))

            ### XP BAR ###
            xp_floor = self.user_current_pkmn.level_to_xp(self.user_current_pkmn.level)
            xp_to_next_lvl = self.user_current_pkmn.level_to_xp(self.user_current_pkmn.level + 1)
            percent_to_next_lvl = (self.user_current_pkmn.xp - xp_floor) / (xp_to_next_lvl - xp_floor)
            xp_bar = pg.shapes.Rectangle(x=16.5*TILE_WIDTH, y=7*TILE_HEIGHT, height=0.1*TILE_HEIGHT, width=6.5*TILE_WIDTH*percent_to_next_lvl,
                                                color=(50, 175, 244), batch=self.batches[1])

            self.shapes.extend([main_bar, f_triangle,
                            health_bar1, health_bar2, health_bar3, health_bar4,
                            pkmn_name, healthbarfill, health_counter, friendly_level, xp_bar])

        if self.foe_current_pkmn is not None:
            enemy_health_bar1 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=13.5*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            enemy_health_bar2 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=14*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            enemy_health_bar3 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=0.5*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            enemy_health_bar4 = pg.shapes.Line(x=7*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                         color=(0,0,0), batch=self.batches[2])
            enemy_pkmn_name = pg.text.Label(text=self.foe_current_pkmn.display_name, font_size=10, x=0.5*TILE_WIDTH, y=14.3*TILE_HEIGHT,
                                      color=(0,0,0,255), batch=self.batches[2])

            enemy_mon_percent = self.foe_current_pkmn.hp / self.foe_current_pkmn.stats["max_hp"]
            enemy_healthbarfill = pg.shapes.Rectangle(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, height=0.5*TILE_HEIGHT, width=6.5*TILE_WIDTH*enemy_mon_percent,
                                                color=(0, 255, 0), batch=self.batches[3])

            enemy_level = pg.text.Label(text="Lv. " + str(self.foe_current_pkmn.level), font_size=10, x=6 * TILE_WIDTH,
                                           y=14.3 * TILE_HEIGHT,
                                           color=(0, 0, 0, 255), batch=self.batches[2])

            enemy_bar = pg.shapes.Rectangle(x=0, y=13*TILE_HEIGHT, width=7*TILE_WIDTH, height=2*TILE_HEIGHT,
                                           batch=self.batches[1], color=(200,200,200))
            enemy_triangle = pg.shapes.Triangle(x=7*TILE_WIDTH, y=13*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=15*TILE_HEIGHT, x3=8*TILE_WIDTH, y3=15*TILE_HEIGHT,
                                            batch=self.batches[1], color=(200,200,200))




            self.shapes.extend([enemy_health_bar1, enemy_health_bar2, enemy_bar, enemy_triangle,
                                enemy_health_bar3, enemy_health_bar4, enemy_pkmn_name, enemy_healthbarfill,
                                 enemy_level])

    def render_sprites(self):
        """Draws the front of the opponent and the back of the user."""
        friendly_mon = self.user_current_pkmn
        if friendly_mon is not None:
            friendly_mon.back_sprite.batch = self.batches[2]
            friendly_mon.back_sprite.x = 4*TILE_WIDTH
            friendly_mon.back_sprite.y = 6*TILE_HEIGHT

        foe_mon = self.foe_current_pkmn
        if foe_mon is not None:
            foe_mon.front_sprite.batch = self.batches[2]
            foe_mon.front_sprite.x = 15*TILE_WIDTH
            foe_mon.front_sprite.y = 11*TILE_HEIGHT

    def render_buttons(self):
        """Main menu button renderer."""
        battle_button = pg.shapes.BorderedRectangle(x= self.battle_button_bottom_left[0], y=self.battle_button_bottom_left[1],
                                     width=self.battle_button_top_right[0] - self.battle_button_bottom_left[0],
                                     height=self.battle_button_top_right[1] - self.battle_button_bottom_left[1],
                                     color=(243, 103, 89), border_color=(173, 24, 10), batch = self.batches[3], border=3)

        battle_button_label = pg.text.Label(text="BATTLE", font_size=24, x= self.battle_button_bottom_left[0] + 1 * TILE_WIDTH,
                                       y= self.battle_button_bottom_left[1] + 1 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        run_button = pg.shapes.BorderedRectangle(x= self.run_button_bottom_left[0], y=self.run_button_bottom_left[1],
                                     width=self.run_button_top_right[0] - self.run_button_bottom_left[0],
                                     height=self.run_button_top_right[1] - self.run_button_bottom_left[1],
                                     color=(128, 237, 68), border_color=(64, 161, 10), batch = self.batches[3], border=3)

        run_button_label = pg.text.Label(text="RUN", font_size=18, x= self.run_button_bottom_left[0] + 1.33 * TILE_WIDTH,
                                       y= self.run_button_bottom_left[1] + 0.25 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        items_button = pg.shapes.BorderedRectangle(x= self.items_button_bottom_left[0], y=self.items_button_bottom_left[1],
                                     width=self.items_button_top_right[0] - self.items_button_bottom_left[0],
                                     height=self.items_button_top_right[1] - self.items_button_bottom_left[1],
                                     color=(50, 175, 244), border_color=(16, 80, 200), batch = self.batches[3], border=3)

        items_button_label = pg.text.Label(text="ITEMS", font_size=20, x= self.items_button_bottom_left[0] + 1 * TILE_WIDTH,
                                       y= self.items_button_bottom_left[1] + 0.5 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        pokemon_button = pg.shapes.BorderedRectangle(x= self.pokemon_button_bottom_left[0], y=self.pokemon_button_bottom_left[1],
                                     width=self.pokemon_button_top_right[0] - self.pokemon_button_bottom_left[0],
                                     height=self.pokemon_button_top_right[1] - self.pokemon_button_bottom_left[1],
                                     color=(50, 175, 244), border_color=(16, 80, 200), batch = self.batches[3], border=3)

        pokemon_button_label = pg.text.Label(text="POKEMON", font_size=20, x= self.pokemon_button_bottom_left[0] + 0.25 * TILE_WIDTH,
                                       y= self.pokemon_button_bottom_left[1] + 0.5 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        self.shapes.extend([battle_button, battle_button_label,
                            run_button, run_button_label,
                            items_button, items_button_label,
                            pokemon_button, pokemon_button_label])

    def dispatch_mouse_click(self, x, y):
        """Process mouse click based on current menus."""
        # Case in main menu
        if self.curr_menu == 0:
            # Case clicked ITEMS
            if self.items_button_bottom_left[0] <= x <= self.items_button_top_right[0] \
                    and self.items_button_bottom_left[1] <= y <= self.items_button_top_right[1]:
                print("ITEMS CLICKED")
                self.curr_menu = 1
            # Case clicked RUN
            elif self.run_button_bottom_left[0] <= x <= self.run_button_top_right[0] \
                    and self.run_button_bottom_left[1] <= y <= self.run_button_top_right[1]:
                print("RUN CLICKED")
                self.run_action()
            # Case clicked BATTLE
            elif self.battle_button_bottom_left[0] <= x <= self.battle_button_top_right[0] \
                    and self.battle_button_bottom_left[1] <= y <= self.battle_button_top_right[1]:
                print("BATTLE CLICKED")
                self.curr_menu = 2
            # Case clicked POKEMON
            elif self.pokemon_button_bottom_left[0] <= x <= self.pokemon_button_top_right[0] \
                    and self.pokemon_button_bottom_left[1] <= y <= self.pokemon_button_top_right[1]:
                print("POKEMON CLICKED")
                self.curr_menu = 3
        # Case in items menu
        elif self.curr_menu == 1:
            return
        # Case in battle menu
        elif self.curr_menu == 2:
            # Case move one exists and is clicked
            if 1 * TILE_WIDTH <= x <= 1 * TILE_WIDTH + self.move_box_width \
                and 3.25 * TILE_HEIGHT <= y <= 3.25 * TILE_HEIGHT + self.move_box_height \
                and len(self.user_current_pkmn.moveset)>=1:

                    move = self.user_current_pkmn.moveset[0]
                    print(move.name)
                    self.battle_action(move)
            # Case move two exists and is clicked
            elif 10 * TILE_WIDTH <= x <= 10 * TILE_WIDTH + self.move_box_width \
                and 3.25 * TILE_HEIGHT <= y <= 3.25 * TILE_HEIGHT + self.move_box_height \
                and len(self.user_current_pkmn.moveset)>=2:

                    move = self.user_current_pkmn.moveset[1]
                    print(move.name)
                    self.battle_action(move)
            # case move three exists and is clicked
            elif 1 * TILE_WIDTH <= x <= 1 * TILE_WIDTH + self.move_box_width \
                and 0.5 * TILE_HEIGHT <= y <= 0.5 * TILE_HEIGHT + self.move_box_height \
                and len(self.user_current_pkmn.moveset)>=3:

                    move = self.user_current_pkmn.moveset[2]
                    print(move.name)
                    self.battle_action(move)
            # case move four exists and is clicked
            elif 10 * TILE_WIDTH <= x <= 10 * TILE_WIDTH + self.move_box_width \
                and 0.5 * TILE_HEIGHT <= y <= 0.5 * TILE_HEIGHT + self.move_box_height \
                and len(self.user_current_pkmn.moveset)>=4:

                    move = self.user_current_pkmn.moveset[3]
                    print(move.name)
                    self.battle_action(move)
            # case back button is clicked
            elif 19 * TILE_WIDTH <= x <= 23 * TILE_WIDTH \
                    and 1.5 * TILE_HEIGHT <= y <= 5 * TILE_HEIGHT:

                print("BACK CLICKED")
                self.curr_menu = 0


        # Case in pokemon menu
        elif self.curr_menu == 3:
            # Case mon 1 exists and may be switched to and is switched to
            if 1 * TILE_WIDTH <= x <= 1 * TILE_WIDTH + self.switch_box_width \
                and 3.25 * TILE_HEIGHT <= y <= 3.25 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 1 and not self.trainer.team[0].fainted and self.user_current_pkmn is not self.trainer.team[0]:
                    print("User switched to 0")
                    self.user_switched(0)

            # Case mon 2 exists and may be switched to and is switched to
            elif 1 * TILE_WIDTH <= x <= 1 * TILE_WIDTH + self.switch_box_width \
                and 0.5 * TILE_HEIGHT <= y <= 0.5 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 2 and not self.trainer.team[1].fainted and self.user_current_pkmn is not self.trainer.team[1]:
                    print("User switched to 1")
                    self.user_switched(1)

            # Case mon 3 exists and may be switched to and is switched to
            elif 7 * TILE_WIDTH <= x <= 7 * TILE_WIDTH + self.switch_box_width \
                and 3.25 * TILE_HEIGHT <= y <= 3.25 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 3 and not self.trainer.team[2].fainted and self.user_current_pkmn is not self.trainer.team[2]:
                    print("User switched to 2")
                    self.user_switched(2)

            # Case mon 4 exists and may be switched to and is switched to
            elif 7 * TILE_WIDTH <= x <= 7 * TILE_WIDTH + self.switch_box_width \
                and 0.5 * TILE_HEIGHT <= y <= 0.5 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 4 and not self.trainer.team[3].fainted and self.user_current_pkmn is not self.trainer.team[3]:
                    print("User switched to 3")
                    self.user_switched(3)

            # Case mon 5 exists and may be switched to and is switched to
            elif 13 * TILE_WIDTH <= x <= 13 * TILE_WIDTH + self.switch_box_width \
                and 3.25 * TILE_HEIGHT <= y <= 3.25 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 5 and not self.trainer.team[4].fainted and self.user_current_pkmn is not self.trainer.team[4]:
                    print("User switched to 4")
                    self.user_switched(4)

            # Case mon 6 exists and may be switched to and is switched to
            elif 13 * TILE_WIDTH <= x <= 13 * TILE_WIDTH + self.switch_box_width \
                and 0.5 * TILE_HEIGHT <= y <= 0.5 * TILE_HEIGHT + self.switch_box_height \
                and len(self.trainer.team) >= 6 and not self.trainer.team[5].fainted and self.user_current_pkmn is not self.trainer.team[5]:
                    print("User switched to 5")
                    self.user_switched(5)

            # case back button is clicked
            elif 19 * TILE_WIDTH <= x <= 23 * TILE_WIDTH \
                    and 1.5 * TILE_HEIGHT <= y <= 5 * TILE_HEIGHT and self.user_current_pkmn is not None:

                print("BACK CLICKED")
                self.curr_menu = 0

    def run_action(self):
        """When run is pressed"""
        # if ... pokemon related conditions, for now just let escape occur
        escape_prob = 0
        if np.random.random() >= escape_prob:
            self.board.display_text(TextBox("You got away safely!"), 2 * REFRESH_RATE)
            self.battle_ended_bool = True

    def ended_action(self):
        """Begins end of battle sequence."""
        self.player_may_take_action = False
        self.outro_animation()
        self.board.exit_encounter()
        self.board.end_text()

    def animate_turn(self):
        """Lower HP by the correct proportional amount for one frame, dispatch all else to switch_turn."""

        # Case turn should be over
        if self.turn_counter == 2 or self.shown_effectiveness:
            self.switch_turn()
            return

        if self.curr_turn == 0:
            self.foe_current_pkmn.take_damage(self.curr_total_damage / (1.5 * REFRESH_RATE))
            self.curr_damage += self.curr_total_damage / ( 1.5 * REFRESH_RATE)
            if self.foe_current_pkmn.fainted:
                self.opponent_fainted()
                self.switch_turn()
        else:
            self.user_current_pkmn.take_damage(self.curr_total_damage / ( 1.5 * REFRESH_RATE))
            self.curr_damage += self.curr_total_damage / ( 1.5 * REFRESH_RATE)
            if self.user_current_pkmn.fainted:
                self.user_fainted()
                self.switch_turn()

        # If move is complete
        # For status moves, keep curr_damage as a timer
        if self.curr_total_damage == 0:
            self.curr_damage += 1
            if self.curr_damage == (1.5 * REFRESH_RATE):
                self.switch_turn()

        # For attacks, keep the tick as a timer
        elif self.curr_damage >= self.curr_total_damage:
            self.switch_turn()

    def switch_turn(self):
        """Swap turn, display outcome, and set up for next turn"""
        # A player has just finished a turn or wrap up

        ### First, check if entire turn or battle has ended ###
        if self.battle_ended_bool or self.turn_counter is None:
            return

        ### Then, display effectivenss of user move ###
        if not self.shown_effectiveness:
            self.display_effectiveness()
            self.shown_effectiveness = True
            return
        else:
            self.shown_effectiveness = False
            self.turn_counter += 1

        ### If turn has reached 2, dispatch back to renderer to wrap up ###
        if self.turn_counter == 2:
            self.turn_counter = None
            self.curr_turn = None
            self.curr_damage = 0
            return


        ### If user move has ended, begin agent turn ###
        if self.curr_turn == 0:
            self.is_crit, self.effectiveness, self.is_hit, self.curr_total_damage = self.opponent_turn()
            # Case item or switch, both would already have taken place
            if self.is_crit is None:
                self.turn_counter = 2
                return
            # Case opponent attacked
            else:
                self.curr_turn = 1
                self.curr_damage = 0
                if self.is_hit:
                    hit_str = ""
                else:
                    hit_str = "\n" + self.foe_current_pkmn.name+" missed!"
                if self.is_wild:
                    self.board.display_text(TextBox("The wild " + self.foe_current_pkmn.name + str(
                        " used ") + self.curr_agent_move.name + "!"+hit_str, overworld=False, unskippable=True), 0)
                else:
                    self.board.display_text(TextBox("The foe's " + self.foe_current_pkmn.name + str(
                        " used ") + self.curr_user_move.name + "!"+hit_str, overworld=False, unskippable=True), 0)

        ### If agent move has ended, begin user turn ###
        elif self.curr_turn == 1:
            self.is_crit, self.effectiveness, self.is_hit, self.curr_total_damage = self.curr_user_move.use(self.foe_current_pkmn)
            self.curr_damage = 0
            self.curr_turn = 0
            if self.is_hit:
                hit_str = ""
            else:
                hit_str = "\n" + self.user_current_pkmn.name + " missed!"
            self.board.display_text(TextBox(self.user_current_pkmn.name + str(" used ") + self.curr_user_move.name + "!"+hit_str, overworld=False, unskippable=True), 0)

    def battle_action(self, user_move: PokemonMove):
        """When a move is picked, set up one turn cycle."""
        # Determine turn order by speed
        if self.user_current_pkmn.stats["speed"] == self.foe_current_pkmn.stats["speed"]:
            order = np.random.choice(range(0,2))
        elif self.user_current_pkmn.stats["speed"] > self.foe_current_pkmn.stats["speed"]:
            order = 0
        else:
            order = 1

        # Prepare to display effectiveness
        self.shown_effectiveness = False

        # TODO: ADD SECOND SET OF SELF.IS_CRIT, ETC. AND CORRESPONDING LOGIC IN EFFECTIVENESS --> ALLOW AI SWITCH OR ITEM TO MOVE FIRST

        # Player moves first
        self.turn_counter = 0
        self.curr_turn = order
        self.curr_user_move = user_move
        if order == 0:
            self.is_crit, self.effectiveness, self.is_hit, self.curr_total_damage = user_move.use(self.foe_current_pkmn)
            self.curr_damage = 0
            if self.is_hit:
                hit_str = ""
            else:
                hit_str = "\n" + self.user_current_pkmn.name + " missed!"
            self.board.display_text(TextBox(self.user_current_pkmn.name+str(" used ")+user_move.name+"!"+hit_str, overworld=False, unskippable=True), 0)

        # Agent moves first
        else:
            self.is_crit, self.effectiveness, self.is_hit, self.curr_total_damage = self.opponent_turn()
            if self.is_crit is None:
                # Case item or switch
                return
            # Case agent used move
            self.curr_damage = 0
            if self.is_hit:
                hit_str = ""
            else:
                hit_str = "\n" + self.foe_current_pkmn.name + " missed!"
            if self.is_wild:
                self.board.display_text(TextBox("The wild "+self.user_current_pkmn.name + str(" used ") + self.curr_agent_move.name + "!"+hit_str, overworld=False, unskippable=True), 0)
            else:
                self.board.display_text(TextBox("The foe's "+self.user_current_pkmn.name + str(" used ") + self.curr_user_move.name + "!"+hit_str, overworld=False, unskippable=True), 0)

        self.curr_menu = 0

    def opponent_turn(self):
        """Allow the opponent agent to take an action."""
        ai_action = self.agent.action()
        # Case AI attacked
        if isinstance(ai_action, PokemonMove):
            self.curr_agent_move = ai_action
            return ai_action.use(self.user_current_pkmn)

        # Case AI switched
        elif isinstance(ai_action, Pokemon):
            self.opponent_switched(self.opponent.team.index(ai_action))
        # Case AI used item
        elif isinstance(ai_action, Item):
            self.opponent.use_item(ai_action.name)
            # TODO: print corresponding messages
        return None, None, None, None

    def opponent_fainted(self):
        """Ends current turn and forces agent switch."""
        if self.is_wild:
            wild_str = "The wild "
        else:
            wild_str = ""
        message = TextBox(wild_str+self.foe_current_pkmn.name+str(" fainted!"), unskippable=True, overworld=False)
        self.board.display_text(message, 1 * REFRESH_RATE)
        living_mons = len([mon for mon in self.opponent.team if not mon.fainted])
        if living_mons == 0:
            self.battle_ended_bool = True
        else:
            self.curr_turn = None
            new_mon = self.agent.switch()
            self.opponent_switched(new_mon)

        self.recently_deceased = self.foe_current_pkmn
        self.foe_current_pkmn = None
        self.award_xp()

    def user_fainted(self):
        """Ends current turn and forces user switch"""
        message = TextBox(self.user_current_pkmn.name+str(" fainted!"), overworld=False, unskippable=False)
        self.board.display_text(message, 1 * REFRESH_RATE)
        living_mons = len([mon for mon in self.trainer.team if not mon.fainted])
        if living_mons == 0:
            self.battle_ended_bool = True
        else:
            self.switch_forced = True
            self.curr_turn = None
            self.curr_menu = 3

        self.user_current_pkmn = None

    def opponent_switched(self, ind: int):
        """Helper method to set fields with new foe pokemon."""
        ### FIRST HALF ###
        if not self.mid_switch:
            if self.foe_current_pkmn is not None:
                self.board.display_text(TextBox(self.agent.trainer.name+" withdrew "+self.foe_current_pkmn.name+"!", overworld=False, unskippable=True), 1 * REFRESH_RATE)
                self.foe_current_pkmn = None
            self.mid_switch = True
            self.ind_to_switch_to = ind

        ### SECOND HALF ###
        else:
            self.foe_current_pkmn = self.opponent.team[self.ind_to_switch_to]
            self.board.display_text(TextBox("Opponent sent out "+self.foe_current_pkmn.name+"!", overworld=False, unskippable=True), 1 * REFRESH_RATE)
            self.mid_switch = False

            # User has battled current foe
            self.user_current_pkmn.seen.append(self.foe_current_pkmn)

    def user_switched(self, ind: int):
        """Helper method to set fields and flags for new user pokemon."""
        ### FIRST HALF ###
        if not self.mid_switch:
            if self.user_current_pkmn is not None:
                self.board.display_text(TextBox("That's enough, come back " + self.user_current_pkmn.name + "!", overworld=False, unskippable=True), 1 * REFRESH_RATE)
                self.user_current_pkmn = None
            self.mid_switch = True
            self.ind_to_switch_to = ind

        ### SECOND HALF ###
        else:
            self.user_current_pkmn = self.trainer.team[self.ind_to_switch_to]
            self.board.display_text(TextBox("Go, " + self.user_current_pkmn.name + "!", overworld=False, unskippable=True))
            self.mid_switch = False

            # Has battled current foe
            self.user_current_pkmn.seen.append(self.foe_current_pkmn)

        if not self.switch_forced:
            self.user_switched_bool = True
        elif not self.mid_switch:
            self.switch_forced = False

        self.curr_menu = 0

    def battle_ended(self):
        """Dispatch needed logic and close encounter."""
        # TODO: CALCULATE HOW MUCH $$ TO ADD TO PLAYER WALLET
        # TODO: PRINT MESSAGE
        self.ended_action()

    def display_effectiveness(self):
        """Send to screen the effectiveness and critical hit outcome of a move."""
        crit_text = ""
        if self.is_crit:
            crit_text = "A critical hit!"
        if self.effectiveness == 0 or (self.curr_turn == 0 and self.curr_user_move.is_status) \
                or (self.curr_turn == 1 and self.curr_agent_move.is_status):
            if self.is_crit:
                self.board.display_text(TextBox(crit_text, overworld=False, unskippable=True), 1 * REFRESH_RATE)
            return
        if self.effectiveness == -2:
            self.board.display_text(TextBox("It doesn't affect "+self.foe_current_pkmn.name+"...", overworld=False, unskippable=True), 1 * REFRESH_RATE)
        elif self.effectiveness == -1:
            self.board.display_text(TextBox("It's not very effective..."+"\n"+crit_text, overworld=False, unskippable=True), 1 * REFRESH_RATE)
        elif self.effectiveness == 1:
            self.board.display_text(TextBox("It's super effective!"+"\n"+crit_text, overworld=False, unskippable=True), 1 * REFRESH_RATE)

    def render_items_menu(self):
        # TODO: make items menu and corresponding mouse parsing
        pass

    def render_battle_menu(self):

        move_objects = []

        num_moves = len(self.user_current_pkmn.moveset)
        move_colors = [TYPE_TO_COLOR[move.type] for move in self.user_current_pkmn.moveset]

        if num_moves >= 1:
            move_box_one = pg.shapes.BorderedRectangle(x = 1 * TILE_WIDTH, y = 3.25 * TILE_HEIGHT,
                                                       width=self.move_box_width, height=self.move_box_height,
                                                       color=move_colors[0], border_color=(0,0,0), border=3,
                                                       batch=self.batches[3])
            text_one = self.user_current_pkmn.moveset[0].name+"\n"+str(self.user_current_pkmn.moveset[0].pp)+" / "+str(self.user_current_pkmn.moveset[0].max_pp)

            move_title_one = pg.text.Label(text=text_one,
                                           x = 1.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                           y = 5 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                           color=(0,0,0,255), batch=self.batches[4])
            move_objects.extend([move_box_one, move_title_one])
        if num_moves >= 2:
            move_box_two = pg.shapes.BorderedRectangle(x = 10 * TILE_WIDTH, y = 3.25 * TILE_HEIGHT,
                                                       width=self.move_box_width, height=self.move_box_height,
                                                       color=move_colors[1], border_color=(0,0,0), border=3,
                                                       batch=self.batches[3])
            text_two = self.user_current_pkmn.moveset[1].name+"\n"+str(self.user_current_pkmn.moveset[1].pp)+" / "+str(self.user_current_pkmn.moveset[1].max_pp)

            move_title_two = pg.text.Label(text=text_two,
                                            x = 10.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                            y = 5 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                            color=(0,0,0,255), batch=self.batches[4])
            move_objects.extend([move_box_two, move_title_two])
        if num_moves >= 3:
            move_box_three = pg.shapes.BorderedRectangle(x = 1 * TILE_WIDTH, y = 0.5 * TILE_HEIGHT,
                                                       width=self.move_box_width, height=self.move_box_height,
                                                       color=move_colors[2], border_color=(0,0,0), border=3,
                                                         batch=self.batches[3])
            text_three = self.user_current_pkmn.moveset[2].name+"\n"+str(self.user_current_pkmn.moveset[2].pp)+" / "+str(self.user_current_pkmn.moveset[2].max_pp)
            move_title_three = pg.text.Label(text=text_three,
                                           x = 1.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                           y = 2 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                           color=(0,0,0,255), batch=self.batches[4])
            move_objects.extend([move_box_three, move_title_three])
        if num_moves == 4:
            move_box_four = pg.shapes.BorderedRectangle(x = 10 * TILE_WIDTH, y = 0.5 * TILE_HEIGHT,
                                                       width=self.move_box_width, height=self.move_box_height,
                                                       color=move_colors[3], border_color=(0,0,0), border=3,
                                                        batch=self.batches[3])
            text_four = self.user_current_pkmn.moveset[3].name+"\n"+str(self.user_current_pkmn.moveset[3].pp)+" / "+str(self.user_current_pkmn.moveset[3].max_pp)
            move_title_four = pg.text.Label(text=text_four,
                                            x = 10.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                            y = 2 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                            color=(0,0,0,255), batch=self.batches[4])
            move_objects.extend([move_box_four, move_title_four])

        back_button = pg.shapes.BorderedRectangle(x = 19 * TILE_WIDTH, y = 1.5 * TILE_HEIGHT,
                                                       width=4 * TILE_WIDTH, height= 3.5 * TILE_HEIGHT,
                                                       color=(128, 237, 68), border_color=(0,0,0), border=3,
                                                        batch=self.batches[3])
        back_button_title = pg.text.Label(text="BACK",
                                            x = 21 * TILE_WIDTH, width = 4 * TILE_WIDTH,
                                            y = 3 * TILE_HEIGHT, anchor_x="center",
                                            color=(0,0,0,255), batch=self.batches[4])
        move_objects.extend([back_button, back_button_title])
        self.shapes.extend(move_objects)

    def render_pokemon_menu(self):
        """Rendering logic for switch menu."""

        pkmn_objects = []

        # Let mon colors be their primary type unless fainted
        mon_colors = [TYPE_TO_COLOR[mon.types[0]] for mon in self.trainer.team]
        for i in range(len(mon_colors)):
            if self.trainer.team[i].fainted:
                mon_colors[i] = (203, 203, 203)

        num_mons = len(self.trainer.team)

        if self.user_current_pkmn is not None:
            back_button = pg.shapes.BorderedRectangle(x=19 * TILE_WIDTH, y=1.5 * TILE_HEIGHT,
                                                      width=4 * TILE_WIDTH, height=3.5 * TILE_HEIGHT,
                                                      color=(128, 237, 68), border_color=(0, 0, 0), border=3,
                                                      batch=self.batches[3])
            back_button_title = pg.text.Label(text="BACK",
                                              x=21 * TILE_WIDTH, width=4 * TILE_WIDTH,
                                              y=3 * TILE_HEIGHT, anchor_x="center",
                                              color=(0, 0, 0, 255), batch=self.batches[4])
            pkmn_objects.extend([back_button, back_button_title])

        # If there is at least one mon
        if num_mons >= 1:
            curr_mon = self.trainer.team[0]
            switch_box_one = pg.shapes.BorderedRectangle(x = 1 * TILE_WIDTH, y = 3.25 * TILE_HEIGHT,
                                                       width=self.switch_box_width, height=self.switch_box_height,
                                                       color=mon_colors[0], border_color=(0,0,0), border=3,
                                                       batch=self.batches[3])
            text_one = curr_mon.name+" Lv."+str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(curr_mon.stats["max_hp"])

            mon_label_one = pg.text.Label(text=text_one,
                                           x = 1.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                           y = 5 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                           color=(0,0,0,255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_one, mon_label_one])

        # If there are at least 2 mons
        if num_mons >= 2:
            curr_mon = self.trainer.team[1]
            switch_box_two = pg.shapes.BorderedRectangle(x = 1 * TILE_WIDTH, y = 0.5 * TILE_HEIGHT,
                                                       width=self.switch_box_width, height=self.switch_box_height,
                                                       color=mon_colors[1], border_color=(0,0,0), border=3,
                                                       batch=self.batches[3])
            text_two = curr_mon.name+" Lv."+str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(curr_mon.stats["max_hp"])

            mon_label_two = pg.text.Label(text=text_two,
                                           x = 1.5 * TILE_WIDTH + self.move_box_width/2, width = self.move_box_width,
                                           y = 2 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                           color=(0,0,0,255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_two, mon_label_two])
        else:
            switch_box_two = pg.shapes.BorderedRectangle(x = 1 * TILE_WIDTH, y = 0.5 * TILE_HEIGHT,
                                                       width=self.switch_box_width, height=self.switch_box_height,
                                                       color=(255,255,255), border_color=(0,0,0), border=3,
                                                       batch=self.batches[3])
            pkmn_objects.extend([switch_box_two])

        # If there are at least 3 mons
        if num_mons >= 3:
            curr_mon = self.trainer.team[2]
            switch_box_three = pg.shapes.BorderedRectangle(x=7 * TILE_WIDTH, y=3.25 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=mon_colors[2], border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            text_three = curr_mon.name + " Lv." + str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(
                curr_mon.stats["max_hp"])

            mon_label_three = pg.text.Label(text=text_three,
                                          x=7.5 * TILE_WIDTH + self.move_box_width / 2, width=self.move_box_width,
                                          y=5 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                          color=(0, 0, 0, 255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_three, mon_label_three])
        else:
            switch_box_three = pg.shapes.BorderedRectangle(x=7 * TILE_WIDTH, y=3.25 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=(255, 255, 255), border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            pkmn_objects.extend([switch_box_three])

        # If there are at least 4 mons
        if num_mons >= 4:
            curr_mon = self.trainer.team[3]
            switch_box_four = pg.shapes.BorderedRectangle(x=7 * TILE_WIDTH, y=0.5 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=mon_colors[3], border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            text_four = curr_mon.name + " Lv." + str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(
                curr_mon.stats["max_hp"])

            mon_label_four = pg.text.Label(text=text_four,
                                          x=7.5 * TILE_WIDTH + self.move_box_width / 2, width=self.move_box_width,
                                          y=2 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                          color=(0, 0, 0, 255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_four, mon_label_four])
        else:
            switch_box_four = pg.shapes.BorderedRectangle(x=7 * TILE_WIDTH, y=0.5 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=(255, 255, 255), border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            pkmn_objects.extend([switch_box_four])

        # If there are at least 5 mons
        if num_mons >= 5:
            curr_mon = self.trainer.team[4]
            switch_box_five = pg.shapes.BorderedRectangle(x=13 * TILE_WIDTH, y=3.25 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=mon_colors[4], border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            text_five = curr_mon.name + " Lv." + str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(
                curr_mon.stats["max_hp"])

            mon_label_five = pg.text.Label(text=text_five,
                                          x=13.5 * TILE_WIDTH + self.move_box_width / 2, width=self.move_box_width,
                                          y=5 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                          color=(0, 0, 0, 255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_five, mon_label_five])
        else:
            switch_box_five = pg.shapes.BorderedRectangle(x=13 * TILE_WIDTH, y=3.25 * TILE_HEIGHT,
                                                         width=self.switch_box_width, height=self.switch_box_height,
                                                         color=(255, 255, 255), border_color=(0, 0, 0), border=3,
                                                         batch=self.batches[3])
            pkmn_objects.extend([switch_box_five])

        # If there are 6 mons
        if num_mons == 6:
            curr_mon = self.trainer.team[5]
            switch_box_six = pg.shapes.BorderedRectangle(x=13 * TILE_WIDTH, y=0.5 * TILE_HEIGHT,
                                                          width=self.switch_box_width, height=self.switch_box_height,
                                                          color=mon_colors[5], border_color=(0, 0, 0), border=3,
                                                          batch=self.batches[3])
            text_six = curr_mon.name + " Lv." + str(curr_mon.level) + "\n" + str(math.ceil(curr_mon.hp)) + " / " + str(
                curr_mon.stats["max_hp"])

            mon_label_six = pg.text.Label(text=text_six,
                                           x=13.5 * TILE_WIDTH + self.move_box_width / 2, width=self.move_box_width,
                                           y=2 * TILE_HEIGHT, anchor_x="center", multiline=True,
                                           color=(0, 0, 0, 255), batch=self.batches[4])
            pkmn_objects.extend([switch_box_six, mon_label_six])
        else:
            switch_box_six = pg.shapes.BorderedRectangle(x=13 * TILE_WIDTH, y=0.5 * TILE_HEIGHT,
                                                          width=self.switch_box_width, height=self.switch_box_height,
                                                          color=(255, 255, 255), border_color=(0, 0, 0), border=3,
                                                          batch=self.batches[3])
            pkmn_objects.extend([switch_box_six])

        self.shapes.extend(pkmn_objects)






