# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import check_degree, integrate_monomial_over_enr2


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.e3r2.Stroud(index), 1.0e-14) for index in [
        'E3r2 5-1', 'E3r2 5-2a', 'E3r2 5-2b', 'E3r2 5-3',
        'E3r2 7-1a', 'E3r2 7-1b',
        ]]
    )
def test_scheme(scheme, tol):
    degree = check_degree(
            lambda poly: quadpy.e3r2.integrate(poly, scheme),
            integrate_monomial_over_enr2,
            lambda n: quadpy.helpers.partition(n, 3),
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree, \
        'Observed: {}   expected: {}'.format(degree, scheme.degree)
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.e3r2.Stroud('E3r2 5-1')]
    )
def test_show(scheme, backend='mpl'):
    quadpy.e3r2.show(scheme, backend=backend)
    return


if __name__ == '__main__':
    scheme_ = quadpy.e3r2.Stroud('E3r2 14-1')
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_, backend='vtk')
