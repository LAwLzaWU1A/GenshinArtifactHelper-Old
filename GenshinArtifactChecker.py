#!/usr/bin/env python3.10

import json
import sys





#Correct set prio 1 = 1000 points
#Correct set prio 2 = 900 points
#Correct mainstat = 1000 points
#Correct priority 1 substat = 100 
#Correct priority 2 substat =  75
#Correct priority 3 substat = 50
#Correct priority 4 substat = 30
#Correct priority 5 substat = 10  


# CharList[1][0] += 100     #add 100 to Albedo
# CharList[1][1] += 100     #add 100 to Aloy
# CharList[1][2] += 100     #add 100 to Amber
# CharList[1][3] += 100     #add 100 to Barbara
# CharList[1][4] += 100     #add 100 to Beidou
# CharList[1][5] += 100     #add 100 to Bennett
# CharList[1][6] += 100     #add 100 to Chongyun
# CharList[1][7] += 100     #add 100 to Diluc
# CharList[1][8] += 100     #add 100 to Diona
# CharList[1][9] += 100     #add 100 to Eula
# CharList[1][10] += 100     #add 100 to Fischl
# CharList[1][11] += 100     #add 100 to Ganyu
# CharList[1][12] += 100     #add 100 to Hu Tao
# CharList[1][13] += 100     #add 100 to Jean
# CharList[1][14] += 100     #add 100 to Kazuha
# CharList[1][15] += 100     #add 100 to Kaeya
# CharList[1][16] += 100     #add 100 to Ayaka
# CharList[1][17] += 100     #add 100 to Keqing
# CharList[1][18] += 100     #add 100 to Klee
# CharList[1][19] += 100     #add 100 to Sara
# CharList[1][20] += 100     #add 100 to Lisa
# CharList[1][21] += 100     #add 100 to Mona
# CharList[1][22] += 100     #add 100 to Ningguang
# CharList[1][23] += 100     #add 100 to Noelle
# CharList[1][24] += 100     #add 100 to Qiqi
# CharList[1][25] += 100     #add 100 to Raiden
# CharList[1][26] += 100     #add 100 to Razor
# CharList[1][27] += 100     #add 100 to Rosaria
# CharList[1][28] += 100     #add 100 to Kokomi
# CharList[1][29] += 100     #add 100 to Sayu
# CharList[1][30] += 100     #add 100 to Sucrose
# CharList[1][31] += 100     #add 100 to Tartaglia
# CharList[1][32] += 100     #add 100 to Thoma
# CharList[1][33] += 100     #add 100 to Traveler (Anemo)
# CharList[1][34] += 100     #add 100 to Traveler (Geo)
# CharList[1][35] += 100     #add 100 to Traveler (Electro)
# CharList[1][36] += 100     #add 100 to Venti
# CharList[1][37] += 100     #add 100 to Xiangling
# CharList[1][38] += 100     #add 100 to Xiao
# CharList[1][39] += 100     #add 100 to Xingqiu
# CharList[1][40] += 100     #add 100 to Xinyan
# CharList[1][41] += 100     #add 100 to Yanfei
# CharList[1][42] += 100     #add 100 to Yoimiya
# CharList[1][43] += 100     #add 100 to Zhongli
# CharList[1][44] += 100     #add 100 to Itto
# CharList[1][45] += 100     #add 100 to Gorou





