#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# The first objective of this program is to calculate the total
# population of all the population values in the census.txt file
#----------------------------------------------------------------------------
# Data Generation Template
#----------------------------------------------------------------------------
# California 38332521
# Texas 26448193
# New-York 19651127
# Florida 19552860
# Illinois 12882135
# Pennsylvania 12773801
# Ohio 11570808
# Georgia 9992167
# Michigan 9895622
# North-Carolina 9848060
# New-Jersey 8899339
# Virginia 8260405
# Washington 6971406
# Massachusetts 6692824
# Arizona 6626624
# Indiana 6570902
# Tennessee 6495978
# Missouri 6044171
# Maryland 5928814
# Wisconsin 5742713
# Minnesota 5420380
# Colorado 5268367
# Alabama 4833722
# South-Carolina 4774839
# Louisiana 4625470
# Kentucky 4395295
# Oregon 3930065
# Oklahoma 3850568
# Connecticut 3596080
# Iowa 3090416
# Mississippi 2991207
# Arkansas 2959373
# Utah 2900872
# Kansas 2893957
# Nevada 2790136
# New-Mexico 2085287
# Nebraska 1868516
# West-Virginia 1854304
# Idaho 1612136
# Hawaii 1404054
# Maine 1328302
# New-Hampshire 1323459
# Rhode-Island 1051511
# Montana 1015165
# Delaware 925749
# South-Dakota 844877
# Alaska 735132
# North-Dakota 723393
# District-of-Columbia 646449
# Vermont 626630
# Wyoming 582658
#----------------------------------------------------------------------------

census_file = open("census.txt", "r")
total = 0

for one_line in census_file:
    values = one_line.split()
    total += int(values[1])

print("Total population: ", total)
print("-----------------------\n")
census_file.close()

#----------------------------------------------------------------------------
# The second objective is to add the population of each state together in
# succession so that the total population is written into the summary.txt
# file. There should be 51 entries in the summary.txt file.
#----------------------------------------------------------------------------

census_file = open("census.txt", "r")
summary_file = open("summary.txt", "w")
input_line = census_file.readline()
cumulative_population = 0

while input_line:
    values = input_line.split()
    cumulative_population += int(values[1])
    summary_file.write("Population so far: " + str(cumulative_population) + "\n")
    input_line = census_file.readline()

print("See summary.txt file.")
print("------------------------\n")
census_file.close()
summary_file.close()

