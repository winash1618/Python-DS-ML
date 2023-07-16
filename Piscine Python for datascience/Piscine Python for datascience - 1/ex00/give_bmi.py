from typing import List, Union

def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    return [x /(y * y) for x, y in zip(weight, height)]

def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    return [x > limit for x in bmi]