def Eval_Set (CharList, artifact):            #Check the set, and add the score to the character.
    match artifact["setKey"]:          
        case "GladiatorsFinale":
            CharList[1][7] += 900     #add 900 to Diluc
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][42] += 1000     #add 1000 to Yoimiya
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 900     #add 900 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][26] += 900     #add 900 to Razor
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 900     #add 900 to Raiden
            CharList[1][31] += 900     #add 900 to Tartaglia
            CharList[1][16] += 900     #add 900 to Ayaka
            CharList[1][33] += 900     #add 900 to Traveler (Anemo)
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
        case "WanderersTroupe":
            CharList[1][41] += 900     #add 900 to Yanfei
            CharList[1][7] += 900     #add 900 to Diluc
            CharList[1][11] += 900     #add 900 to Ganyu
            CharList[1][33] += 900     #add 900 to Traveler (Anemo)
        case "Thundersoother":
            CharList[1][10] += 900     #add 900 to Fischl
            CharList[1][17] += 900     #add 900 to Keqing
        case "ThunderingFury":
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 900     #add 900 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][19] += 900     #add 900 to Sara
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 900     #add 900 to Raiden
        case "MaidenBeloved":
            CharList[1][3] += 900     #add 900 to Barbara
        case "ViridescentVenerer":
            CharList[1][30] += 1000     #add 1000 to Sucrose
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][14] += 1000     #add 1000 to Kazuha
        case "CrimsonWitchOfFlames":
            CharList[1][37] += 900     #add 900 to Xiangling
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][42] += 1000     #add 1000 to Yoimiya
        case "Lavawalker":
            CharList[1][18] += 900     #add 900 to Klee
        case "NoblesseOblige":
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][4] += 900     #add 900 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][19] += 900     #add 900 to Sara
            CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
            CharList[1][17] += 900     #add 900 to Keqing
            CharList[1][25] += 900     #add 900 to Raiden
            CharList[1][39] += 900     #add 900 to Xingqiu
            CharList[1][21] += 900     #add 900 to Mona
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 900     #add 900 to Kaeya
            CharList[1][27] += 900     #add 900 to Rosaria
            CharList[1][1] += 900     #add 900 to Aloy
            CharList[1][29] += 900     #add 900 to Sayu
            CharList[1][33] += 900     #add 900 to Traveler (Anemo)
            CharList[1][13] += 900     #add 900 to Jean
            CharList[1][36] += 900     #add 900 to Venti
            CharList[1][45] += 1000     #add 1000 to Gorou
            CharList[1][34] += 900     #add 900 to Traveler (Geo)
        case "BloodstainedChivalry":
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][26] += 900     #add 900 to Razor
            CharList[1][9] += 900     #add 900 to Eula
        case "ArchaicPetra":
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
            CharList[1][0] += 900     #add 900 to Albedo
        case "RetracingBolide":
            CharList[1][40] += 900     #add 900 to Xinyan
            CharList[1][22] += 900     #add 900 to Ningguang
            CharList[1][23] += 900     #add 900 to Noelle
            CharList[1][44] += 900     #add 900 to Itto
        case "BlizzardStrayer":
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 900     #add 900 to Kaeya
            CharList[1][27] += 900     #add 900 to Rosaria
            CharList[1][16] += 1000     #add 1000 to Ayaka
            CharList[1][1] += 1000     #add 1000 to Aloy
        case "HeartOfDepth":
            CharList[1][39] += 900     #add 900 to Xingqiu
            CharList[1][31] += 1000     #add 1000 to Tartaglia
            CharList[1][21] += 900     #add 900 to Mona
        case "TenacityOfTheMillelith":
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][43] += 1000     #add 1000 to Zhongli
        case "PaleFlame":
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][26] += 1000     #add 1000 to Razor
            CharList[1][9] += 1000     #add 1000 to Eula
        case "ShimenawasReminiscence":
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][12] += 900     #add 900 to Hu Tao
            CharList[1][42] += 1000     #add 1000 to Yoimiya
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][7] += 900     #add 900 to Diluc
            CharList[1][18] += 900     #add 900 to Klee
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 900     #add 900 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 900     #add 900 to Raiden
            CharList[1][31] += 900     #add 900 to Tartaglia
            CharList[1][16] += 900     #add 900 to Ayaka
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
        case "EmblemOfSeveredFate":
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 900     #add 900 to Bennett
            CharList[1][32] += 900     #add 900 to Thoma
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][35] += 900     #add 900 to Traveler (Electro)
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][39] += 1000     #add 1000 to Xingqiu
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][8] += 900     #add 900 to Diona
            CharList[1][6] += 900     #add 900 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
        case "HuskOfOpulentDreams":
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][0] += 1000     #add 1000 to Albedo
            CharList[1][44] += 1000     #add 1000 to Itto
        case "OceanHuedClam":
            CharList[1][3] += 1000     #add 1000 to Barbara
            CharList[1][28] += 900     #add 900 to Kokomi
            CharList[1][24] += 900     #add 900 to Qiqi

    return CharList



def Eval_FlatHP (CharList):         #Add score to characters who want flat HP and return CharList again.
    CharList[1][32] += 30     #add 30 to Thoma
    CharList[1][3] += 50     #add 50 to Barbara
    CharList[1][28] += 30     #add 30 to Kokomi
    CharList[1][8] += 50     #add 50 to Diona
    CharList[1][43] += 75     #add 75 to Zhongli

    return CharList



def Eval_HPpercent (CharList):         #Add score to characters who want HP Percent and return CharList again.
    CharList[1][32] += 75     #add 75 to Thoma
    CharList[1][3] += 100     #add 100 to Barbara
    CharList[1][12] += 50     #add 50 to Hu Tao
    CharList[1][28] += 100     #add 100 to Kokomi
    CharList[1][8] += 100     #add 100 to Diona
    CharList[1][43] += 100     #add 100 to Zhongli

    return CharList



def Eval_FlatATK (CharList):         #Add score to characters who want flat ATK and return CharList again.
    CharList[1][2] += 10     #add 10 to Amber
    CharList[1][37] += 10     #add 10 to Xiangling
    CharList[1][40] += 30     #add 30 to Xinyan
    CharList[1][41] += 10     #add 10 to Yanfei
    CharList[1][18] += 10     #add 10 to Klee
    CharList[1][42] += 10     #add 10 to Yoimiya
    CharList[1][10] += 10     #add 10 to Fischl
    CharList[1][4] += 30     #add 30 to Beidou
    CharList[1][20] += 10     #add 10 to Lisa
    CharList[1][26] += 10     #add 10 to Razor
    CharList[1][19] += 30     #add 30 to Sara
    CharList[1][35] += 30     #add 30 to Traveler (Electro)
    CharList[1][17] += 30     #add 30 to Keqing
    CharList[1][25] += 30     #add 30 to Raiden
    CharList[1][39] += 10     #add 10 to Xingqiu
    CharList[1][31] += 10     #add 10 to Tartaglia
    CharList[1][28] += 10     #add 10 to Kokomi
    CharList[1][6] += 10     #add 10 to Chongyun
    CharList[1][15] += 10     #add 10 to Kaeya
    CharList[1][27] += 10     #add 10 to Rosaria
    CharList[1][24] += 50     #add 50 to Qiqi
    CharList[1][11] += 30     #add 30 to Ganyu
    CharList[1][9] += 30     #add 30 to Eula
    CharList[1][16] += 10     #add 10 to Ayaka
    CharList[1][1] += 10     #add 10 to Aloy
    CharList[1][33] += 10     #add 10 to Traveler (Anemo)
    CharList[1][13] += 10     #add 10 to Jean
    CharList[1][36] += 10     #add 10 to Venti
    CharList[1][38] += 10     #add 10 to Xiao
    CharList[1][22] += 30     #add 30 to Ningguang
    CharList[1][34] += 30     #add 30 to Traveler (Geo)

    return CharList



