import random
import typing

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run",
           "eat",
           "sleep",
           "run",
           "grab",
           "move",
           "climb",
           "swim",
           "release"]


def gen_event() -> typing.Generator[tuple, None, None]:
    pl_act_pair = (players[random.randint(0, 3)],
                   actions[random.randint(0, 8)])
    yield pl_act_pair


pl_act_pair = (players[random.randint(0, 3)], actions[random.randint(0, 8)])
print(pl_act_pair)

print("=== Game Data Stream Processor ===")

for i in range(1000):
    print(f"Event {i}: Player {next(gen_event())[0]}", end='')
    print(f" did action {next(gen_event())[1]}")

ten_events = []
for element in range(10):
    ten_events.append(next(gen_event()))

print(f"Built a list of 10 events: {ten_events}")

for element in range(len(ten_events)):
    ran_index = random.randint(0, len(ten_events) - 1)
    rm_element = ten_events.pop(ran_index)
    print(f"Got event from list: {rm_element}")
    print(f"Remains in list: {ten_events}")
