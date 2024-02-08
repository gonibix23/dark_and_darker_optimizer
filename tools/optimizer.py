import cvxpy as cp
import data.stats as stats
import data.game_data as data

def calculate_physical_damage_metric(character, item):
    # Create the physical damage metric
    damage_metric = (
        item.stats["strength"]+item.stats["all_attributes_bonus"]+
        item.stats["additional_physical_damage"]+
        2*item.stats["true_physical_damage"]+
        item.stats["weapon_damage"]+
        item.stats["physical_power"]+
        item.stats["physical_damage_bonus"]+
        item.stats["additional_action_speed"]+
        item.stats["dexterity"]+
        0.5*item.stats["armor_penetration"]
        )*(1+round(stats.physical_power_bonus(character.strength+item.stats["all_attributes_bonus"]+item.stats["physical_power"])+item.stats["physical_damage_bonus"]/100, 4))
    if damage_metric < 0:
        damage_metric = 0
    return damage_metric

def calculate_magical_damage_metric(character, item):
    # Create the magical damage metric
    damage_metric = (
        item.stats["will"]+item.stats["all_attributes_bonus"]+
        item.stats["additional_magical_damage"]+
        2*item.stats["true_magical_damage"]+
        item.stats["magical_damage"]+
        item.stats["magical_power"]+
        item.stats["magical_damage_bonus"]+
        0.5*item.stats["magic_penetration"]+
        (stats.spell_casting_speed(character.will+item.stats["all_attributes_bonus"])+item.stats["additional_spell_casting_speed"])
        )*(1+round(stats.magical_power_bonus(character.will+item.stats["all_attributes_bonus"]+item.stats["magical_power"])+item.stats["magical_damage_bonus"]/100, 4))
    if damage_metric < 0:
        damage_metric = 0
    return damage_metric

def calculate_health_metric(character, item):
    # Create the health metric
    health_metric = (
        0.75*(item.stats["vigor"]+item.stats["all_attributes_bonus"])+
        0.25*(item.stats["strength"]+item.stats["all_attributes_bonus"])+
        item.stats["max_health_bonus"]+
        2*item.stats["additional_max_health"]+
        (stats.max_health(0.75*(item.stats["vigor"]+item.stats["all_attributes_bonus"]+character.vigor)+0.25*(item.stats["strength"]+item.stats["all_attributes_bonus"]+character.strength))))*(1+(item.stats["max_health_bonus"]/100))
    health_metric = health_metric/12
    if health_metric < 0:
        health_metric = 0
    return health_metric

def calculate_armor_metric(character, item):
    # Create the armor metric
    armor_metric = (
        item.stats["armor"]/10+
        item.stats["physical_damage_reduction_bonus"]+
        0.5*item.stats["projectile_damage_reduction"]+
        0.5*item.stats["headshot_damage_reduction"]
        )*(1+(stats.physical_damage_reduction(item.stats["armor"])+(item.stats["physical_damage_reduction_bonus"]/100)))
    if armor_metric < 0:
        armor_metric = 0
    return armor_metric

def calculate_magic_resist_metric(character, item):
    # Create the magic resist metric
    magic_resist_metric = (
        item.stats["magic_resist"]/10+
        item.stats["magical_damage_reduction_bonus"]
        )*(1+(stats.magical_damage_reduction(item.stats["magic_resist"])+(item.stats["magical_damage_reduction_bonus"]/100)))
    if magic_resist_metric < 0:
        magic_resist_metric = 0
    return magic_resist_metric

def calculate_move_speed_metric(character, item):
    # Create the move speed metric
    move_speed_metric = (
        item.stats["agility"]+item.stats["all_attributes_bonus"]+
        item.stats["additional_move_speed"]+
        item.stats["move_speed_bonus"]
        )*(1+((stats.move_speed((item.stats["agility"]+item.stats["all_attributes_bonus"]))+300+item.stats["additional_move_speed"]+(item.stats["move_speed_bonus"]*3))/3))
    if move_speed_metric < 0:
        move_speed_metric = 0
    return move_speed_metric

def optimize_equipment(character, items, weights):
    # Remove items that the character cannot equip
    for item in items:
        if type(character).__name__ not in item.character and "All" not in item.character:
            items.remove(item)

    # Create the optimization variables
    x = cp.Variable(len(items), boolean=True)

    constraints = []

    for item_type in data.type:
        # Create the constraint for the number of items of each type
        constraints.append(
            cp.sum([x[i] for i in range(len(items)) if items[i].type == item_type]) <= data.type[item_type]
        )

    # Create the objective function
    objective = cp.Maximize(
        sum(
            weights["physical_damage"][0]*calculate_physical_damage_metric(character, items[i])*x[i] +
            weights["magical_damage"][0]*calculate_magical_damage_metric(character, items[i])*x[i] +
            weights["health"][0]*calculate_health_metric(character, items[i])*x[i] +
            weights["armor"][0]*calculate_armor_metric(character, items[i])*x[i] +
            weights["magic_resist"][0]*calculate_magic_resist_metric(character, items[i])*x[i] +
            weights["speed"][0]*calculate_move_speed_metric(character, items[i])*x[i]
            for i in range(len(items))
        )
    )

    # Create the problem
    problem = cp.Problem(objective, constraints)

    # Solve the problem
    problem.solve(solver=cp.GUROBI)

    # Create a list of the best items
    best_items = [items[i] for i in range(len(items)) if x[i].value == 1]

    return best_items