def Eval_ATKpercent (CharList):         #Add score to characters who want ATK Percent and return CharList again.
    CharList[1][2] += 50     #add 50 to Amber
    CharList[1][37] += 50     #add 50 to Xiangling
    CharList[1][5] += 75     #add 75 to Bennett
    CharList[1][40] += 75     #add 75 to Xinyan
    CharList[1][41] += 75     #add 75 to Yanfei
    CharList[1][7] += 75     #add 75 to Diluc
    CharList[1][18] += 75     #add 75 to Klee
    CharList[1][12] += 30     #add 30 to Hu Tao
    CharList[1][42] += 75     #add 75 to Yoimiya
    CharList[1][10] += 75     #add 75 to Fischl
    CharList[1][4] += 75     #add 75 to Beidou
    CharList[1][20] += 50     #add 50 to Lisa
    CharList[1][26] += 75     #add 75 to Razor
    CharList[1][19] += 75     #add 75 to Sara
    CharList[1][35] += 75     #add 75 to Traveler (Electro)
    CharList[1][17] += 75     #add 75 to Keqing
    CharList[1][25] += 75     #add 75 to Raiden
    CharList[1][39] += 75     #add 75 to Xingqiu
    CharList[1][31] += 75     #add 75 to Tartaglia
    CharList[1][21] += 50     #add 50 to Mona
    CharList[1][28] += 50     #add 50 to Kokomi
    CharList[1][6] += 75     #add 75 to Chongyun
    CharList[1][15] += 50     #add 50 to Kaeya
    CharList[1][27] += 50     #add 50 to Rosaria
    CharList[1][24] += 100     #add 100 to Qiqi
    CharList[1][11] += 75     #add 75 to Ganyu
    CharList[1][9] += 50     #add 50 to Eula
    CharList[1][16] += 75     #add 75 to Ayaka
    CharList[1][1] += 75     #add 75 to Aloy
    CharList[1][30] += 75     #add 75 to Sucrose
    CharList[1][29] += 50     #add 50 to Sayu
    CharList[1][33] += 50     #add 50 to Traveler (Anemo)
    CharList[1][13] += 75     #add 75 to Jean
    CharList[1][36] += 50     #add 50 to Venti
    CharList[1][38] += 75     #add 75 to Xiao
    CharList[1][14] += 50     #add 50 to Kazuha
    CharList[1][22] += 75     #add 75 to Ningguang
    CharList[1][34] += 75     #add 75 to Traveler (Geo)
    CharList[1][0] += 50     #add 50 to Albedo
    CharList[1][44] += 30     #add 30 to Itto

    return CharList



def Eval_FlatDEF (CharList):         #Add score to characters who want flat DEF and return CharList again.
    CharList[1][0] += 10     #add 10 to Albedo
    CharList[1][44] += 10     #add 10 to Itto

    return CharList


 
def Eval_DEFpercent (CharList):         #Add score to characters who want DEF Percent and return CharList again.
    CharList[1][40] += 10     #add 10 to Xinyan
    CharList[1][23] += 50     #add 50 to Noelle
    CharList[1][45] += 75     #add 75 to Gorou
    CharList[1][0] += 75     #add 75 to Albedo
    CharList[1][44] += 75     #add 75 to Itto

    return CharList



