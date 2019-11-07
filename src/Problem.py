import src.Cube as Cube
from numpy import nditer, full


class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def is_goal2(self, state):
        """This function checks if a certain state of the cube is solved.

        Returns:
            True/False -- Boolean that represents if each of the faces is diferent from each one
        """
        number_list = []

        if not self.__check_correctness_face(state.back, number_list):
            return False
        if not self.__check_correctness_face(state.down, number_list):
            return False
        if not self.__check_correctness_face(state.front, number_list):
            return False
        if not self.__check_correctness_face(state.left, number_list):
            return False
        if not self.__check_correctness_face(state.right, number_list):
            return False
        if not self.__check_correctness_face(state.up, number_list):
            return False

        return number_list.sort() == [0, 1, 2, 3, 4, 5]

    def __check_correctness_face(self, face, number_list):
        """This function checks the correctness of a certain face of the state(cube)

        Returns:
            True/False -- Boolean that represents if all the numbers of the face are equal to the first one
        """
        first_number_face = face[0, 0]
        for number in nditer(face):
            if first_number_face != number:
                return False

        number_list.append(first_number_face)
        return True

    def is_goal(self, state):
        """This function checks if a certain state of the cube is solved. To do that, a solved cube
        with the right dimensions is created and their md5 are compared.

        Returns:
            True/False -- Boolean that represents if the Rubik's cube positions are in the right way
        """
        cube_faces = {}
        for i in range(0, 6):
            cube_faces[i] = full(state.left.shape, i, dtype="int8")

        solved_cube = Cube.Cube(None, cube_faces)

        return state.create_md5() == solved_cube.create_md5()


if __name__ == "__main__":
    cube = Cube.Cube("src/resources/cube.json")
    problem = Problem(cube)
    print(problem.is_goal(cube))
