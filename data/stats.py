def physical_power_bonus(value):
    if 0 <= value < 5:
        return -0.8 + 0.1 * abs(value - 0)
    elif 5 <= value < 7:
        return -0.3 + 0.05 * abs(value - 5)
    elif 7 <= value < 11:
        return -0.2 + 0.03 * abs(value - 7)
    elif 11 <= value < 15:
        return -0.08 + 0.02 * abs(value - 11)
    elif 15 <= value < 50:
        return 0 + 0.01 * abs(value - 15)
    elif 50 <= value < 100:
        return 0.35 + 0.005 * abs(value - 50)
    else:
        if 0.35 + 0.005 * abs(value - 50) < 1:
            return 0.35 + 0.005 * abs(value - 50)
        else:
            return 1
    
def health_recovery(value):
    if 0 <= value < 5:
        return -0.55 + 0.05 * abs(value - 0)
    elif 5 <= value < 15:
        return -0.3 + 0.03 * abs(value - 5)
    elif 15 <= value < 25:
        return 0 + 0.07 * abs(value - 15)
    elif 25 <= value < 35:
        return 0.7 + 0.05 * abs(value - 25)
    elif 35 <= value < 84:
        return 1.2 + 0.02 * abs(value - 35)
    elif 84 <= value < 85:
        return 2.18 + 0.01 * abs(value - 84)
    elif 85 <= value < 86:
        return 2.19 + 0.03 * abs(value - 85)
    else:
        return 2.22 + 0.02 * abs(value - 86)

def move_speed(value):
    if 0 <= value < 15:
        return -30 + 2 * abs(value - 0)
    elif 15 <= value < 45:
        return 0 + 1 * abs(value - 15)
    elif 45 <= value < 46:
        return 30 + 0 * abs(value - 45)
    elif 46 <= value < 47:
        return 30 + 1 * abs(value - 46)
    elif 47 <= value < 48:
        return 31 + 0 * abs(value - 47)
    elif 48 <= value < 49:
        return 31 + 1 * abs(value - 48)
    elif 49 <= value < 50:
        return 32 + 0 * abs(value - 49)
    elif 50 <= value < 51:
        return 32 + 1 * abs(value - 50)
    elif 51 <= value < 52:
        return 33 + 0 * abs(value - 51)
    elif 52 <= value < 53:
        return 33 + 1 * abs(value - 52)
    elif 53 <= value < 54:
        return 34 + 0 * abs(value - 53)
    elif 54 <= value < 55:
        return 34 + 1 * abs(value - 54)
    elif 55 <= value < 56:
        return 35 + 0 * abs(value - 55)
    elif 56 <= value < 57:
        return 35 + 1 * abs(value - 56)
    elif 57 <= value < 58:
        return 36 + 0 * abs(value - 57)
    elif 58 <= value < 59:
        return 36 + 1 * abs(value - 58)
    elif 59 <= value < 60:
        return 37 + 0 * abs(value - 59)
    elif 60 <= value < 61:
        return 37 + 1 * abs(value - 60)
    elif 61 <= value < 62:
        return 38 + 0 * abs(value - 61)
    elif 62 <= value < 63:
        return 38 + 1 * abs(value - 62)
    elif 63 <= value < 64:
        return 39 + 0 * abs(value - 63)
    elif 64 <= value < 65:
        return 39 + 1 * abs(value - 64)
    elif 65 <= value < 67:
        return 40 + 0 * abs(value - 65)
    elif 67 <= value < 68:
        return 40 + 1 * abs(value - 67)
    elif 68 <= value < 70:
        return 41 + 0 * abs(value - 68)
    elif 70 <= value < 71:
        return 41 + 1 * abs(value - 70)
    elif 71 <= value < 73:
        return 42 + 0 * abs(value - 71)
    elif 73 <= value < 74:
        return 42 + 1 * abs(value - 73)
    elif 74 <= value < 76:
        return 43 + 0 * abs(value - 74)
    elif 76 <= value < 77:
        return 43 + 1 * abs(value - 76)
    elif 77 <= value < 79:
        return 44 + 0 * abs(value - 77)
    elif 79 <= value < 80:
        return 44 + 1 * abs(value - 79)
    elif 80 <= value < 82:
        return 45 + 0 * abs(value - 80)
    elif 82 <= value < 83:
        return 45 + 1 * abs(value - 82)
    elif 83 <= value < 85:
        return 46 + 0 * abs(value - 83)
    elif 85 <= value < 86:
        return 46 + 1 * abs(value - 85)
    elif 86 <= value < 88:
        return 47 + 0 * abs(value - 86)
    elif 88 <= value < 89:
        return 47 + 1 * abs(value - 88)
    elif 89 <= value < 91:
        return 48 + 0 * abs(value - 89)
    elif 91 <= value < 92:
        return 48 + 1 * abs(value - 91)
    elif 92 <= value < 94:
        return 49 + 0 * abs(value - 92)
    elif 94 <= value < 95:
        return 49 + 1 * abs(value - 94)
    elif 95 <= value < 97:
        return 50 + 0 * abs(value - 95)
    elif 97 <= value < 98:
        return 50 + 1 * abs(value - 97)
    else:
        return 51 + 0 * abs(value - 98)