def Eval_eleMas (CharList):         #Add score to characters who want Elemental Mastery and return CharList again.
    CharList[1][2] += 30     #add 30 to Amber
    CharList[1][37] += 30     #add 30 to Xiangling
    CharList[1][5] += 30     #add 30 to Bennett
    CharList[1][41] += 30     #add 30 to Yanfei
    CharList[1][7] += 50     #add 50 to Diluc
    CharList[1][18] += 50     #add 50 to Klee
    CharList[1][12] += 75     #add 75 to Hu Tao
    CharList[1][42] += 50     #add 50 to Yoimiya
    CharList[1][10] += 30     #add 30 to Fischl
    CharList[1][4] += 10     #add 10 to Beidou
    CharList[1][20] += 30     #add 30 to Lisa
    CharList[1][26] += 30     #add 30 to Razor
    CharList[1][17] += 50     #add 50 to Keqing
    CharList[1][25] += 10     #add 10 to Raiden
    CharList[1][39] += 30     #add 30 to Xingqiu
    CharList[1][31] += 50     #add 50 to Tartaglia
    CharList[1][21] += 30     #add 30 to Mona
    CharList[1][6] += 50     #add 50 to Chongyun
    CharList[1][15] += 30     #add 30 to Kaeya
    CharList[1][27] += 75     #add 75 to Rosaria
    CharList[1][11] += 50     #add 50 to Ganyu
    CharList[1][1] += 50     #add 50 to Aloy
    CharList[1][30] += 100     #add 100 to Sucrose
    CharList[1][29] += 75     #add 75 to Sayu
    CharList[1][33] += 100     #add 100 to Traveler (Anemo)
    CharList[1][13] += 30     #add 30 to Jean
    CharList[1][36] += 100     #add 100 to Venti
    CharList[1][38] += 30     #add 30 to Xiao
    CharList[1][14] += 100     #add 100 to Kazuha
    
    return CharList



def Eval_enerRech (CharList):         #Add score to characters who want Energy Recharge and return CharList again.
    CharList[1][2] += 100     #add 100 to Amber
    CharList[1][37] += 100     #add 100 to Xiangling
    CharList[1][5] += 50     #add 50 to Bennett
    CharList[1][40] += 50     #add 50 to Xinyan
    CharList[1][41] += 50     #add 50 to Yanfei
    CharList[1][32] += 100     #add 100 to Thoma
    CharList[1][7] += 30     #add 30 to Diluc
    CharList[1][18] += 30     #add 30 to Klee
    CharList[1][12] += 10     #add 10 to Hu Tao
    CharList[1][42] += 30     #add 30 to Yoimiya
    CharList[1][10] += 50     #add 50 to Fischl
    CharList[1][4] += 50     #add 50 to Beidou
    CharList[1][20] += 100     #add 100 to Lisa
    CharList[1][26] += 50     #add 50 to Razor
    CharList[1][19] += 50     #add 50 to Sara
    CharList[1][35] += 100     #add 100 to Traveler (Electro)
    CharList[1][17] += 10     #add 10 to Keqing
    CharList[1][25] += 50     #add 50 to Raiden
    CharList[1][39] += 50     #add 50 to Xingqiu
    CharList[1][3] += 75     #add 75 to Barbara
    CharList[1][31] += 30     #add 30 to Tartaglia
    CharList[1][21] += 75     #add 75 to Mona
    CharList[1][28] += 75     #add 75 to Kokomi
    CharList[1][8] += 75     #add 75 to Diona
    CharList[1][6] += 30     #add 30 to Chongyun
    CharList[1][15] += 100     #add 100 to Kaeya
    CharList[1][27] += 30     #add 30 to Rosaria
    CharList[1][24] += 75     #add 75 to Qiqi
    CharList[1][11] += 10     #add 10 to Ganyu
    CharList[1][9] += 75     #add 75 to Eula
    CharList[1][1] += 30     #add 30 to Aloy
    CharList[1][30] += 30     #add 30 to Sucrose
    CharList[1][29] += 100     #add 100 to Sayu
    CharList[1][33] += 75     #add 75 to Traveler (Anemo)
    CharList[1][13] += 50     #add 50 to Jean
    CharList[1][36] += 75     #add 75 to Venti
    CharList[1][38] += 50     #add 50 to Xiao
    CharList[1][14] += 75     #add 75 to Kazuha
    CharList[1][22] += 50     #add 50 to Ningguang
    CharList[1][23] += 75     #add 75 to Noelle
    CharList[1][45] += 100     #add 100 to Gorou
    CharList[1][34] += 50     #add 50 to Traveler (Geo)
    CharList[1][43] += 50     #add 50 to Zhongli
    CharList[1][0] += 30     #add 30 to Albedo
    CharList[1][44] += 50     #add 50 to Itto
    CharList[1][16] += 50     #add 50 to Ayaka

    return CharList



