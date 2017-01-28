# TODO:
# Refactor to make it more Pythonic
# Use functions directly instead of utils
# Use assign_value to visualize
# Optimize naked_twins to get rid of duplicated cases

import utils

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    
    for box in values:
        if len(values[box])==2:
            for peer in utils.peers[box]:
                if values[peer]==values[box]: # found a naked twin
                    affected_peers = utils.peers[box] & utils.peers[peer]
                    for ap in affected_peers:
                        values[ap] = values[ap].replace(values[box][0],'').replace(values[box][1],'')

    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return dict(zip(utils.boxes,map(lambda x: ('123456789' if x=='.' else x), [char for char in grid])))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    utils.display(values)

def eliminate(values):
    return utils.eliminate(values)

def only_choice(values):
    return utils.only_choice(values)

def reduce_puzzle(values):
    return utils.reduce_puzzle(values)

def search(values):
    return utils.search(values)

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    print(utils.diagonal_units)
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
