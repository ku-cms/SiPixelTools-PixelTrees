# PixelTrees

Make pixel trees used for testing and calibration of reconstruction.


## Software setup

Prepare your working directory with CMSSW

```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_0
cd CMSSW_11_2_0/src
cmsenv
git clone https://github.com/CMSTrackerDPG/SiPixelTools-PixelTrees.git SiPixelTools/PixelTrees
scram b -j 8
cd SiPixelTools/PixelTrees/test/
```
## Crab jobs

Documentation: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

To check crab write permissions: 
```
crab checkwrite --site <site>
```

To submit crab jobs:
```
crab submit -c <config_file>
```