def Eval_critRate (CharList):         #Add score to characters who want Crit Rate and return CharList again.
    CharList[1][2] += 75     #add 75 to Amber
    CharList[1][37] += 75     #add 75 to Xiangling
    CharList[1][5] += 100     #add 100 to Bennett
    CharList[1][40] += 100     #add 100 to Xinyan
    CharList[1][41] += 100     #add 100 to Yanfei
    CharList[1][7] += 100     #add 100 to Diluc
    CharList[1][18] += 100     #add 100 to Klee
    CharList[1][12] += 100     #add 100 to Hu Tao
    CharList[1][42] += 100     #add 100 to Yoimiya
    CharList[1][10] += 100     #add 100 to Fischl
    CharList[1][4] += 100     #add 100 to Beidou
    CharList[1][20] += 75     #add 75 to Lisa
    CharList[1][26] += 100     #add 100 to Razor
    CharList[1][19] += 100     #add 100 to Sara
    CharList[1][35] += 50     #add 50 to Traveler (Electro)
    CharList[1][17] += 100     #add 100 to Keqing
    CharList[1][25] += 100     #add 100 to Raiden
    CharList[1][39] += 100     #add 100 to Xingqiu
    CharList[1][31] += 100     #add 100 to Tartaglia
    CharList[1][21] += 100     #add 100 to Mona
    CharList[1][6] += 100     #add 100 to Chongyun
    CharList[1][15] += 75     #add 75 to Kaeya
    CharList[1][27] += 100     #add 100 to Rosaria
    CharList[1][11] += 100     #add 100 to Ganyu
    CharList[1][9] += 100     #add 100 to Eula
    CharList[1][1] += 100     #add 100 to Aloy
    CharList[1][30] += 50     #add 50 to Sucrose
    CharList[1][33] += 30     #add 30 to Traveler (Anemo)
    CharList[1][13] += 100     #add 100 to Jean
    CharList[1][36] += 30     #add 30 to Venti
    CharList[1][38] += 100     #add 100 to Xiao
    CharList[1][14] += 30     #add 30 to Kazuha
    CharList[1][22] += 100     #add 100 to Ningguang
    CharList[1][23] += 100     #add 100 to Noelle
    CharList[1][34] += 100     #add 100 to Traveler (Geo)
    CharList[1][0] += 100     #add 100 to Albedo
    CharList[1][44] += 100     #add 100 to Itto
    CharList[1][32] += 50     #add 50 to Thoma
    CharList[1][45] += 50     #add 50 to Gorou
    CharList[1][16] += 30     #add 30 to Ayaka

    return CharList



def Eval_critDMG (CharList):         #Add score to characters who want Crit DMG and return CharList again.
    CharList[1][2] += 75     #add 75 to Amber
    CharList[1][37] += 75     #add 75 to Xiangling
    CharList[1][5] += 100     #add 100 to Bennett
    CharList[1][40] += 100     #add 100 to Xinyan
    CharList[1][41] += 100     #add 100 to Yanfei
    CharList[1][7] += 100     #add 100 to Diluc
    CharList[1][18] += 100     #add 100 to Klee
    CharList[1][12] += 100     #add 100 to Hu Tao
    CharList[1][42] += 100     #add 100 to Yoimiya
    CharList[1][10] += 100     #add 100 to Fischl
    CharList[1][4] += 100     #add 100 to Beidou
    CharList[1][20] += 75     #add 75 to Lisa
    CharList[1][26] += 100     #add 100 to Razor
    CharList[1][19] += 100     #add 100 to Sara
    CharList[1][35] += 50     #add 50 to Traveler (Electro)
    CharList[1][17] += 100     #add 100 to Keqing
    CharList[1][25] += 100     #add 100 to Raiden
    CharList[1][39] += 100     #add 100 to Xingqiu
    CharList[1][31] += 100     #add 100 to Tartaglia
    CharList[1][21] += 100     #add 100 to Mona
    CharList[1][6] += 100     #add 100 to Chongyun
    CharList[1][15] += 75     #add 75 to Kaeya
    CharList[1][27] += 100     #add 100 to Rosaria
    CharList[1][11] += 100     #add 100 to Ganyu
    CharList[1][9] += 100     #add 100 to Eula
    CharList[1][1] += 100     #add 100 to Aloy
    CharList[1][30] += 50     #add 50 to Sucrose
    CharList[1][33] += 30     #add 30 to Traveler (Anemo)
    CharList[1][13] += 100     #add 100 to Jean
    CharList[1][36] += 30     #add 30 to Venti
    CharList[1][38] += 100     #add 100 to Xiao
    CharList[1][14] += 30     #add 30 to Kazuha
    CharList[1][22] += 100     #add 100 to Ningguang
    CharList[1][23] += 100     #add 100 to Noelle
    CharList[1][34] += 100     #add 100 to Traveler (Geo)
    CharList[1][0] += 100     #add 100 to Albedo
    CharList[1][44] += 100     #add 100 to Itto
    CharList[1][16] += 100     #add 100 to Ayaka

    return CharList



def Eval_MainSands (CharList, artifact):         #Evaluate circlet main stat
    match artifact["mainStatKey"]:          
        case "hp_":                  
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][3] += 1000     #add 1000 to Barbara
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][43] += 1000     #add 1000 to Zhongli
        case "atk_":                  
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][42] += 1000     #add 1000 to Yoimiya
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][26] += 1000     #add 1000 to Razor
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][39] += 1000     #add 1000 to Xingqiu
            CharList[1][31] += 1000     #add 1000 to Tartaglia
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][9] += 1000     #add 1000 to Eula
            CharList[1][16] += 1000     #add 1000 to Ayaka
            CharList[1][1] += 1000     #add 1000 to Aloy
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
        case "def_":
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][0] += 1000     #add 1000 to Albedo
            CharList[1][44] += 1000     #add 1000 to Itto
        case "eleMas":
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][1] += 1000     #add 1000 to Aloy
            CharList[1][30] += 1000     #add 1000 to Sucrose
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][14] += 1000     #add 1000 to Kazuha
        case "enerRech_":
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][39] += 1000     #add 1000 to Xingqiu
            CharList[1][3] += 1000     #add 1000 to Barbara
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][14] += 1000     #add 1000 to Kazuha
            CharList[1][45] += 1000     #add 1000 to Gorou

    return CharList