def item_equip_speed(D_dexterity):
    if 0 <= D_dexterity < 1:
        return -0.95 + 0 * abs(D_dexterity - 0)
    elif 1 <= D_dexterity < 2:
        return -0.95 + 0.04 * abs(D_dexterity - 1)
    elif 2 <= D_dexterity < 15:
        return -0.91 + 0.07 * abs(D_dexterity - 2)
    elif 15 <= D_dexterity < 35:
        return 0 + 0.05 * abs(D_dexterity - 15)
    elif 35 <= D_dexterity < 70:
        return 1 + 0.02 * abs(D_dexterity - 35)
    else:
        return 1.7 + 0.01 * abs(D_dexterity - 70)
    
def manual_dexterity(D_dexterity):
    if 0 <= D_dexterity < 15:
        return -0.15 + 0.01 * abs(D_dexterity - 0)
    elif 15 <= D_dexterity < 23:
        return 0 + 0.03 * abs(D_dexterity - 15)
    elif 23 <= D_dexterity < 31:
        return 0.24 + 0.02 * abs(D_dexterity - 23)
    elif 31 <= D_dexterity < 37:
        return 0.4 + 0.01 * abs(D_dexterity - 31)
    elif 37 <= D_dexterity < 45:
        return 0.46 + 0.005 * abs(D_dexterity - 37)
    elif 45 <= D_dexterity < 95:
        return 0.5 + 0.001 * abs(D_dexterity - 45)
    else:
        return 0.55 + 0 * abs(D_dexterity - 95)

def magical_power_bonus(M_magicalPower):
    if 0 <= M_magicalPower < 1:
        return -0.9 + 0 * abs(M_magicalPower - 0)
    elif 1 <= M_magicalPower < 5:
        return -0.9 + 0.1 * abs(M_magicalPower - 1)
    elif 5 <= M_magicalPower < 15:
        return -0.5 + 0.05 * abs(M_magicalPower - 5)
    elif 15 <= M_magicalPower < 21:
        return 0 + 0.025 * abs(M_magicalPower - 15)
    elif 21 <= M_magicalPower < 40:
        return 0.15 + 0.02 * abs(M_magicalPower - 21)
    elif 40 <= M_magicalPower < 50:
        return 0.53 + 0.01 * abs(M_magicalPower - 40)
    else:
        return 0.63 + 0.005 * abs(M_magicalPower - 50)