#----------------------------------------------------------------------------
# The third objective is to read the mystery.txt file and produce whatever
# the data located within the mystery.txt file entails.
#----------------------------------------------------------------------------
# Data Generation Template
#----------------------------------------------------------------------------
##UP
##-218 185
##DOWN
##-240 189
##-246 188
##-248 183
##-246 178
##-244 175
##-240 170
##-235 166
##-229 163
##-220 158
##-208 156
##-203 153
##-194 148
##-187 141
##-179 133
##-171 119
##-166 106
##-163 87
##-161 66
##-162 52
##-164 44
##-167 28
##-171 6
##-172 -15
##-171 -30
##-165 -46
##-156 -60
##-152 -67
##-152 -68
##UP
##-134 -61
##DOWN
##-145 -66
##-152 -78
##-152 -94
##-157 -109
##-157 -118
##-151 -128
##-146 -135
##-146 -136
##UP
##-97 -134
##DOWN
##-98 -138
##-97 -143
##-96 -157
##-96 -169
##-98 -183
##-104 -194
##-110 -203
##-114 -211
##-117 -220
##-120 -233
##-122 -243
##-123 -247
##-157 -248
##-157 -240
##-154 -234
##-154 -230
##-153 -229
##-149 -226
##-146 -223
##-145 -219
##-143 -214
##-142 -210
##-141 -203
##-139 -199
##-136 -192
##-132 -184
##-130 -179
##-132 -171
##-133 -162
##-134 -153
##-138 -145
##-143 -137
##-143 -132
##-142 -124
##-138 -112
##-134 -104
##-132 -102
##UP
##-97 -155
##DOWN
##-92 -151
##-91 -147
##-89 -142
##-89 -135
##-90 -129
##-90 -128
##UP
##-94 -170
##DOWN
##-83 -171
##-68 -174
##-47 -177
##-30 -172
##-15 -171
##-11 -170
##UP
##12 -96
##DOWN
##9 -109
##9 -127
##7 -140
##5 -157
##9 -164
##22 -176
##37 -204
##40 -209
##49 -220
##55 -229
##57 -235
##57 -238
##50 -239
##49 -241
##51 -248
##53 -249
##63 -245
##70 -243
##57 -249
##62 -250
##71 -250
##75 -250
##81 -250
##86 -248
##86 -242
##84 -232
##85 -226
##81 -221
##77 -211
##73 -205
##67 -196
##62 -187
##58 -180
##51 -171
##47 -164
##46 -153
##50 -141
##53 -130
##54 -124
##57 -112
##56 -102
##55 -98
##UP
##48 -164
##DOWN
##54 -158
##60 -146
##64 -136
##64 -131
##UP
##5 -152
##DOWN
##1 -150
##-4 -145
##-8 -138
##-14 -128
##-19 -119
##-17 -124
##UP
##21 -177
##DOWN
##14 -176
##7 -174
##-6 -174
##-14 -170
##-19 -166
##-20 -164
##UP
##-8 -173
##DOWN
##-8 -180
##-5 -189
##-4 -201
##-2 -211
##-1 -220
##-2 -231
##-5 -238
##-8 -241
##-9 -244
##-7 -249
##6 -247
##9 -248
##16 -247
##21 -246
##24 -241
##27 -234
##27 -226
##27 -219
##27 -209
##27 -202
##28 -193
##28 -188
##28 -184
##UP
##-60 -177
##DOWN
##-59 -186
##-57 -199
##-56 -211
##-59 -225
##-61 -233
##-65 -243
##-66 -245
##-73 -246
##-81 -246
##-84 -246
##-91 -245
##-91 -244
##-88 -231
##-87 -225
##-85 -218
##-85 -211
##-85 -203
##-85 -193
##-88 -185
##-89 -180
##-91 -175
##-92 -172
##-93 -170
##UP
##-154 -93
##DOWN
##-157 -87
##-162 -74
##-168 -66
##-172 -57
##-175 -49
##-178 -38
##-178 -26
##-178 -12
##-177 4
##-175 17
##-172 27
##-168 36
##-161 48
##-161 50
##UP
##-217 178
##DOWN
##-217 178
##-217 177
##-215 176
##-214 175
##-220 177
##-223 178
##-223 178
##-222 178
##UP
##-248 185
##DOWN
##-245 184
##-240 182
##-237 181
##-234 179
##-231 177
##-229 176
##-228 175
##-226 174
##-224 173
##-223 173
##-220 172
##-217 172
##-216 171
##-214 170
##-214 169
##UP
##-218 186
##DOWN
##-195 173
##-183 165
##-175 159
##-164 151
##-158 145
##-152 139
##-145 128
##-143 122
##-139 112
##-138 105
##-134 95
##-131 88
##-129 78
##-126 67
##-125 62
##-125 54
##-124 44
##-125 38
##-126 30
##-125 27
##-125 8
##-126 5
##-125 -9
##-122 -15
##-115 -25
##-109 -32
##-103 -39
##-95 -42
##-84 -45
##-72 -47
##-56 -48
##-41 -47
##-31 -46
##-18 -45
##-1 -44
##9 -43
##34 -45
##50 -52
##67 -61
##83 -68
##95 -80
##112 -97
##142 -115
##180 -132
##200 -146
##227 -159
##259 -175
##289 -185
##317 -189
##349 -190
##375 -191
##385 -192
##382 -196
##366 -199
##352 -204
##343 -204
##330 -205
##315 -209
##296 -212
##276 -214
##252 -208
##237 -202
##218 -197
##202 -193
##184 -187
##164 -179
##147 -173
##128 -168
##116 -164
##102 -160
##88 -158
##78 -159
##69 -162
##57 -164
##56 -165
##51 -165
##UP
##68 -144
##DOWN
##83 -143
##96 -141
##109 -139
##119 -146
##141 -150
##161 -155
##181 -163
##195 -169
##208 -179
##223 -187
##241 -191
##247 -193
##249 -194
##UP
##-6 -141
##DOWN
##-15 -146
##-29 -150
##-42 -154
##-51 -153
##-60 -152
##-60 -152
##UP
##-90 -134
##DOWN
##-85 -131
##-79 -128
##-78 -123
##-80 -115
##-82 -106
##-80 -101
##-76 -101
##UP
##-81 -132
##DOWN
##-76 -130
##-71 -126
##-72 -124
##UP
##43 -118
##DOWN
##44 -125
##47 -135
##41 -156
##37 -160
##40 -166
##47 -171
##47 -171
##UP
##-106 -153
##DOWN
##-107 -167
##-106 -178
##-109 -192
##-114 -198
##-116 -201
#----------------------------------------------------------------------------

import turtle

def process_command(command, some_turtle):
    if command == "UP\n":
        some_turtle.up()
    elif command == "DOWN\n":
        some_turtle.down()
    else:
        coordinates = command.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        some_turtle.goto(x, y)

def main(file_name):
    turtle_commands = open(file_name, "r")
    picture_turtle = turtle.Turtle()
    for command in turtle_commands:
        process_command(command, picture_turtle)
    turtle_commands.close()

main("mystery.txt")

#----------------------------------------------------------------------------

def total_population_01(states_information):
    result = 0
    for state_information in states_information:
        result += state_information[1]
    return result

def water_population(states_information):
    result = 0
    for state_information in states_information:
        if state_information[2] == "Water":
            result += state_information[1]
    return result

def total_population_02(states_information):
    result = 0
    for index in range(len(states_information)):
        result += states_information[index][1]
    return result

populations = [["California", 38332521, "Water"], ["Texas", 26448193, "Water"],
               ["New York", 19651127, "Water"], ["Florida", 19552860, "Water"],
               ["Illinois", 12882135, "Land"], ["Pennsylvania", 12773801, "Land"],
               ["Ohio", 11570808, "Land"], ["Georgia", 9992167, "Water"],
               ["Michigan", 9895622, "Land"], ["North Carolina", 9848060, "Water"]]

print("The total population for states surrounded by water =", water_population(populations))
