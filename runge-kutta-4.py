def runge_kutta_4(fun, a0, v0, t0, T, args):
    """
    Runge Kutta 4 (5)
    :param fun: Diferential Equation Functions with acceleration (a) as result
    :param a0: Initial acceleration
    :param v0: Initial speed
    :param t0: Initial time
    :param T: Period
    :param args: Any argument you need for your equation
    :return: Estimated acceleration multiplied by period T
    """
    A = fun(v0, t0, args)
    B = fun(v0 + ((T / 2) * A), t0 + (T / 2), args)
    C = fun(v0 + ((T / 2) * B), t0 + (T / 2), args)
    D = fun(v0 + (T * C), t0 + T, args)
    return (a0 + ((T / 6) * (A + (2 * B) + (2 * C) + D))) * T