def magic_resistance(W_will):
    if 0 <= W_will < 5:
        return -20 + 4 * abs(W_will - 0)
    elif 5 <= W_will < 35:
        return 0 + 3 * abs(W_will - 5)
    elif 35 <= W_will < 55:
        return 90 + 2 * abs(W_will - 35)
    elif 55 <= W_will < 66:
        return 130 + 1 * abs(W_will - 55)
    elif 66 <= W_will < 67:
        return 141 + 0 * abs(W_will - 66)
    elif 67 <= W_will < 68:
        return 141 + 1 * abs(W_will - 67)
    elif 68 <= W_will < 69:
        return 142 + 0 * abs(W_will - 68)
    elif 69 <= W_will < 70:
        return 142 + 1 * abs(W_will - 69)
    elif 70 <= W_will < 71:
        return 143 + 0 * abs(W_will - 70)
    elif 71 <= W_will < 72:
        return 143 + 1 * abs(W_will - 71)
    elif 72 <= W_will < 73:
        return 144 + 0 * abs(W_will - 72)
    elif 73 <= W_will < 74:
        return 144 + 1 * abs(W_will - 73)
    elif 74 <= W_will < 75:
        return 145 + 0 * abs(W_will - 74)
    elif 75 <= W_will < 76:
        return 145 + 1 * abs(W_will - 75)
    elif 76 <= W_will < 77:
        return 146 + 0 * abs(W_will - 76)
    elif 77 <= W_will < 78:
        return 146 + 1 * abs(W_will - 77)
    elif 78 <= W_will < 79:
        return 147 + 0 * abs(W_will - 78)
    elif 79 <= W_will < 80:
        return 147 + 1 * abs(W_will - 79)
    elif 80 <= W_will < 82:
        return 148 + 0 * abs(W_will - 80)
    elif 82 <= W_will < 83:
        return 148 + 1 * abs(W_will - 82)
    elif 83 <= W_will < 84:
        return 149 + 0 * abs(W_will - 83)
    elif 84 <= W_will < 85:
        return 149 + 1 * abs(W_will - 84)
    elif 85 <= W_will < 86:
        return 150 + 0 * abs(W_will - 85)
    elif 86 <= W_will < 87:
        return 150 + 1 * abs(W_will - 86)
    elif 87 <= W_will < 88:
        return 151 + 0 * abs(W_will - 87)
    elif 88 <= W_will < 89:
        return 151 + 1 * abs(W_will - 88)
    elif 89 <= W_will < 90:
        return 152 + 0 * abs(W_will - 89)
    elif 90 <= W_will < 91:
        return 152 + 1 * abs(W_will - 90)
    elif 91 <= W_will < 92:
        return 153 + -1 * abs(W_will - 91)
    elif 92 <= W_will < 94:
        return 152 + 1 * abs(W_will - 92)
    elif 94 <= W_will < 95:
        return 154 + 0 * abs(W_will - 94)
    elif 95 <= W_will < 96:
        return 154 + 1 * abs(W_will - 95)
    elif 96 <= W_will < 97:
        return 155 + 0 * abs(W_will - 96)
    elif 97 <= W_will < 98:
        return 155 + 1 * abs(W_will - 97)
    elif 98 <= W_will < 99:
        return 156 + 0 * abs(W_will - 98)
    else:
        return 156 + 1 * abs(W_will - 99)

def magical_damage_reduction(M_magicResistance):
    if -300 <= M_magicResistance < -15:
        return -5.95 + 0.02 * abs(M_magicResistance - (-300))
    elif -15 <= M_magicResistance < 10:
        return -0.25 + 0.01 * abs(M_magicResistance - (-15))
    elif 10 <= M_magicResistance < 19:
        return 0 + 0.005 * abs(M_magicResistance - 10)
    elif 19 <= M_magicResistance < 30:
        return 0.045 + 0.004 * abs(M_magicResistance - 19)
    elif 30 <= M_magicResistance < 40:
        return 0.089 + 0.003 * abs(M_magicResistance - 30)
    elif 40 <= M_magicResistance < 50:
        return 0.119 + 0.002 * abs(M_magicResistance - 40)
    elif 50 <= M_magicResistance < 100:
        return 0.139 + 0.001 * abs(M_magicResistance - 50)
    elif 100 <= M_magicResistance < 150:
        return 0.189 + 0.002 * abs(M_magicResistance - 100)
    elif 150 <= M_magicResistance < 250:
        return 0.289 + 0.003 * abs(M_magicResistance - 150)
    elif 250 <= M_magicResistance < 350:
        return 0.589 + 0.002 * abs(M_magicResistance - 250)
    else:
        return 0.789 + 0.001 * abs(M_magicResistance - 350)

def buff_duration(W_will):
    if 0 <= W_will < 5:
        return -0.8 + 0.1 * abs(W_will - 0)
    elif 5 <= W_will < 7:
        return -0.3 + 0.05 * abs(W_will - 5)
    elif 7 <= W_will < 11:
        return -0.2 + 0.03 * abs(W_will - 7)
    elif 11 <= W_will < 15:
        return -0.08 + 0.02 * abs(W_will - 11)
    elif 15 <= W_will < 50:
        return 0 + 0.01 * abs(W_will - 15)
    else:
        return 0.35 + 0.005 * abs(W_will - 50)

