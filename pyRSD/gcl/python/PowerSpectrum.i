%{
#include "PowerSpectrum.h"
%}

class PowerSpectrum {
public:
    PowerSpectrum();
    virtual ~PowerSpectrum();

    // translated to __call__ -> calls Evaluate(K)
    double operator()(const double k) const;
    
    // translated to __call__ -> calls EvaluateMany(K)
    parray operator()(const parray& k) const;
     
    const Cosmology& GetCosmology() const = 0;
    void Save(const char* filename, double kmin = 1e-3, double kmax = 1, int Nk = 1001, bool log = false);
    
    // mass variance sigma(R)
    double Sigma(double R) const;
    
    // 1D velocity dispersion
    double VelocityDispersion() const;
    
    // 1 / 1D velocity disp
    double NonlinearScale() const;
    
    // sigma_v as a function of k
    parray VelocityDispersion(const parray& k) const;
    double VelocityDispersion(const double k) const;
    
    // Zeldovich approximation integrals
    parray X_Zel(const parray& k) const;
    double X_Zel(const double k) const;
    
    parray Y_Zel(const parray& k) const;
    double Y_Zel(const double k) const;
};

