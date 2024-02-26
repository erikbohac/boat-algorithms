import random
from itertools import islice, permutations


def boat_brute_force(*seats):
    """
    Generates all possible seating arrangements and returns the best balanced ones using brute force.

    Args:
        *seats: Variable number of seats to be arranged.

    Returns:
        List: List of best balanced seating arrangements.
    """
    all_states = permutate([*seats])
    return get_best_option(all_states)


def boat_monte_carlo(*seats):
    """
    Uses Monte Carlo simulation to generate random seating arrangements and returns the best balanced ones.

    Args:
        *seats: Variable number of seats to be arranged.

    Returns:
        List: List of best balanced seating arrangements.
    """
    state = list([*seats])
    all_states = random_generate(state, int(factorial(len(state)) / 2))
    return get_best_option(all_states)


def boat_heuristic(*seats):
    """
    Generates seating arrangements using a heuristic approach and returns the best balanced ones.

    Args:
        *seats: Variable number of seats to be arranged.

    Returns:
        List: List of best balanced seating arrangements.
    """
    state = list([*seats])
    all_states = generate_perms_heuristics(state)
    return get_best_option(all_states)


def get_best_option(states: list):
    """
    Evaluates the balance of each seating arrangement and returns the best balanced ones.

    Args:
        states (list): List of seating arrangements.

    Returns:
        List: List of best balanced seating arrangements.
    """
    evaluated = [evaluate_boat(state) for state in states]
    best_options = find_best_values(states, evaluated)
    return best_options


def generate_perms_heuristics(state: list):
    """
    Generates seating arrangements using a heuristic approach.

    Args:
        state (list): Initial state of seats.

    Returns:
        List: List of generated seating arrangements.
    """
    if len(state) % 2 == 0:
        end = int(factorial(len(state)) / len(state))
        step = factorial(int(len(state) / 2))
        states = [val for val in perm_with_step(state, end, step)]
    else:
        end = int(factorial(len(state)) / 2)
        step = 2
        if len(state) == 3:
            step = 1
        states = [val for val in perm_with_step_half(state, end, step)]
    return states


def factorial(n):
    """
    Computes the factorial of a number.

    Args:
        n (int): Number to compute factorial for.

    Returns:
        int: Factorial of the input number.
    """
    if n < 0 or type(n) is not int:
        raise ValueError('Invalid data')
    if n == 0:
        return 1
    return n * factorial(n - 1)


def perm_with_step(state, end, step):
    """
    Generates permutations with a specific step.

    Args:
        state: Initial state of seats.
        end: Ending index.
        step: Step size.

    Yields:
        list: A permutation of seats.
    """
    for perm in islice(permutations(state), 0, end, step):
        yield list(perm)


def perm_with_step_half(state, end, step):
    """
    Generates permutations with a specific step for half permutations.

    Args:
        state: Initial state of seats.
        end: Ending index.
        step: Step size.

    Yields:
        list: A permutation of seats.
    """
    for perm in islice(permutations(state), 0, end, step):
        yield list(perm)


def random_generate(state: list, count: int):
    """
    Generates random seating arrangements.

    Args:
        state (list): Initial state of seats.
        count (int): Number of random arrangements to generate.

    Returns:
        List: List of generated random seating arrangements.
    """
    all_states = [state]
    for _ in range(count - 1):
        lst = state.copy()
        random.shuffle(lst)
        if lst not in all_states:
            all_states.append(lst)
    return all_states


def permutate(states: list, fixed=0):
    """
    Generates all possible seating arrangements recursively.

    Args:
        states (list): Initial state of seats.
        fixed (int): Index of the fixed seats.

    Returns:
        List: List of all possible seating arrangements.
    """
    all_states = []

    for index in range(fixed, len(states)):
        new_state = states[:fixed]
        state_copy = states[:]
        new_state.append(state_copy.pop(index))
        new_state += state_copy[fixed:]
        if fixed == len(states) - 1:
            return [new_state]
        all_states.extend(permutate(new_state, fixed=fixed + 1))

    return all_states


def evaluate_boat(state: list):
    """
    Evaluates the balance of a seating arrangement.

    Args:
        state (list): A seating arrangement.

    Returns:
        int: The difference between the sums of seats on each side.
    """
    side_length = int(len(state) / 2)

    left_values = sum(state[:side_length])
    right_values = sum(state[-side_length:])

    return left_values - right_values


def find_best_values(states: list, points: list):
    """
    Finds the best balanced seating arrangements.

    Args:
        states (list): List of seating arrangements.
        points (list): List of evaluation points for each arrangement.

    Returns:
        List: List of best balanced seating arrangements.
    """
    min_abs = min(abs(num) for num in points)
    best_points = [i for i, num in enumerate(points) if abs(num) == min_abs]

    return [states[val] for val in best_points]