def debuff_duration(W_will):
    if 0 <= W_will < 1:
        return 4 - 1.667 * abs(W_will - 0)
    elif 1 <= W_will < 2:
        return 2.333 - 0.833 * abs(W_will - 1)
    elif 2 <= W_will < 3:
        return 1.5 - 0.5 * abs(W_will - 2)
    elif 3 <= W_will < 4:
        return 1 - 0.333 * abs(W_will - 3)
    elif 4 <= W_will < 5:
        return 0.667 - 0.238 * abs(W_will - 4)
    elif 5 <= W_will < 6:
        return 0.429 - 0.096 * abs(W_will - 5)
    elif 6 <= W_will < 7:
        return 0.333 - 0.083 * abs(W_will - 6)
    elif 7 <= W_will < 8:
        return 0.25 - 0.045 * abs(W_will - 7)
    elif 8 <= W_will < 9:
        return 0.205 - 0.042 * abs(W_will - 8)
    elif 9 <= W_will < 10:
        return 0.163 - 0.039 * abs(W_will - 9)
    elif 10 <= W_will < 11:
        return 0.124 - 0.037 * abs(W_will - 10)
    elif 11 <= W_will < 12:
        return 0.087 - 0.023 * abs(W_will - 11)
    elif 12 <= W_will < 14:
        return 0.064 - 0.022 * abs(W_will - 12)
    elif 14 <= W_will < 15:
        return 0.02 - 0.02 * abs(W_will - 14)
    elif 15 <= W_will < 17:
        return 0 - 0.01 * abs(W_will - 15)
    elif 17 <= W_will < 19:
        return -0.02 - 0.009 * abs(W_will - 17)
    elif 19 <= W_will < 20:
        return -0.038 - 0.01 * abs(W_will - 19)
    elif 20 <= W_will < 21:
        return -0.048 - 0.009 * abs(W_will - 20)
    elif 21 <= W_will < 22:
        return -0.057 - 0.008 * abs(W_will - 21)
    elif 22 <= W_will < 24:
        return -0.065 - 0.009 * abs(W_will - 22)
    elif 24 <= W_will < 29:
        return -0.083 - 0.008 * abs(W_will - 24)
    elif 29 <= W_will < 30:
        return -0.123 - 0.007 * abs(W_will - 29)
    elif 30 <= W_will < 31:
        return -0.13 - 0.008 * abs(W_will - 30)
    elif 31 <= W_will < 32:
        return -0.138 - 0.007 * abs(W_will - 31)
    elif 32 <= W_will < 33:
        return -0.145 - 0.008 * abs(W_will - 32)
    elif 33 <= W_will < 36:
        return -0.153 - 0.007 * abs(W_will - 33)
    elif 36 <= W_will < 37:
        return -0.174 - 0.006 * abs(W_will - 36)
    elif 37 <= W_will < 39:
        return -0.18 - 0.007 * abs(W_will - 37)
    elif 39 <= W_will < 41:
        return -0.194 - 0.006 * abs(W_will - 39)
    elif 41 <= W_will < 42:
        return -0.206 - 0.007 * abs(W_will - 41)
    elif 42 <= W_will < 46:
        return -0.213 - 0.006 * abs(W_will - 42)
    elif 46 <= W_will < 47:
        return -0.237 - 0.005 * abs(W_will - 46)
    elif 47 <= W_will < 49: # Not Finished
        return -0.237 - 0.005 * abs(W_will - 46)

def spell_casting_speed(Knowledge):
    if 0 <= Knowledge < 1:
        return -0.93 + 0 * abs(Knowledge - 0)
    elif 1 <= Knowledge < 19:
        return -0.93 + 0.05 * abs(Knowledge - 1)
    elif 19 <= Knowledge < 30:
        return -0.03 + 0.03 * abs(Knowledge - 19)
    elif 30 <= Knowledge < 40:
        return 0.3 + 0.04 * abs(Knowledge - 30)
    elif 40 <= Knowledge < 45:
        return 0.7 + 0.03 * abs(Knowledge - 40)
    else:
        return 0.85 + 0.02 * abs(Knowledge - 45)

def magical_interaction_speed(Will):
    if 0 <= Will < 15:
        return -0.75 + 0.05 * abs(Will - 0)
    elif 15 <= Will < 25:
        return 0 + 0.07 * abs(Will - 15)
    elif 25 <= Will < 35:
        return 0.7 + 0.05 * abs(Will - 25)
    elif 35 <= Will < 84:
        return 1.2 + 0.02 * abs(Will - 35)
    elif 84 <= Will < 85:
        return 2.18 + 0.01 * abs(Will - 84)
    elif 85 <= Will < 86:
        return 2.19 + 0.03 * abs(Will - 85)
    else:
        return 2.22 + 0.02 * abs(Will - 86)

def memory_capacity(Knowledge):
    if 0 <= Knowledge < 6:
        return 0 + 0 * abs(Knowledge - 0)
    else:
        return 0 + 1 * abs(Knowledge - 6)
    
def max_health(value):
    if 0 <= value < 10:
        return 60 + 3 * abs(value - 0)
    elif 10 <= value < 50:
        return 90 + 2 * abs(value - 10)
    elif 50 <= value < 75:
        return 170 + abs(value - 50)
    elif 75 <= value < 100:
        return 195 + 0.5 * abs(value - 75)
    else:
        return 207.5
    
