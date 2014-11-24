#ifndef POWER_SPECTRUM_H
#define POWER_SPECTRUM_H

/* Conventions for power spectra:
 *   - k is measured in h/Mpc
 *   - P(k) is measured in (Mpc/h)^3
 *   - My Fourier conventions are
 *       \tilde f(k) = \int dx e^{-ikx} f(x)
 *       f(x) = \int \frac{dk}{(2\pi)^3} e^{ikx} \tilde f(k)
 *     which means P(k) is defined by
 *      (2pi)^3 \delta_D(k+k') P(k) = < \delta(k) \delta(k') >
*/

#include "Common.h"
#include "parray.h"


/**********************************************************************
 * PowerSpectrum
 *
 * Base class for double-space power spectra.
 *********************************************************************/

class PowerSpectrum {
public:
    PowerSpectrum();
    virtual ~PowerSpectrum();

    virtual const Cosmology& GetCosmology() const = 0;

    /* Evaluate power spectrum at a single k */
    virtual double Evaluate(double k) const = 0;
    double operator()(double k) const { return Evaluate(k); }

    /* Evaluate power spectrum at many k values (parallelized for speed) */
    virtual parray EvaluateMany(const parray& k) const;
    parray operator()(const parray& k) const { return EvaluateMany(k); }

    /* Calculate the variance with top-hat smoothing radius R Mpc/h */
    virtual double Sigma(double R) const;

    /* Calculate the 1-D velocity dispersion $\sigma_v^2 = \frac{1}{3} \int_0^\infty P(k) ~dk$ */
    virtual double VelocityDispersion() const;

    /* Calculate the non-linear scale $k_\text{nl} = 1/\sigma_v$ */
    virtual double NonlinearScale() const;

    /* Write power spectrum to file */
    virtual void Save(const char* filename, double kmin = 1e-3, double kmax = 1, int Nk = 1000, bool log = false);
};


#endif /* POWER_SPECTRUM_H */
