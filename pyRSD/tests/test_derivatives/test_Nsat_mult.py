from . import numdifftools, numpy
import pytest
from pyRSD.rsd.derivatives import compute
    
@pytest.fixture(scope='module', params=[True, False])
def socorr(request):
    return request.param
    
def test_total(driver, socorr):
    
    model = driver.theory.model
    
    # get the deriv arguments
    k    = driver.data.combined_k
    mu   = driver.data.combined_mu
    pars = driver.theory.fit_params
    args = (model, pars, k, mu)
    
    # set the socorr
    driver.theory.model.use_so_correction = socorr
    
    # our derivative
    x = compute('Nsat_mult', *args)
    
    # setup the numerical derivative
    index = driver.theory.free_names.index('Nsat_mult')
    theta = [driver.theory.fit_params[k].value for k in driver.theory.free_names]
    
    def f(x):
        t = theta.copy()
        t[index] = x
        driver.theory.set_free_parameters(t)
        return driver.theory.model.Pgal(k, mu)
          
    g = numdifftools.Derivative(f, step=1e-3)
    y = g(theta[index])
    
    # compare to 5% accuracy
    numpy.testing.assert_allclose(x, y, rtol=0.05, atol=0.01)
    

    