def memory_recovery(Knowledge):
    if 0 <= Knowledge < 28:
        return 0.43 + 0.015 * abs(Knowledge - 0)
    elif 28 <= Knowledge < 35:
        return 0.85 + 0.05 * abs(Knowledge - 28)
    elif 35 <= Knowledge < 84:
        return 1.2 + 0.02 * abs(Knowledge - 35)
    elif 84 <= Knowledge < 85:
        return 2.18 + 0.01 * abs(Knowledge - 84)
    elif 85 <= Knowledge < 86:
        return 2.19 + 0.03 * abs(Knowledge - 85)
    else:
        return 2.22 + 0.02 * abs(Knowledge - 86)
    
def persuasiveness(Resourcefulness):
    if 0 <= Resourcefulness < 35:
        return 0 + 1 * abs(Resourcefulness - 0)
    elif 35 <= Resourcefulness < 71:
        return 35 + 0.5 * abs(Resourcefulness - 35)
    elif 71 <= Resourcefulness < 99:
        return 53 + 0.25 * abs(Resourcefulness - 71)
    else:
        return 60 + 0 * abs(Resourcefulness - 99)

def action_speed(Sum):
    if 0 <= Sum < 10:
        return -0.38 + 0.03 * abs(Sum - 0)
    elif 10 <= Sum < 13:
        return -0.08 + 0.02 * abs(Sum - 10)
    elif 13 <= Sum < 25:
        return -0.02 + 0.01 * abs(Sum - 13)
    elif 25 <= Sum < 41:
        return 0.1 + 0.015 * abs(Sum - 25)
    elif 41 <= Sum < 50:
        return 0.34 + 0.01 * abs(Sum - 41)
    else:
        return 0.43 + 0.005 * abs(Sum - 50)
    
def regular_interaction_speed(Sum):
    if 0 <= Sum < 5:
        return -0.55 + 0.05 * abs(Sum - 0)
    elif 5 <= Sum < 15:
        return -0.3 + 0.03 * abs(Sum - 5)
    elif 15 <= Sum < 25:
        return 0 + 0.07 * abs(Sum - 15)
    elif 25 <= Sum < 35:
        return 0.7 + 0.05 * abs(Sum - 25)
    elif 35 <= Sum < 84:
        return 1.2 + 0.02 * abs(Sum - 35)
    elif 84 <= Sum < 85:
        return 2.18 + 0.01 * abs(Sum - 84)
    elif 85 <= Sum < 86:
        return 2.19 + 0.03 * abs(Sum - 85)
    else:
        return 2.22 + 0.02 * abs(Sum - 86)

def physical_damage_reduction(ArmorRating):
    if -300 <= ArmorRating < -3:
        return -6.19 + 0.02 * abs(ArmorRating - (-300))
    elif -3 <= ArmorRating < 22:
        return -0.25 + 0.01 * abs(ArmorRating - (-3))
    elif 22 <= ArmorRating < 31:
        return 0 + 0.005 * abs(ArmorRating - 22)
    elif 31 <= ArmorRating < 42:
        return 0.045 + 0.004 * abs(ArmorRating - 31)
    elif 42 <= ArmorRating < 52:
        return 0.089 + 0.003 * abs(ArmorRating - 42)
    elif 52 <= ArmorRating < 62:
        return 0.119 + 0.002 * abs(ArmorRating - 52)
    elif 62 <= ArmorRating < 112:
        return 0.139 + 0.001 * abs(ArmorRating - 62)
    elif 112 <= ArmorRating < 175:
        return 0.189 + 0.002 * abs(ArmorRating - 112)
    elif 175 <= ArmorRating < 230:
        return 0.315 + 0.003 * abs(ArmorRating - 175)
    elif 230 <= ArmorRating < 317:
        return 0.48 + 0.002 * abs(ArmorRating - 230)
    elif 317 <= ArmorRating < 353:
        return 0.654 + 0.001 * abs(ArmorRating - 317)
    elif 353 <= ArmorRating < 368:
        return 0.69 + 0.0005 * abs(ArmorRating - 353)
    elif 368 <= ArmorRating < 369:
        return 0.698 + 0.0003 * abs(ArmorRating - 368)
    elif 369 <= ArmorRating < 370:
        return 0.698 + 0.0007 * abs(ArmorRating - 369)
    elif 370 <= ArmorRating < 428:
        return 0.699 + 0.0005 * abs(ArmorRating - 370)
    elif 428 <= ArmorRating < 429:
        return 0.728 + (-0.00075) * abs(ArmorRating - 428)
    elif 429 <= ArmorRating < 450:
        return 0.727 + 0.00025 * abs(ArmorRating - 429)
    else:
        return 0.732 + 0.0002 * abs(ArmorRating - 450)
