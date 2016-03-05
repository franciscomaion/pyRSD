%module gcl

%{
#define SWIG_FILE_WITH_INIT
%}

%naturalvar;

%include "numpy.i"

%init %{
    import_array();
%}

%include "typemaps.i"
%include "std_string.i"
using std::string;

%feature("kwargs");
%feature("autodoc");

%include "parray.i"
%include "Common.i"
%include "Spline.i"

//%include "Datafile.i"
%include "DiscreteQuad.i"
//%include "Timer.i"

%include "Engine.i"
%include "ClassParams.i"
%include "ClassCosmology.i"
%include "Cosmology.i"
%include "PowerSpectrum.i"
%include "LinearPS.i"
%include "OneLoopPS.i"
%include "CorrelationFunction.i"
%include "Kaiser.i"
%include "Imn.i"
%include "Jmn.i"
%include "Kmn.i"
%include "ImnOneLoop.i"
%include "ZeldovichPS.i"
%include "NonlinearPS.i"
%include "MyFFTLog.i"
%include "ZeldovichCF.i"




