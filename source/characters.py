import stats

class Character(object):
    def __init__(self, strength, vigor, agility, dexterity, will, knowledge, resourcfulness):
        # Primary Stats
        self.strength = strength
        self.vigor = vigor
        self.agility = agility
        self.dexterity = dexterity
        self.will = will
        self.knowledge = knowledge
        self.resourcfulness = resourcfulness

        # Secondary Stats
        self.luck = 0

        self.all_attributes_bonus = 0

        self.max_health_bonus = 0
        self.additional_max_health = 0
        self.magical_healing = 0

        self.weapon_damage = 0
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

        # Equipment
        self.equipment = {'Head': None, 'Chest': None, 'Legs': None, 'Hands': None, 'Foot': None, 'Primary Weapon': None, 'Necklace': None, 'Back': None, 'Ring': []}

        self.calculate_stats()

    def __str__(self):
        return f"Strength: {self.strength}\nVigor: {self.vigor}\nAgility: {self.agility}\nDexterity: {self.dexterity}\nWill: {self.will}\nKnowledge: {self.knowledge}\nResourcfulness: {self.resourcfulness}\n\nMax Health: {self.max_health}\nHealth Recovery: {self.health_recovery}\nMove Speed: {self.move_speed}\nItem Equip Speed: {self.item_equip_speed}\nManual Dexterity: {self.manual_dexterity}\nMagic Resist: {self.magic_resist}\nPhysical Power Bonus: {self.physical_power_bonus}\nMagical Power Bonus: {self.magical_power_bonus}\nBuff Duration: {self.buff_duration}\nDebuff Duration: {self.debuff_duration}\nPersuasiveness: {self.persuasiveness}\nSpell Casting Speed: {self.spell_casting_speed}\nMemory Capacity: {self.memory_capacity}\nMemory Recovery: {self.memory_recovery}\nAction Speed: {self.action_speed}\nMagical Interaction Speed: {self.magical_interaction_speed}\nRegular Interaction Speed: {self.regular_interaction_speed}\nMagical Damage Reduction: {self.magical_damage_reduction}\nPhysical Damage Reduction: {self.physical_damage_reduction}\n\n{self.equipment_to_string()}"

    def calculate_stats(self):
        self.max_health = round((stats.max_health((self.vigor+self.all_attributes_bonus)*0.75+(self.strength+self.all_attributes_bonus)*0.25)+self.additional_max_health)*(1+(self.max_health_bonus/100)), 4)
        self.health_recovery = round(stats.health_recovery(self.vigor+self.all_attributes_bonus), 4)

        self.move_speed = round(stats.move_speed((self.agility+self.all_attributes_bonus))+300+self.additional_move_speed+(self.move_speed_bonus*3), 4)

        self.item_equip_speed = round(stats.item_equip_speed(self.dexterity+self.all_attributes_bonus), 4)
        self.manual_dexterity = round(stats.manual_dexterity(self.dexterity+self.all_attributes_bonus), 4)
        self.magic_resist = round(stats.magic_resistance(self.will+self.all_attributes_bonus), 4)

        self.magical_power_bonus = round(stats.magical_power_bonus(self.will+self.all_attributes_bonus+self.magical_power)+self.magical_damage_bonus/100, 4)
        self.physical_power_bonus = round(stats.physical_power_bonus(self.strength+self.all_attributes_bonus+self.physical_power)+self.physical_damage_bonus/100, 4)

        self.buff_duration = round(stats.buff_duration(self.will+self.all_attributes_bonus)+self.additional_buff_duration/100, 4)
        self.debuff_duration = round(stats.debuff_duration(self.will+self.all_attributes_bonus)+self.additional_debuff_duration/100, 4)
        self.persuasiveness = round(stats.persuasiveness(self.resourcfulness+self.all_attributes_bonus), 4)

        self.spell_casting_speed = round(stats.spell_casting_speed(self.knowledge+self.all_attributes_bonus)+self.additional_spell_casting_speed/100, 4)
        self.memory_capacity = round(stats.memory_capacity(self.knowledge+self.all_attributes_bonus), 4)
        self.memory_recovery = round(stats.memory_recovery(self.knowledge+self.all_attributes_bonus), 4)

        self.action_speed = round(stats.action_speed((self.agility+self.all_attributes_bonus)*0.25+(self.dexterity+self.all_attributes_bonus)*0.75)+(self.additional_action_speed/100), 4)

        self.magical_interaction_speed = round(stats.magical_interaction_speed(self.will+self.all_attributes_bonus)+self.additional_magic_interaction_speed, 4)
        self.regular_interaction_speed = round(stats.regular_interaction_speed((self.agility+self.all_attributes_bonus)*0.4+(self.resourcfulness+self.all_attributes_bonus)*0.6)+self.additional_regular_interaction_speed, 4)

        self.magical_damage_reduction = round(stats.magical_damage_reduction(self.magic_resist)+(self.magical_damage_reduction_bonus/100), 4)
        self.physical_damage_reduction = round(stats.physical_damage_reduction(self.armor)+(self.physical_damage_reduction_bonus/100), 4)

    def equip_item(self, item):
        if item.type == 'Ring':
            if len(self.equipment['Ring']) < 2:
                self.equipment['Ring'].append(item)
            else:
                self.unequip_item(self.equipment['Ring'].pop(0))
                self.equipment['Ring'].append(item)
        else:
            self.unequip_item(self.equipment[item.type])
            self.equipment[item.type] = item

        for stat in item.stats:
            setattr(self, stat, getattr(self, stat) + item.stats[stat])

        self.calculate_stats()

    def unequip_item(self, item):
        if item:
            for stat in item.stats:
                setattr(self, stat, getattr(self, stat) - item.stats[stat])

    def get_stats(self):
        return {
            "Strength": self.strength,
            "Vigor": self.vigor,
            "Agility": self.agility,
            "Dexterity": self.dexterity,
            "Will": self.will,
            "Knowledge": self.knowledge,
            "Resourcfulness": self.resourcfulness,
            "Luck": self.luck,
            "Max Health": self.max_health,
            "Move Speed": f"{self.move_speed} / {round(self.move_speed/3, 2)}%",
            "Action Speed": f"{round(self.action_speed*100, 2)}%",
            "Physical Power Bonus": f"{round(self.physical_power_bonus*100, 2)}%",
            "Magical Power Bonus": f"{round(self.magical_power_bonus*100, 2)}%",
            "Spell Casting Speed": f"{round(self.spell_casting_speed*100, 2)}%",
            "Armor Rating": self.armor,
            "Magic Resist": self.magic_resist,
            "Magical Damage Reduction": f"{round(self.magical_damage_reduction*100, 2)}%",
            "Physical Damage Reduction": f"{round(self.physical_damage_reduction*100, 2)}%",
            "Headshot Damage Reduction": f"{round(self.headshot_damage_reduction, 2)}%",
            "Projectile Damage Reduction": f"{round(self.projectile_damage_reduction*100, 2)}%",
            "Memory Capacity": self.memory_capacity,
            "Memory Recovery": f"{round(self.memory_recovery*100, 2)}%",
            "Health Recovery": f"{round(self.health_recovery*100, 2)}%",
            "Item Equip Speed": f"{round(self.item_equip_speed*100, 2)}%",
            "Manual Dexterity": f"{round(self.manual_dexterity*100, 2)}%",
            "Buff Duration": f"{round(self.buff_duration*100, 2)}%",
            "Debuff Duration": f"{round(self.debuff_duration*100, 2)}%",
            "persuasiveness": self.persuasiveness,
            "Magical Interaction Speed": f"{self.magical_interaction_speed*100}%",
            "Regular Interaction Speed": f"{self.regular_interaction_speed*100}%",
            "Magical Healing": self.magical_healing,
            "True Physical Damage": self.true_physical_damage,
            "True Magical Damage": self.true_magical_damage,
            "Additional Physical Damage": self.additional_physical_damage,
            "Additional Magical Damage": self.additional_magical_damage,
            "Armor Penetration": f"{round(self.armor_penetration, 2)}%",
            "Magic Penetration": f"{round(self.magic_penetration, 2)}%"
        }

    def equipment_to_string(self):
        equipment = ""
        for item in self.equipment:
            if item:
                equipment += f"{item} - {self.equipment[item]}\n"
        return equipment


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

def create_character(selected_class):
    if selected_class == "Wizard":
        return Wizard()
    elif selected_class == "Fighter":
        return Fighter()
    elif selected_class == "Cleric":
        return Cleric()
    elif selected_class == "Warlock":
        return Warlock()
    elif selected_class == "Bard":
        return Bard()
    elif selected_class == "Ranger":
        return Ranger()
    elif selected_class == "Barbarian":
        return Barbarian()
    elif selected_class == "Rogue":
        return Rogue()
    elif selected_class == "Druid":
        return Druid()