# -*- coding: utf-8 -*-
#
from __future__ import division

import numpy
import sympy

from ._helpers import Enr2Scheme
from ..helpers import untangle, pm, fsd, article

citation = article(
    authors=["A.H. Stroud", "D. Secrest"],
    title="Approximate integration formulas for certain spherically symmetric regions",
    journal="Math. Comp.",
    volume="17",
    year="1963",
    pages="105-135",
    url="https://doi.org/10.1090/S0025-5718-1963-0161473-0",
)


def stroud_secrest_i(n, symbolic=False):
    sqrt = sympy.sqrt if symbolic else numpy.sqrt
    pi = sympy.pi if symbolic else numpy.pi
    frac = sympy.Rational if symbolic else lambda x, y: x / y

    data = [(frac(1, n + 1), sqrt(frac(1, 2)) * _nsimplex(n, symbolic=symbolic))]
    points, weights = untangle(data)
    weights *= sqrt(pi) ** n
    return Enr2Scheme("Stroud-Secrest I", n, weights, points, 2, citation)


def stroud_secrest_ii(n, symbolic=False):
    sqrt = sympy.sqrt if symbolic else numpy.sqrt
    pi = sympy.pi if symbolic else numpy.pi
    frac = sympy.Rational if symbolic else lambda x, y: x / y

    nu = sqrt(frac(n, 2))
    data = [(frac(1, 2 * n), fsd(n, (nu, 1)))]
    points, weights = untangle(data)
    weights *= sqrt(pi) ** n
    return Enr2Scheme("Stroud-Secrest II", n, weights, points, 3, citation)


def stroud_secrest_iii(n, symbolic=False):
    sqrt = sympy.sqrt if symbolic else numpy.sqrt
    pi = sympy.pi if symbolic else numpy.pi
    frac = sympy.Rational if symbolic else lambda x, y: x / y

    nu = sqrt(frac(1, 2))
    data = [(frac(1, 2 ** n), pm(n, nu))]
    points, weights = untangle(data)
    weights *= sqrt(pi) ** n
    return Enr2Scheme("Stroud-Secrest III", n, weights, points, 3, citation)


def stroud_secrest_iv(n, symbolic=False):
    sqrt = sympy.sqrt if symbolic else numpy.sqrt
    pi = sympy.pi if symbolic else numpy.pi
    frac = sympy.Rational if symbolic else lambda x, y: x / y

    nu = sqrt(frac(n + 2, 2))
    xi = sqrt(frac(n + 2, 4))
    A = frac(2, n + 2)
    B = frac(4 - n, 2 * (n + 2) ** 2)
    C = frac(1, (n + 2) ** 2)

    data = [(A, numpy.full((1, n), 0)), (B, fsd(n, (nu, 1))), (C, fsd(n, (xi, 2)))]
    points, weights = untangle(data)
    weights *= sqrt(pi) ** n
    return Enr2Scheme("Stroud-Secrest IV", n, weights, points, 5, citation)


def _nsimplex(n, symbolic):
    # construct the regular n-simplex points with 0 center
    sqrt = sympy.sqrt if symbolic else numpy.sqrt
    frac = sympy.Rational if symbolic else lambda x, y: x / y

    return numpy.array(
        [
            [-sqrt(frac(n + 1, (n + 1 - k) * (n - k))) for k in range(i)]
            + [sqrt(frac((n + 1) * (n - i), n + 1 - i))]
            + (n - i - 1) * [0]
            for i in range(n)
        ]
        + [[-sqrt(frac(n + 1, (n + 1 - i) * (n - i))) for i in range(n)]]
    )