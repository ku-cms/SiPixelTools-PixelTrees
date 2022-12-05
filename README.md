# PixelTrees

Make pixel trees used for testing and calibration of reconstruction.


## Software setup

Prepare your working directory.

Setup for CMSSW_11_2_0:
```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_0
cd CMSSW_11_2_0/src
cmsenv
git clone git@github.com:ku-cms/SiPixelTools-PixelTrees.git SiPixelTools/PixelTrees
scram b -j 8
cd SiPixelTools/PixelTrees/test
```

Setup for CMSSW_12_5_2:
```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_12_5_2
cd CMSSW_12_5_2/src
cmsenv
git clone git@github.com:ku-cms/SiPixelTools-PixelTrees.git SiPixelTools/PixelTrees
scram b -j 8
cd SiPixelTools/PixelTrees/test
```

## Crab jobs

Documentation: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

Initiate grid certificate:
```
voms-proxy-init --valid 192:00 -voms cms
voms-proxy-info
```

To check crab write permissions: 
```
crab checkwrite --site <site>
```
Check crab write for user area on cmslpc:
```
crab checkwrite --site=T3_US_FNALLPC
```
Check crab write for group area on cmslpc:
```
crab checkwrite --site=T3_US_FNALLPC --lfn=/store/group/lpcsusylep
```

Check group area storage space:
```
eosgrpquota lpcsusylep
```

To submit crab jobs:
```
cmsenv
crab submit -c <config_file>
crab status -d <directory>
```
Example:
```
cmsenv
crab submit -c crab-zerobias-2022.py
crab status -d ./crab_PixelTree_ZeroBias_2022F_RAW_v1_Run362154_v1
crab status --verboseErrors -d ./crab_PixelTree_ZeroBias_2022F_RAW_v1_Run362154_v1
```