def Eval_MainGoblet (CharList, artifact):         #Evaluate goblet main stat.
    match artifact["mainStatKey"]:          
        case "hp_":                  #If it's HP%
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][3] += 1000     #add 1000 to Barbara
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][43] += 1000     #add 1000 to Zhongli
        case "atk_":                  #If it's ATK%
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][13] += 1000     #add 1000 to Jean
        case "def_":  
            CharList[1][45] += 1000     #add 1000 to Gorou
        case "eleMas":  
            CharList[1][30] += 1000     #add 1000 to Sucrose
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][14] += 1000     #add 1000 to Kazuha
        case "physical_dmg_":  
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][26] += 1000     #add 1000 to Razor
            CharList[1][9] += 1000     #add 1000 to Eula
        case "anemo_dmg_":  
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][38] += 1000     #add 1000 to Xiao
        case "geo_dmg_":  
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][45] += 1000     #add 1000 to Gorou
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
            CharList[1][0] += 1000     #add 1000 to Albedo
            CharList[1][44] += 1000     #add 1000 to Itto
        case "electro_dmg_":  
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 1000     #add 1000 to Raiden
        case "hydro_dmg_":  
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][31] += 1000     #add 1000 to Tartaglia
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][28] += 1000     #add 1000 to Kokomi
        case "pyro_dmg_":  
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][42] += 1000     #add 1000 to Yoimiya
        case "cryo_dmg_":  
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][16] += 1000     #add 1000 to Ayaka
            CharList[1][1] += 1000     #add 1000 to Aloy

    return CharList



def Eval_MainCirclet (CharList, artifact):         #Evaluate circlet main stat.
    match artifact["mainStatKey"]:          
        case "hp_":                  #If it's HP%
            CharList[1][32] += 1000     #add 1000 to Thoma
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][43] += 1000     #add 1000 to Zhongli
        case "atk_":                  #If it's ATK%
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][16] += 1000     #add 1000 to Ayaka
            CharList[1][13] += 1000     #add 1000 to Jean
        case "def_":                  #If it's DEF%
            CharList[1][45] += 1000     #add 1000 to Gorou
            CharList[1][0] += 1000     #add 1000 to Albedo
        case "eleMas":                  #If it's Elemental Mastery
            CharList[1][30] += 1000     #add 1000 to Sucrose
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][14] += 1000     #add 1000 to Kazuha
        case "critRate_":                  #If it's Crit Rate
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][42] += 1000     #add 1000 to Yoimiya
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][26] += 1000     #add 1000 to Razor
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][39] += 1000     #add 1000 to Xingqiu
            CharList[1][31] += 1000     #add 1000 to Tartaglia
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][9] += 1000     #add 1000 to Eula
            CharList[1][1] += 1000     #add 1000 to Aloy
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][45] += 1000     #add 1000 to Gorou
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
            CharList[1][0] += 1000     #add 1000 to Albedo
            CharList[1][44] += 1000     #add 1000 to Itto
        case "critDMG_":                  #If it's Crit DMG
            CharList[1][2] += 1000     #add 1000 to Amber
            CharList[1][37] += 1000     #add 1000 to Xiangling
            CharList[1][5] += 1000     #add 1000 to Bennett
            CharList[1][40] += 1000     #add 1000 to Xinyan
            CharList[1][41] += 1000     #add 1000 to Yanfei
            CharList[1][7] += 1000     #add 1000 to Diluc
            CharList[1][18] += 1000     #add 1000 to Klee
            CharList[1][12] += 1000     #add 1000 to Hu Tao
            CharList[1][42] += 1000     #add 1000 to Yoimiya
            CharList[1][10] += 1000     #add 1000 to Fischl
            CharList[1][4] += 1000     #add 1000 to Beidou
            CharList[1][20] += 1000     #add 1000 to Lisa
            CharList[1][26] += 1000     #add 1000 to Razor
            CharList[1][19] += 1000     #add 1000 to Sara
            CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
            CharList[1][17] += 1000     #add 1000 to Keqing
            CharList[1][25] += 1000     #add 1000 to Raiden
            CharList[1][39] += 1000     #add 1000 to Xingqiu
            CharList[1][31] += 1000     #add 1000 to Tartaglia
            CharList[1][21] += 1000     #add 1000 to Mona
            CharList[1][6] += 1000     #add 1000 to Chongyun
            CharList[1][15] += 1000     #add 1000 to Kaeya
            CharList[1][27] += 1000     #add 1000 to Rosaria
            CharList[1][11] += 1000     #add 1000 to Ganyu
            CharList[1][9] += 1000     #add 1000 to Eula
            CharList[1][16] += 1000     #add 1000 to Ayaka
            CharList[1][1] += 1000     #add 1000 to Aloy
            CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
            CharList[1][13] += 1000     #add 1000 to Jean
            CharList[1][36] += 1000     #add 1000 to Venti
            CharList[1][38] += 1000     #add 1000 to Xiao
            CharList[1][22] += 1000     #add 1000 to Ningguang
            CharList[1][23] += 1000     #add 1000 to Noelle
            CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
            CharList[1][0] += 1000     #add 1000 to Albedo
            CharList[1][44] += 1000     #add 1000 to Itto
        case "heal_":                  #If it's healing bonus
            CharList[1][3] += 1000     #add 1000 to Barbara
            CharList[1][28] += 1000     #add 1000 to Kokomi
            CharList[1][8] += 1000     #add 1000 to Diona
            CharList[1][24] += 1000     #add 1000 to Qiqi
            CharList[1][29] += 1000     #add 1000 to Sayu
            CharList[1][45] += 1000     #add 1000 to Gorou

    return CharList



