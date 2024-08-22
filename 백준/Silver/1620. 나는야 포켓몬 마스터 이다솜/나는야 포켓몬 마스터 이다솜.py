# 나는야 포켓몬 마스터 이다솜

import sys

N,M = map(int,sys.stdin.readline().split())

pokemons = dict()
pokemons_num = dict()
for i in range(1,N+1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[pokemon] = i
    pokemons_num[i] = pokemon
for i in range(M):
    search = sys.stdin.readline().rstrip()

    if search.isnumeric():
        print(pokemons_num[int(search)])
    else:
        print(pokemons[search])
