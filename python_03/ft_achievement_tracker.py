import random

achievements = ["Crafting Genius",
                "Strategist",
                "World Saviour",
                "Speed Runner",
                "Survivour",
                "Master Explorer",
                "Treasure Hunter",
                "Unstoppable",
                "First Steps",
                "Collector Supreme",
                "Untouchable",
                "Sharp Mind",
                "Boss Slayer"]


def gen_player_achievements() -> set:
    rand_achs = set(random.sample(achievements, random.randint(0, 13)))
    return rand_achs


p_alice = gen_player_achievements()
p_bob = gen_player_achievements()
p_charlie = gen_player_achievements()
p_dylan = gen_player_achievements()

print(f"All distinct achievements: {achievements}\n")

common_achs = p_alice.intersection(p_bob, p_charlie, p_dylan)
print(f"Common achievements: {common_achs}\n")


print(f"Only Alice has {(p_alice.difference(p_bob, p_charlie, p_dylan))}")
print(f"Only Bob has {(p_bob.difference(p_alice, p_charlie, p_dylan))}")
print(f"Only Charlie has {(p_charlie.difference(p_bob, p_alice, p_dylan))}")
print(f"Only Dylan has {(p_dylan.difference(p_bob, p_charlie, p_alice))}\n")

print(f"Alice is missing: {set(achievements).difference(p_alice)}")
print(f"Bob is missing: {set(achievements).difference(p_bob)}")
print(f"Charlie is missing: {set(achievements).difference(p_charlie)}")
print(f"Dylan is missing: {set(achievements).difference(p_dylan)}")
