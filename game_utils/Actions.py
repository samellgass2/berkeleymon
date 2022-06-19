from game_utils.Encounter import *
from data.Constants import *

##### ALL MOVES #####
class Splash(PokemonMove):
    def __init__(self):
        super().__init__(type=10, name="Splash", power=0, physical=True, accuracy=100,pp=35, is_status=True)

class Pound(PokemonMove):
    """Pound."""
    def __init__(self):
        super().__init__(type=0, name="Pound", power=40, physical=True, accuracy=100, pp=35)

class Tackle(PokemonMove):
    """Tackle."""
    def __init__(self):
        super().__init__(type=0, name="Tackle", power=35, physical=True, accuracy=95, pp=35)

class Withdraw(PokemonMove):
    """Withdraw."""
    def __init__(self):
        super().__init__(type=10, name="Withdraw", power=0, physical=False, accuracy=100, pp=40, is_status=True)

    def use(self, opponent):
        self.raise_stat("defense", opponent)
        self.pp -= 1

class Growl(PokemonMove):
    """Growl."""
    def __init__(self):
        super().__init__(type=0, name="Growl", power=0, physical=False, accuracy=100, pp=40, is_status=True)

    def use(self, opponent):
        opponent.raise_stat("attack", opponent, lower=True)
        self.pp -= 1

