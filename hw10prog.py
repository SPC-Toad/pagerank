import numpy as np

def power_step(a, v, zero_cols, alpha=0.15):
    """Performs one step of the power method

    Parameters:

    a: 2D sparce SciPy matrix
    v: 1D NumPy array
    zero_cols: 1D NumPy array
    alpha: float for the damping factor

    Returns:

    The result of performing one step of the power method, including
    reflecting boundaries and damping

    Roughly speaking, it should return the vector

    (1 - alpha)(av + (1/n)w) + (alpha/n)u

    where w and u are vectors which represent boundary reflection and
    damping, respectively

    Notes:

    zero_col has the property that zero_col[i] == 1 if column i of 'a'
    is all zeros, and zero_col[i] == 0 otherwise.

    """
    # TODO: Fill in this function and change its return value
    
    # From the Discussion:
    
    # print(a)
    # print(a.toarray())
    
    # n = len(v)
    # u = v.dot(np.ones(n)) * (alpha/n)
    
    # zero_index = np.where(zero_cols == 1)[0][0]
    
    # for i in range(n): 
    #     a[i][zero_index] = 1/n
    
    # n = len(v)
    # u = v.dot(np.ones(n)) * (alpha/n)
    
    # for i in range(n):
    #     if zero_cols[i] == 1:
    #         for j in range(n):
    #             a[j,i] = 1.0/n
                
    # return ((1 - alpha) * a.dot(v)) + u
    # return ((1 - alpha) * (a.toarray().dot(v))) + u
    
    n = len(v)
    zero_index = np.where(zero_cols == 1)[0]
    component_1 = a.dot(v)
    component_2 = 1/n * v[zero_index].sum()
    component_3 = alpha/n * v.sum()
    
    return (1-alpha) * (component_1 + component_2) + component_3
    

def print_error_log(num_iter, s):
    print(f'    | error after {num_iter} iterations: {s}')

def l1_error(u, v):
    """Computes the L1 error of two vectors

    Parameters:

    u: 1D NumPy array
    v: 1D NumPy array

    Returns:

    The sum of the absolute values of the differences of the entries
    of u and v

    """
    # TODO: Fill in this function and change its return value
    # err = 0
    # if (len(u) == len(v)) :
    #     for i in range(len(u)) :
    #         err += np.abs(u[i] - v[i])
    # return err

    return np.sum(np.abs(u - v))

def power_iter(a, start, zero_cols, tol=0.001, alpha=0.15):
    """Computes a steady state via the power method

    Parameters:

    a: 2D sparse SciPy matrix
    start: 1D NumPy matrix, starting point for the power method
    zero_cols: 1D NumPy array (see docstring for power_step)
    tol: float for error tolerance
    alpha: float for the damping factor

    Returns:

    The result of repeated applications of power_step until the
    l1_error between consecutive vectors is below the given error
    tolerance

    Notes:

    It should call print_error_log every 10 iterations, and one last
    time for the last iteration

    """
    # TODO: Fill in this function and change its return value
    v = start # Start vector
    num_iter = 0 # Initialized the num_iter to 0
    while True: # Infinite loop til break
        num_iter += 1 # Increment the count each loop.
        v_next = power_step(a, v, zero_cols, alpha) # Get the next power step value
        error = l1_error(v, v_next) # Compute the error between current vector and power_steps
        if num_iter % 10 == 0 and error >= tol: # Every 10th iteration and as long as error is less than tolerance value,
            print_error_log(num_iter, error) # print the error and its iteration
        if error < tol: # if the error is greater or equal to tol
            print_error_log(num_iter, error) # then print the current num_iter and error
            break # exit out of the while loop
        v = v_next
    return v



top_five_stanford = [281, 67, 1352, 4898, 3367] # TODO: Fill this in
top_five_berkstan = [288238, 9, 225465, 54130, 1283] # TODO: Fill this in
top_five_google = [115, 2138, 2560, 3178, 1950] # TODO: Fill this in
