from enum import Enum

ElementTypes = Enum("ElementTypes", "Fire Water Wood Dark Light NoElement")
ElementIds = {
    0 : ElementTypes.Fire,
    1 : ElementTypes.Water,
    2 : ElementTypes.Wood,
    3 : ElementTypes.Dark,
    4 : ElementTypes.Light,
    None : ElementTypes.NoElement,
}


TypeTypes = Enum("TypeTypes", "Dragon Balanced Physical Healer Attacker God EvoMaterial EnhanceMaterial Devil AwokenSkillMaterial Machine Protected NoType")
TypeIds = {
    1 : TypeTypes.Dragon,
    2 : TypeTypes.Balanced,
    3 : TypeTypes.Physical,
    4 : TypeTypes.Healer,
    5 : TypeTypes.Attacker,
    6 : TypeTypes.God,
    7 : TypeTypes.EvoMaterial,
    8 : TypeTypes.EnhanceMaterial,
    9 : TypeTypes.Devil,
    11 : TypeTypes.AwokenSkillMaterial,
    12 : TypeTypes.Machine,
    13 : TypeTypes.Protected,
    None : TypeTypes.NoType,
}


XpCurveTypes = Enum("XpCurveTypes", "One OnePointFive Two TwoPointFive Three ThreePointFive Four FourPointFive Five FivePointFive Six SixPointFive Seven SevenPointFive Eight EightPointFive NoCurve")
XpCurveIds = { 
    1000000 : XpCurveTypes.One,
    1500000 : XpCurveTypes.OnePointFive,
    2000000 : XpCurveTypes.Two,
    2500000 : XpCurveTypes.TwoPointFive,
    3000000 : XpCurveTypes.Three,
    3500000 : XpCurveTypes.ThreePointFive,
    4000000 : XpCurveTypes.Four,
    4500000 : XpCurveTypes.FourPointFive,
    5000000 : XpCurveTypes.Five,
    5500000 : XpCurveTypes.FivePointFive,
    6000000 : XpCurveTypes.Six,
    6500000 : XpCurveTypes.SixPointFive,
    7000000 : XpCurveTypes.Seven,
    7500000 : XpCurveTypes.SevenPointFive,
    8000000 : XpCurveTypes.Eight,
    8500000 : XpCurveTypes.EightPointFive,
    None : XpCurveTypes.NoCurve,
}


class ConstraintTypes(Enum):
   Element="El"
   Type = "Ty"
   NoneSet = "Nil"

ConstraintNoneTypes = Enum("ConstraintNoneTypes", "NoConstraint")
ConstraintNoneIds = {
    None : ConstraintNoneTypes.NoConstraint
}

ConstraintIds = {
    'elem' : ConstraintTypes.Element,
    'type' : ConstraintTypes.Type,
    None : ConstraintTypes.NoneSet,
}
ConstraintMap = {
    ConstraintTypes.Element : ElementIds,
    ConstraintTypes.Type : TypeIds,
    ConstraintTypes.NoneSet : ConstraintNoneIds,
}


class FoodTypes(Enum):
    Food = "Food"
    Monster = "Mstr"

FoodIds = {
    "food" : FoodTypes.Food,
    "monsters" : FoodTypes.Monster,
}

AttributeTypes = Enum("AttributeTypes", "Hp Atk Rcv")

AttributePlusMap = {
    AttributeTypes.Hp : 10,
    AttributeTypes.Atk : 5,
    AttributeTypes.Rcv : 3,
}

EventCountryTypes = Enum("EventCountryTypes", "Jp Us")
EventCountryIds = {
    1 : EventCountryTypes.Jp,
    2 : EventCountryTypes.Us,
}
