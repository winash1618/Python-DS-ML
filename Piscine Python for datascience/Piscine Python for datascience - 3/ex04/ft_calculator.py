class calculator:
    """
    A simple calculator class with static methods for vector operations.

    Methods:
        dotproduct(V1, V2):
            Calculates the dot product of two vectors.

        add_vec(V1, V2):
            Adds two vectors element-wise.

        sous_vec(V1, V2):
            Subtracts the second vector from the first vector element-wise.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the dot product result.
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print("Dot Product:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the vector addition result.
        """
        result = [x + y for x, y in zip(V1, V2)]
        print("Vector Addition: ", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first vector element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the vector subtraction result.
        """
        result = [x - y for x, y in zip(V1, V2)]
        print("Vector Subtraction: ", result)
