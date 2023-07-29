from typing import List, Union


def give_bmi(height: List[Union[int, float]],
             weight: List[Union[int, float]]) -> List[Union[int, float]]:
    """Calculate the BMI (Body Mass Index) for a list of individuals.

    Args:
        height (List[Union[int, float]]): A list of heights in meters.
        weight (List[Union[int, float]]): A list of weights in kilograms.

    Returns:
        List[Union[int, float]]: A list of calculated BMIs for each individual.
    """
    return [x / (y * y) for x, y in zip(weight, height)]


def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    """Check if the BMI of individuals is above a specified limit.

    Args:
        bmi (List[Union[int, float]]): A list of BMIs for individuals.
        limit (int): The BMI limit to compare against.

    Returns:
        List[bool]: A list of boolean values indicating whether each
        BMI is above the limit.
    """
    return [x > limit for x in bmi]