def Eval_Add1000toAll (CharList):         #Special for flower and feather. Add 1000 to everyone.
    CharList[1][0] += 1000     #add 1000 to Albedo
    CharList[1][1] += 1000     #add 1000 to Aloy
    CharList[1][2] += 1000     #add 1000 to Amber
    CharList[1][3] += 1000     #add 1000 to Barbara
    CharList[1][4] += 1000     #add 1000 to Beidou
    CharList[1][5] += 1000     #add 1000 to Bennett
    CharList[1][6] += 1000     #add 1000 to Chongyun
    CharList[1][7] += 1000     #add 1000 to Diluc
    CharList[1][8] += 1000     #add 1000 to Diona
    CharList[1][9] += 1000     #add 1000 to Eula
    CharList[1][10] += 1000     #add 1000 to Fischl
    CharList[1][11] += 1000     #add 1000 to Ganyu
    CharList[1][12] += 1000     #add 1000 to Hu Tao
    CharList[1][13] += 1000     #add 1000 to Jean
    CharList[1][14] += 1000     #add 1000 to Kazuha
    CharList[1][15] += 1000     #add 1000 to Kaeya
    CharList[1][16] += 1000     #add 1000 to Ayaka
    CharList[1][17] += 1000     #add 1000 to Keqing
    CharList[1][18] += 1000     #add 1000 to Klee
    CharList[1][19] += 1000     #add 1000 to Sara
    CharList[1][20] += 1000     #add 1000 to Lisa
    CharList[1][21] += 1000     #add 1000 to Mona
    CharList[1][22] += 1000     #add 1000 to Ningguang
    CharList[1][23] += 1000     #add 1000 to Noelle
    CharList[1][24] += 1000     #add 1000 to Qiqi
    CharList[1][25] += 1000     #add 1000 to Raiden
    CharList[1][26] += 1000     #add 1000 to Razor
    CharList[1][27] += 1000     #add 1000 to Rosaria
    CharList[1][28] += 1000     #add 1000 to Kokomi
    CharList[1][29] += 1000     #add 1000 to Sayu
    CharList[1][30] += 1000     #add 1000 to Sucrose
    CharList[1][31] += 1000     #add 1000 to Tartaglia
    CharList[1][32] += 1000     #add 1000 to Thoma
    CharList[1][33] += 1000     #add 1000 to Traveler (Anemo)
    CharList[1][34] += 1000     #add 1000 to Traveler (Geo)
    CharList[1][35] += 1000     #add 1000 to Traveler (Electro)
    CharList[1][36] += 1000     #add 1000 to Venti
    CharList[1][37] += 1000     #add 1000 to Xiangling
    CharList[1][38] += 1000     #add 1000 to Xiao
    CharList[1][39] += 1000     #add 1000 to Xingqiu
    CharList[1][40] += 1000     #add 1000 to Xinyan
    CharList[1][41] += 1000     #add 1000 to Yanfei
    CharList[1][42] += 1000     #add 1000 to Yoimiya
    CharList[1][43] += 1000     #add 1000 to Zhongli
    CharList[1][44] += 1000     #add 1000 to Itto
    CharList[1][45] += 1000     #add 1000 to Gorou

    return CharList






def CalcCharScore(artifact):

    #List of characters and the artifacts score for that character (starts at 0).
    CharList = [
        "Albedo (Off-Field DPS)", "Aloy (Burst Support)", "Amber (Support)", "Barbara (Support)", "Beidou (Off-Field DPS)",
        "Bennett (Burst Support)", "Chongyun (Burst Support)", "Diluc (DPS)", "Diona (Support)", "Eula (DPS)", "Fischl (Off-Field DPS)",
        "Ganyu (Melt DPS)", "Hu Tao (DPS)", "Jean (Burst Support)", "Kazuha (EM Build)", "Kaeya (Burst Support)", "Ayaka (DPS)",
        "Keqing (Electro DPS)", "Klee (DPS)", "Sara (Burst Support)", "Lisa (Off-Field DPS)", "Mona (Nuke)", "Ningguang (DPS)", "Noelle (DPS)",
        "Qiqi (Support)", "Raiden (Electro DPS)", "Razor (DPS)", "Rosaria (Burst Support)", "Kokomi (Support)", "Sayu (Support)",
        "Sucrose (EM Build)", "Tartaglia (DPS)", "Thoma (Support)", "Traveler (Anemo - DPS)", "Traveler (Geo - DPS)", "Traveler (Electro - Support)",
        "Venti (Off-Field DPS)", "Xiangling (Off-Field DPS)", "Xiao (DPS)", "Xingqiu (Off-Field DPS)", "Xinyan (DPS)", "Yanfei (DPS)",
        "Yoimiya (DPS)", "Zhongli (Shield Support)", "Itto (DPS)", "Gorou (Support)"
        ],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    CharList = Eval_Set(CharList, artifact)    #Evaluate and score the set. Gives 1000 points if it's the best set. 900 if it's the second best.


    if artifact["slotKey"] == "sands":            #Evaluate and score sands main stat.
        CharList = Eval_MainSands(CharList, artifact)

    if artifact["slotKey"] == "goblet":            #Evaluate and score goblet main stat.
        CharList = Eval_MainGoblet(CharList, artifact)

    if artifact["slotKey"] == "circlet":            #Evaluate and score circlet main stat.
        CharList = Eval_MainCirclet(CharList, artifact)

    if artifact["slotKey"] == "flower" or artifact["slotKey"] == "plume":         #Add 1000 to everyone if it's a flower or plume since those are always the same stat.
        CharList = Eval_Add1000toAll(CharList)



