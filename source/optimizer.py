import cvxpy as cp
import data
import stats

def calculate_phyisical_damage_metric(character, item):
    # Create the damage metric
    damage_metric = sum(
        item.stats['additional_physical_damage'],
        2*item.stats['true_physical_damage'],
        item.stats['weapon_damage']
    )*(1+round(stats.physical_power_bonus(character.strength+item.stats['all_attributes_bonus']+item.stats['physical_power'])+item.stats['physical_damage_bonus']/100, 4))

    return damage_metric

def calculate_magical_damage_metric(character, item):
    # Create the damage metric
    damage_metric = sum(
        item.stats['additional_magical_damage'],
        2*item.stats['true_magical_damage'],
        (stats.spell_casting_speed(character.will+item.stats['all_attributes_bonus'])+item.stats['spell_casting_speed'])
    )*(1+round(stats.magical_power_bonus(character.will+item.stats['all_attributes_bonus']+item.stats['magical_power'])+item.stats['magical_damage_bonus']/100, 4))

    return damage_metric

def optimize_equipment(character, items):
    x = cp.Variable(len(items), boolean=True)

    constraints = []

    for item_type in data.type:
        constraints.append(cp.sum(x[i] for i in range(len(items)) if items[i].type == item_type) <= data.type[item_type])

    print(constraints)

    # Create the objective function
    objective = cp.Maximize(
        sum(
            x[i]*calculate_phyisical_damage_metric(character, items[i]) for i in range(len(items))
        ) + 
        sum(
            x[i]*calculate_magical_damage_metric(character, items[i]) for i in range(len(items))
        )
    )

    # Create the problem
    problem = cp.Problem(objective, constraints)

    # Solve the problem
    problem.solve()

    # Create a list of the best items
    best_items = [items[i] for i in range(len(items)) if x[i].value == 1]

    return best_items