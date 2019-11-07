# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 10:30:57 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 11:42:22 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import vector

print ("\nFirst vec :\n")
vec = vector.Vector(3, 20)
print(vec)
print("\nSecond vec :\n")
vec2 = vector.Vector([50.0, 30.0, 10.0], 1)
print(vec2)
print("\nFirst * second :\n")
vec3 = vec2 * vec
print(vec3)
print("\nFirst + second :\n")
vec3 = vec + vec2
print(vec3)
print("\nFirst + 5 :\n")
vec3 = 5 + vec
print(vec3)
print("\nFirst - second :\n")
vec3 = vec - vec2
print(vec3)
print("\nFirst - 5 :\n")
vec3 = 5 - vec
print(vec3)
print("\nRange between 1 and 10\n")
vec3 = vector.Vector(range(1, 10))
print(vec3)