#Evaluate all the substats

    for i in range(len(artifact["substats"])) :    #Go through all substats
        if artifact["substats"][i]["key"] == "hp":      #search all substats for flat HP
            CharList = Eval_FlatHP(CharList)

        if artifact["substats"][i]["key"] == "hp_":    #search all substats for HP percent
            CharList = Eval_HPpercent(CharList)
    
        if artifact["substats"][i]["key"] == "atk":   #search all substats for flat ATK
            CharList = Eval_FlatATK(CharList)

        if artifact["substats"][i]["key"] == "atk_":   #search all substats for ATK percent
            CharList = Eval_ATKpercent(CharList)
    
        if artifact["substats"][i]["key"] == "def":   #search all substats for flat DEF
            CharList = Eval_FlatDEF(CharList)
    
        if artifact["substats"][i]["key"] == "def_":   #search all substats for DEF percent
            CharList = Eval_DEFpercent(CharList)
    
        if artifact["substats"][i]["key"] == "eleMas":   #search all substats for Elemental Mastery
            CharList = Eval_eleMas(CharList)

        if artifact["substats"][i]["key"] == "enerRech_":   #search all substats for Energy Recharge
            CharList = Eval_enerRech(CharList)

        if artifact["substats"][i]["key"] == "critRate_":   #search all substats for Crit Rate
            CharList = Eval_critRate(CharList)

        if artifact["substats"][i]["key"] == "critDMG_":   #search all substats for Crit DMG
            CharList = Eval_critDMG(CharList)




    GoodForAnyone = False


    for i in range(len(CharList[0])):   #Go through the entire list of characters.
        if CharList[1][i] >= 2155:        #If the score of an artifact is over 2155, print it.
            GoodForAnyone = True


    if GoodForAnyone == True:       #Print the artifact that's good.
        print("", file=open("ArtifactResults.txt", "a"))
        print("Set:", artifact["setKey"],"-", "Rarity:", artifact["rarity"], "-", "Level:", artifact["level"], "-", "Slot:", artifact["slotKey"], file=open("ArtifactResults.txt", "a"))
        print("Main Stat:", artifact["mainStatKey"].replace("_", "%"), file=open("ArtifactResults.txt", "a"))
        for i in range(len(artifact["substats"])):          #Loop and print all substats
            print("Substat", i+1, ":", artifact["substats"][i]["key"].replace("_", "%"), file=open("ArtifactResults.txt", "a"))
        print("The above artifact is good for:", file=open("ArtifactResults.txt", "a"))
        for i in range(len(CharList[0])):       #print all the character's it's good for
            if CharList[1][i] >= 2155: 
                print(CharList[0][i], "Score:", CharList[1][i], file=open("ArtifactResults.txt", "a"))
    else:
        print("", file=open("ArtifactResults.txt", "a"))
        print("Set:", artifact["setKey"],"-", "Rarity:", artifact["rarity"], "-", "Level:", artifact["level"], "-", "Slot:", artifact["slotKey"], file=open("ArtifactResults.txt", "a"))
        print("Main Stat:", artifact["mainStatKey"].replace("_", "%"), file=open("ArtifactResults.txt", "a"))
        for i in range(len(artifact["substats"])):          #Loop and print all substats
            print("Substat",  i+1, ":", artifact["substats"][i]["key"].replace("_", "%"), file=open("ArtifactResults.txt", "a"))
        print("The above artifact is crap", file=open("ArtifactResults.txt", "a"))











if len(sys.argv) < 2:          #Error handling, if a user doesn't specify their artifact list
    print("Please specify the file as an argument")
    sys.exit()


try:                                    #Error handling, if a user specifies an incorrect file
    file = open(sys.argv[1])
except FileNotFoundError:               #Error handling, if a user specifies an incorrect file
    print("File not found, please make sure the file exists")
    sys.exit()






file = open(sys.argv[1])       #Open the file and load it to the varaible "file"
artifact_data = json.load(file)     #take the data from file, load it into the varable artifact_data as a directory





#print("Found", len(artifact_data["artifacts"]), "artifacts")      #Check and print how many artifacts are in the JSON file. Good for debugging

for i in artifact_data["artifacts"]:    #Go through all artifacts
    if i["rarity"] == 5:
        CalcCharScore(i)




