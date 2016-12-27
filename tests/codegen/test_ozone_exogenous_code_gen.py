import pandas as pd
import numpy as np

import ForecastEngine as autof
import Bench.TS_datasets as tsds

import CodeGen.TS_CodeGenerator as tscodegen

import warnings

from CodeGen import TS_CodeGenerator as tscodegen

#get_ipython().magic('matplotlib inline')

with warnings.catch_warnings():
    # warnings.simplefilter("error")

    b1 = tsds.load_ozone_exogenous()
    df = b1.mPastData

    H = b1.mHorizon;
    
    N = df.shape[0];
    for n in range(2*H,  N , 10):
        df1 = df.head(n).copy();
        lEngine = autof.cForecastEngine()
        lEngine
        #    lEngine.mOptions.mEnableSeasonals = False;
        #    lEngine.mOptions.mEnableCycles = False;
        #    lEngine.mOptions.mEnableARModels = False;
        #    lEngine.mOptions.mDebugCycles = True;
        lExogenousData = (b1.mExogenousDataFrame , b1.mExogenousVariables) 
        lEngine.train(df1 , b1.mTimeVar , b1.mSignalVar, H, lExogenousData);
        lEngine.getModelInfo();
        lEngine.mSignalDecomposition.mBestModel.mTimeInfo.mResolution
        lEngine.standrdPlots(name = "outputs/my_arx_ozone_")
        lCodeGenerator = tscodegen.cTimeSeriesCodeGenerator();
        lSQL = lCodeGenerator.testGeneration(lEngine);
        
