class calculator:
    #your code here
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(x * y for x, y in zip(V1, V2))
        print("Dot Product:", result)
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [x + y for x, y in zip(V1, V2)]
        print("Vector Addition: ", result)
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [x - y for x, y in zip(V1, V2)]
        print("Vector Subtraction: ", result)