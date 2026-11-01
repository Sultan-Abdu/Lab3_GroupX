from logic import *

# Define symbols for Puzzle 0
AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")

knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

print("Puzzle 0")
for symbol in [AKnight, AKnave]:
    if model_check(knowledge0, symbol):
        print(symbol)

# Puzzle 1
AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")
BKnight = Symbol("BKnight")
BKnave = Symbol("BKnave")

knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

print("\nPuzzle 1")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge1, symbol):
        print(symbol)

# Puzzle 2
AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")
BKnight = Symbol("BKnight")
BKnave = Symbol("BKnave")

knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

print("\nPuzzle 2")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge2, symbol):
        print(symbol)

# Puzzle 3
AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")
BKnight = Symbol("BKnight")
BKnave = Symbol("BKnave")
CKnight = Symbol("CKnight")
CKnave = Symbol("CKnave")

knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(BKnight, Implication(AKnight, AKnave)),
    Implication(BKnave, Not(Implication(AKnight, AKnave))),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

print("\nPuzzle 3")
for symbol in [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]:
    if model_check(knowledge3, symbol):
        print(symbol)