class Absorb(PokemonMove):
    """Absorb."""
    def __init__(self):
        super().__init__(type=11, name="Absorb", power=20, physical=False, accuracy=100, pp=25, is_status=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class RazorLeaf(PokemonMove):
    """Razor Leaf."""
    def __init__(self):
        super().__init__(type=11, name="Razor Leaf", power=55, accuracy=95, physical=True,pp=25)

class Curse(PokemonMove):
    """Curse."""
    def __init__(self):
        super().__init__(type=7, name="Curse", power=0, accuracy=100, physical=False, pp=10)

    def use(self, opponent):
        self.raise_stat(opponent, key="speed", lower=True, lower_self=True)
        self.raise_stat(opponent, key="attack")
        self.raise_stat(opponent, key="defense")
        self.pp -= 1
        return False, 0, True, 0

class Bite(PokemonMove):
    def __init__(self):
        super().__init__(type=16, name="Bite", power=60, accuracy=100, pp=25, physical=True)

    # TODO: may cause flinch

class MegaDrain(PokemonMove):
    def __init__(self):
        super().__init__(type=11, name="Mega drain", power=40, accuracy=100, pp=15, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class LeechSeed(PokemonMove):
    """Leech Seed."""
    def __init__(self):
        super().__init__(type=11, name="Leech Seed", power=0, physical=False, accuracy=90, pp=10, is_status=True)

    # TODO: IMPLEMENT LEECHING AS A STATUS

class Synthesis(PokemonMove):
    """Synthesis."""
    def __init__(self):
        super().__init__(type=11, name="Synthesis", power=0, physical=False, accuracy=100, pp=10, is_status=True)

    def use(self, opponent):
        healing = np.random.choice(range(self.user.stats["max_hp"] // 3, self.user.stats["max_hp"] // 2))
        self.user.take_damage(-healing)
        if self.user.trainer.board is not None:
            self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!", overworld=False, unskippable=False))
        return False, False, True, 0

class Crunch(PokemonMove):
    """Crunch."""
    def __init__(self):
        super().__init__(type=16, name="Crunch", power=80, physical=True, accuracy=100, pp=15)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # may lower defense
        if np.random.random() <= 0.2:
            self.raise_stat(opponent, "defense", lower=True)
        return is_crit, is_super_eff, is_hit, total_damage

class GigaDrain(PokemonMove):
    """Giga Drain."""
    def __init__(self):
        super().__init__(type=11, name="Mega drain", power=60, accuracy=100, pp=10, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class LeafStorm(PokemonMove):
    """Leaf Storm."""
    def __init__(self):
        super().__init__(type=11, name="Leaf Storm", power=140, accuracy=90, pp=5, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        self.raise_stat(opponent, "special attack", lower=True, lower_self=True, sharply=True)
        return is_crit, is_super_eff, is_hit, total_damage

class Earthquake(PokemonMove):
    """Earthquake."""
    def __init__(self):
        super().__init__(type=4, name="Earthquake", power=100, accuracy=100, pp=10, physical=True)

class Scratch(PokemonMove):
    """Scratch."""
    def __init__(self):
        super().__init__(type=0, name="Scratch", power=40, accuracy=100, pp=35, physical=True)

class Leer(PokemonMove):
    """Leer."""
    def __init__(self):
        super().__init__(type=0, name="Leer", power=0, accuracy=100, pp=35, physical=False)

    def use(self, opponent):
        self.raise_stat(opponent, "defense", lower=True)
        return False, False, True, 0

class Ember(PokemonMove):
    """Ember."""
    def __init__(self):
        super().__init__(type=9, name="Ember", power=40, accuracy=100, pp=25, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

class Taunt(PokemonMove):
    """Taunt."""
    def __init__(self):
        super().__init__(type=16, name="Taunt", power=0, accuracy=100, pp=20, physical=False)

    # TODO: MAKE TAUNT WORK
    def use(self, opponent):
        return False, False, True, 0

class FurySwipes(PokemonMove):
    """Fury Swipes."""
    def __init__(self):
        super().__init__(type=0, name="Fury Swipes", power=18, accuracy=80, pp=15, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        times_hit = np.random.choice(range(2,6))
        return is_crit, is_super_eff, is_hit, times_hit * total_damage

class FlameWheel(PokemonMove):
    """Flame Wheel."""
    def __init__(self):
        super().__init__(type=9, name="Flame Wheel", power=60, physical=True, accuracy=100, pp=25)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

class NastyPlot(PokemonMove):
    """Nasty Plot."""
    def __init__(self):
        super().__init__(type=16, name="Nasty Plot", power=0, physical=True, accuracy=100, pp=20)


    def use(self, opponent):
        self.raise_stat(opponent, "special attack", sharply=True)
        return False, False, True, 0

class Torment(PokemonMove):
    """Torment."""
    def __init__(self):
        super().__init__(type=16, name="Torment", power=0, physical=False, accuracy=100, pp=15)

    # TODO: figure ouot how to do torment
    def use(self, opponent):
        return False, False, True, 0

class Facade(PokemonMove):
    """Facade."""
    def __init__(self):
        super().__init__(type=0, name="Facade", power=70, physical=True, accuracy=100, pp=20)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if self.user.status is not None and self.user.status in ["paralysis", "burn", "poison"]:
            total_damage *= 2
        return is_crit, is_super_eff, is_hit, total_damage

class FireSpin(PokemonMove):
    """Fire Spin."""
    def __init__(self):
        super().__init__(type=9, name="Fire Spin", power=15, physical=True, accuracy=70, pp=15)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            turns = np.random.choice(range(2,6), p=[0.375, 0.375, 0.125, 0.125])
            opponent.inflict_secondary_status("fire spin:"+str(turns))
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(TextBox(opponent.name+" was trapped in a fiery vortex!", overworld=False))
        return is_crit, is_super_eff, is_hit, total_damage


class SlackOff(PokemonMove):
    """Slack Off."""
    def __init__(self):
        super().__init__(type=0, name="Slack Off.", power=0, physical=False, accuracy=100, pp=10, is_status=True)

    def use(self, opponent):
        healing = np.random.choice(range(self.user.stats["max_hp"] // 3, self.user.stats["max_hp"] // 2))
        self.user.take_damage(-healing)
        if self.user.trainer.board is not None:
            self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!", overworld=False, unskippable=False))
        return False, False, True, 0

class FlameThrower(PokemonMove):
    """Flame Thrower."""
    def __init__(self):
        super().__init__(type=9, name="Flame Thrower", power=95, accuracy=100, pp=15, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

class MachPunch(PokemonMove):
    """Mach Punch."""
    def __init__(self):
        super().__init__(type=1, name="Mach Punch", power=40, accuracy=100, pp=30, physical=True)

    # TODO: MAKE MOVE FIRST

class Feint(PokemonMove):
    """Feint."""
    def __init__(self):
        super().__init__(type=0, name="Feint",physical=True, power=50, accuracy=100, pp=10)

    # TODO: MAKE BREAK PROTECT

class CloseCombat(PokemonMove):
    """Close Combat."""
    def __init__(self):
        super().__init__(type=1, name="Close Combat",physical=True, power=120, accuracy=100, pp=5)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        self.raise_stat(opponent, "defense", lower=True, lower_self=True)
        self.raise_stat(opponent, "special defense", lower=True, lower_self=True)
        return is_crit, is_super_eff, is_hit, total_damage

class FlareBlitz(PokemonMove):
    """Flare Blitz."""
    def __init__(self):
        super().__init__(type=9, name="Flare Blitz", physical=True, power=120, accuracy=100, pp=15)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        self.user.take_damage(total_damage // 3)
        if self.user.trainer.board is not None:
            self.user.trainer.board.display_text(TextBox(self.user.name+" was hurt by the recoil!"))
        return is_crit, is_super_eff, is_hit, total_damage

class Punishment(PokemonMove):
    """Punishment."""
    def __init__(self):
        super().__init__(type=16, name="Punishment", physical=True, power=60, accuracy=100, pp=5)

    def use(self, opponent):
        pow_offset = 0
        if opponent.attack_stage > 0:
            pow_offset += 20 * opponent.attack_stage
        if opponent.special_attack_stage > 0:
            pow_offset += 20 * opponent.special_attack_stage
        if opponent.defense_stage > 0:
            pow_offset += 20 * opponent.defense_stage
        if opponent.special_defense_stage > 0:
            pow_offset += 20 * opponent.special_defense_stage
        if opponent.speed_stage > 0:
            pow_offset += 20 * opponent.speed_stage
        self.power += pow_offset
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        self.power -= pow_offset
        return is_crit, is_super_eff, is_hit, total_damage

class CalmMind(PokemonMove):
    """Calm Mind."""
    def __init__(self):
        super().__init__(type=16, name="Calm Mind", power=0, physical=False, accuracy=100, pp=20)


    def use(self, opponent):
        self.raise_stat(opponent, "special attack", sharply=False)
        self.raise_stat(opponent, "special defense", sharply=False)
        return False, False, True, 0

class MetalClaw(PokemonMove):
    """Metal Claw."""
    def __init__(self):
        super().__init__(type=8, name="Metal Claw", power=50, accuracy=95, pp=35, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            self.raise_stat(opponent, "attack")
        return is_crit, is_super_eff, is_hit, total_damage

class SwordsDance(PokemonMove):
    """Swords Dance."""
    def __init__(self):
        super().__init__(type=0, name="Swords Dance", power=0, accuracy=100, pp=30, physical=False)

    def use(self, opponent):
        self.pp -= 1
        self.raise_stat(opponent, "attack", sharply=True)
        return False, False, True, 0

class Swagger(PokemonMove):
    """Swagger."""
    def __init__(self):
        super().__init__(type=0, name="Swagger", power=0, physical=False, pp=10, accuracy=100)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit:
            turns = np.random.choice(range(2, 6))
            opponent.inflict_secondary_status("confusion:"+str(turns))
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(TextBox(opponent.name+" became confused!", overworld=False))
        return False, False, is_hit, 0

class DoubleTeam(PokemonMove):
    """Double Team."""
    def __init__(self):
        super().__init__(type=0, name="Double Team", power=0, physical=False, pp=15, accuracy=100)

    def use(self, opponent):
        self.raise_stat(opponent, "evasiveness", sharply=True)
        self.pp -= 1
        return False, False, True, 0

class Endeavor(PokemonMove):
    """Endeavor."""
    def __init__(self):
        super().__init__(type=0, name="Endeavor", power=0, physical=True, pp=5, accuracy=100)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            total_damage = max(opponent.hp - self.user.hp,0)
        return False, is_super_eff, is_hit, total_damage

class Whirlwind(PokemonMove):
    """Whirlwind."""
    def __init__(self):
        super().__init__(type=0, name="Whirlwind", power=0, physical=False, pp=20, accuracy=100)

    # TODO: make whirlwind immediately force random switch / end random encounters

class AerialAce(PokemonMove):
    """Aerial Ace."""
    def __init__(self):
        super().__init__(type=2, name="Aerial Ace", power=60, physical=True, pp=20, accuracy=100000)

class TakeDown(PokemonMove):
    """Take Down."""
    def __init__(self):
        super().__init__(type=0, name="Take Down", power=90, physical=True, pp=20, accuracy=85)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            self.user.take_damage(total_damage // 4)
        return is_crit, is_super_eff, is_hit, total_damage

class DefenseCurl(PokemonMove):
    """Defense Curl."""
    def __init__(self):
        super().__init__(type=0, name="Defense Curl", power=0, physical=False, pp=40, accuracy=100)

    def use(self, opponent):
        self.pp -= 1
        self.raise_stat(opponent, "defense")
        return False, False, True, 0

class Agility(PokemonMove):
    """Agility."""
    def __init__(self):
        super().__init__(type=13, name="Agility", power=0, physical=False, pp=30, accuracy=100)

    def use(self, opponent):
        self.pp -= 1
        self.raise_stat(opponent, "speed", sharply=True)
        return False, False, True, 0

class BraveBird(PokemonMove):
    """Brave Bird."""
    def __init__(self):
        super().__init__(type=2, name="Brave Bird", power=120, physical=True, pp=15, accuracy=100)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            self.user.take_damage(total_damage // 3)
        return is_crit, is_super_eff, is_hit, total_damage

class Bubble(PokemonMove):
    """Bubble."""
    def __init__(self):
        super().__init__(type=10, name="Bubble", power=20, physical=True, accuracy=100, pp=30)

class WaterSport(PokemonMove):
    """Water Sport."""
    def __init__(self):
        super().__init__(type=10, name="Water Sport", power=0, physical=False, accuracy=100, pp=15, is_status=True)

class Peck(PokemonMove):
    """Peck."""
    def __init__(self):
        super().__init__(type=2, name="Peck", power=35, physical=True, accuracy=100, pp=35)

class Bide(PokemonMove):
    """Bide."""
    def __init__(self):
        super().__init__(type=0, name="Bide", power=50, physical=True, accuracy=100, pp=10)

    # TODO: override behavior for counting turns and forcing move to be bide

class BubbleBeam(PokemonMove):
    """BubbleBeam."""
    def __init__(self):
        super().__init__(type=10, name="Bubblebeam", power=65, physical=False, accuracy=100, pp=20)

class FuryAttack(PokemonMove):
    """Fury Attack."""
    def __init__(self):
        super().__init__(type=0, name="Fury Attack", power=15, physical=True, accuracy=85, pp=20)

    # TODO: make multi-hit moves random

class Brine(PokemonMove):
    """Brine."""
    def __init__(self):
        super().__init__(type=10, name="Brine", power=65, physical=False, accuracy=100, pp=10)

    def use(self, opponent):
        """Attack: damage is doubled if below half."""
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if opponent.hp <= opponent.stats["max_hp"]//2:
            total_damage *= 2
        return is_crit, is_super_eff, is_hit, total_damage

class AquaJet(PokemonMove):
    """Aqua Jet."""
    def __init__(self):
        super().__init__(type=10, name="Aqua Jet", power=40, accuracy=100, pp=20, priority=True, physical=True)

class Whirlpool(PokemonMove):
    """Whirlpool."""
    def __init__(self):
        super().__init__(type=10, name="Whirlpool", power=15, physical=False, accuracy=85, pp=15)

    # TODO: make lingering moves

class Mist(PokemonMove):
    """Mist."""
    def __init__(self):
        super().__init__(type=14, name="Mist", power=0, physical=False, accuracy=100, pp=30, is_status=True)

    def use(self, opponent):
        self.user.reset_stat_stages()
        if self.user.trainer.board is not None:
            self.user.trainer.board.display_text(TextBox(self.user.name+"'s stats returned to normal!", overworld=False))
        return False, 0, True, 0

class QuickAttack(PokemonMove):
    """Quick Attack."""
    def __init__(self):
        super().__init__(type=0, name="Quick Attack", power=40, accuracy=100, pp=30, physical=True, priority=True)

class WingAttack(PokemonMove):
    """Wing Attack."""
    def __init__(self):
        super().__init__(type=2, name="Wing Attack", power=60, accuracy=100, pp=35, physical=True)

class DrillPeck(PokemonMove):
    """Drill Peck."""
    def __init__(self):
        super().__init__(type=2, name="Drill Peck", power=80, physical=True, accuracy=100, pp=20)

class HydroPump(PokemonMove):
    """Hydro Pump."""
    def __init__(self):
        super().__init__(type=10, name="Hydro Pump", power=120, physical=False, accuracy=80, pp=5)

class Rollout(PokemonMove):
    """Rollout."""
    def __init__(self):
        super().__init__(type=5, name="Rollout", power=30, accuracy=90, pp=20, physical=True)

    # TODO: make hit over 5 turns

class Headbutt(PokemonMove):
    """Headbutt."""
    def __init__(self):
        super().__init__(type=0, name="Headbutt", power=70, accuracy=90, pp=15, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.3:
            opponent.inflict_secondary_status("flinch")
        return is_crit, is_super_eff, is_hit, total_damage

class HyperFang(PokemonMove):
    """Hyper Fang."""
    def __init__(self):
        super().__init__(type=0, name="Hyper Fang", power=85, accuracy=100, pp=15, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_secondary_status("flinch")
        return is_crit, is_super_eff, is_hit, total_damage

class SuperFang(PokemonMove):
    """Super Fang."""
    def __init__(self):
        super().__init__(type=0, name="Super Fang", power=0, accuracy=100, pp=10, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            total_damage = opponent.hp // 2
        return is_crit, is_super_eff, is_hit, total_damage

class Superpower(PokemonMove):
    """Super Fang."""
    def __init__(self):
        super().__init__(type=1, name="Superpower", power=120, accuracy=100, pp=5, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2:
            self.raise_stat(opponent, "defense", lower=True, lower_self=True)
            self.raise_stat(opponent, "attack", lower=True, lower_self=True)

class Yawn(PokemonMove):
    """Yawn."""
    def __init__(self):
        super().__init__(type=0, name="Yawn", power=0, physical=False, pp=10, accuracy=100)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit:
            opponent.inflict_secondary_status("yawn:1")
        return False, False, is_hit, 0

class Amnesia(PokemonMove):
    """Amnesia."""
    def __init__(self):
        super().__init__(type=13, name="Amnesia", power=0, physical=False, pp=20, accuracy=100)

    def use(self, opponent):
        self.pp -= 1
        self.raise_stat(opponent, "special defense", sharply=True)
        return False, False, True, 0

class WaterGun(PokemonMove):
    """Water Gun."""
    def __init__(self):
        super().__init__(type=10, name="Water Gun", power=40, accuracy=100, pp=25, physical=False)

class BugBite(PokemonMove):
    """Bug Bite."""
    def __init__(self):
        super().__init__(type=6, name="Bug Bite", power=60, accuracy=100, pp=20, physical=True)

    # TODO: make eat berry if holding berry

class FuryCutter(PokemonMove):
    """Fury Cutter."""
    def __init__(self):
        super().__init__(type=6, name="Fury Cutter", power=10, accuracy=95, pp=20, physical=True)

    # TODO: rises in power for successive hits

class LeechLife(PokemonMove):
    """Leech Life."""
    def __init__(self):
        super().__init__(type=6, name="Leech Life", power=20, accuracy=100, pp=15, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit and is_super_eff > -2:
            self.user.take_damage(-total_damage // 2)
            if self.user.trainer.board is not None:
                self.user.trainer.board.display_text(
                TextBox(self.user.name + " was healed!", overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class Sing(PokemonMove):
    """Sing."""
    def __init__(self):
        super().__init__(type=0, name="Sing", power=0, accuracy=55, pp=15, physical=False)

    def use(self, opponent):
        self.pp -= 1
        opponent.inflict_status("sleep")
        return False, 0, True, 0

class FocusEnergy(PokemonMove):
    """Focus Energy."""
    def __init__(self):
        super().__init__(type=0, name="Focus Energy", power=0, accuracy=100, pp=30, physical=False)

    # TODO: MAKE CRIT STAGES
    def use(self, opponent):
        self.pp -=1
        #self.inflict_status(opponent, "crit ?")
        return False, 0, True, 0

class XScissor(PokemonMove):
    """X-Scissor."""
    def __init__(self):
        super().__init__(type=6, name="X-Scissor", power=80, accuracy=100, pp=15, physical=True)

class Screech(PokemonMove):
    """Screech."""
    def __init__(self):
        super().__init__(type=0, name="Screech", power=0, accuracy=85, pp=40, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit and is_super_eff > -2:
            self.raise_stat(opponent, "defense", sharply=True, lower=True)
        return False, is_super_eff, is_hit, 0

class BugBuzz(PokemonMove):
    """Bug Buzz."""
    def __init__(self):
        super().__init__(type=6, name="Bug Buzz", power=90, accuracy=100, pp=10, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if is_hit and is_super_eff > -2 and np.random.random() <= 0.1:
            self.raise_stat(opponent, "special defense", lower=True)
        return is_crit, is_super_eff, is_hit, total_damage

class PerishSong(PokemonMove):
    """Perish Song."""
    def __init__(self):
        super().__init__(type=0, name="Perish Song", power=0, accuracy=100, pp=5, physical=False)

    def use(self, opponent):
        self.pp -= 1
        opponent.inflict_secondary_status("perish song: 3")
        return False, 0, True, 0

# TODO: HANDLE PERISH SONG AND ALL STATUS AT END OF TURN
