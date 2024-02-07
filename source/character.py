import stats

class Character(object):
    def __init__(self, strength, vigor, agility, dexterity, will, knowledge, resourcfulness):
        self.strength = strength
        self.vigor = vigor
        self.agility = agility
        self.dexterity = dexterity
        self.will = will
        self.knowledge = knowledge
        self.resourcfulness = resourcfulness

        self.luck = 0

        self.all_atributes_bonus = 0

        self.max_health_bonus = 0
        self.additional_max_health = 0
        self.magical_healing = 0

        self.true_physical_damage = 0
        self.true_magical_damage = 0
        self.additional_physical_damage = 0
        self.additional_magical_damage = 0

        self.magic_resist = 0
        self.armor = 0

        self.additional_move_speed = 0
        self.move_speed_bonus = 0

        self.additional_buff_duration = 0
        self.additional_debuff_duration = 0

        self.additional_action_speed = 0
        self.additional_spell_casting_speed = 0
        self.additional_magic_interaction_speed = 0
        self.additional_regular_interaction_speed = 0

        self.physical_power = 0
        self.magical_power = 0
        self.physical_damage_bonus = 0
        self.magical_damage_bonus = 0

        self.armor_penetration = 0
        self.magic_penetration = 0

        self.headshot_damage_reduction = 0
        self.projectile_damage_reduction = 0
        self.physical_damage_reduction_bonus = 0
        self.magical_damage_reduction_bonus = 0

        self.calculate_stats()

    def __str__(self):
        return f"Strength: {self.strength}\nVigor: {self.vigor}\nAgility: {self.agility}\nDexterity: {self.dexterity}\nWill: {self.will}\nKnowledge: {self.knowledge}\nResourcfulness: {self.resourcfulness}\n\nMax Health: {self.max_health}\nHealth Recovery: {self.health_recovery}\nMove Speed: {self.move_speed}\nItem Equip Speed: {self.item_equip_speed}\nManual Dexterity: {self.manual_dexterity}\nMagic Resist: {self.magic_resist}\nPhysical Power Bonus: {self.physical_power_bonus}\nMagical Power Bonus: {self.magical_power_bonus}\nBuff Duration: {self.buff_duration}\nDebuff Duration: {self.debuff_duration}\nPersuasiveness: {self.persuasiveness}\nSpell Casting Speed: {self.spell_casting_speed}\nMemory Capacity: {self.memory_capacity}\nMemory Recovery: {self.memory_recovery}\nAction Speed: {self.action_speed}\nMagical Interaction Speed: {self.magical_interaction_speed}\nRegular Interaction Speed: {self.regular_interaction_speed}\nMagical Damage Reduction: {self.magical_damage_reduction}\nPhysical Damage Reduction: {self.physical_damage_reduction}"

    def calculate_stats(self):
        self.max_health = (stats.max_health((self.vigor+self.all_atributes_bonus)*0.75+(self.strength+self.all_atributes_bonus)*0.25)+self.additional_max_health)*self.max_health_bonus
        self.health_recovery = stats.health_recovery(self.vigor+self.all_atributes_bonus)
        
        self.move_speed = stats.move_speed((self.agility+self.all_atributes_bonus))+300+self.additional_move_speed

        self.item_equip_speed = stats.item_equip_speed(self.dexterity+self.all_atributes_bonus)
        self.manual_dexterity = stats.manual_dexterity(self.dexterity+self.all_atributes_bonus)
        self.magic_resist = stats.magic_resistance(self.will+self.all_atributes_bonus)+self.magic_resist
        
        self.magical_power_bonus = stats.magical_power_bonus(self.will+self.all_atributes_bonus+self.magical_power)+self.magical_damage_bonus
        self.physical_power_bonus = stats.physical_power_bonus(self.strength+self.all_atributes_bonus+self.physical_power)+self.physical_damage_bonus

        self.buff_duration = stats.buff_duration(self.will+self.all_atributes_bonus)+self.additional_buff_duration
        self.debuff_duration = stats.debuff_duration(self.will+self.all_atributes_bonus)+self.additional_debuff_duration
        self.persuasiveness = stats.persuasiveness(self.resourcfulness+self.all_atributes_bonus)

        self.spell_casting_speed = stats.spell_casting_speed(self.knowledge+self.all_atributes_bonus)+self.additional_spell_casting_speed
        self.memory_capacity = stats.memory_capacity(self.knowledge+self.all_atributes_bonus)
        self.memory_recovery = stats.memory_recovery(self.knowledge+self.all_atributes_bonus)

        self.action_speed = stats.action_speed((self.agility+self.all_atributes_bonus)*0.25+(self.dexterity+self.all_atributes_bonus)*0.75)+self.additional_action_speed

        self.magical_interaction_speed = stats.magical_interaction_speed(self.will+self.all_atributes_bonus)+self.additional_magic_interaction_speed
        self.regular_interaction_speed = stats.regular_interaction_speed((self.agility+self.all_atributes_bonus)*0.4+(self.resourcfulness+self.all_atributes_bonus)*0.6)+self.additional_regular_interaction_speed

        self.magical_damage_reduction = stats.magical_damage_reduction(self.magic_resist)+self.magical_damage_reduction_bonus
        self.physical_damage_reduction = stats.physical_damage_reduction(self.armor)+self.physical_damage_reduction_bonus


class Wizard(Character):
    def __init__(self):
        super().__init__(
            strength = 6,
            vigor = 7,
            agility = 15,
            dexterity = 17,
            will = 20,
            knowledge = 28, # 25 Without the bonus of the ability
            resourcfulness = 15
        )

class Fighter(Character):
    def __init__(self):
        super().__init__(
            strength = 15,
            vigor = 15,
            agility = 15,
            dexterity = 15,
            will = 15,
            knowledge = 15,
            resourcfulness = 15
        )

class Cleric(Character):
    def __init__(self):
        super().__init__(
            strength = 11,
            vigor = 13,
            agility = 12,
            dexterity = 14,
            will = 25,
            knowledge = 20,
            resourcfulness = 10
        )

class Warlock(Character):
    def __init__(self):
        super().__init__(
            strength = 13,
            vigor = 14,
            agility = 14,
            dexterity = 15,
            will = 22,
            knowledge = 15,
            resourcfulness = 12
        )

class Bard(Character):
    def __init__(self):
        super().__init__(
            strength = 13,
            vigor = 13,
            agility = 13,
            dexterity = 20,
            will = 11,
            knowledge = 20,
            resourcfulness = 15
        )

class Ranger(Character):
    def __init__(self):
        super().__init__(
            strength = 10,
            vigor = 10,
            agility = 20,
            dexterity = 18,
            will = 10,
            knowledge = 12,
            resourcfulness = 25
        )

class Barbarian(Character):
    def __init__(self):
        super().__init__(
            strength = 25,
            vigor = 25,
            agility = 13,
            dexterity = 12,
            will = 18,
            knowledge = 5,
            resourcfulness = 7
        )

class Rogue(Character):
    def __init__(self):
        super().__init__(
            strength = 5,
            vigor = 5,
            agility = 25,
            dexterity = 25,
            will = 10,
            knowledge = 10,
            resourcfulness = 25
        )

class Druid(Character):
    def __init__(self):
        super().__init__(
            strength = 10,
            vigor = 10,
            agility = 15,
            dexterity = 15,
            will = 25,
            knowledge = 20,
            resourcfulness = 15
        )