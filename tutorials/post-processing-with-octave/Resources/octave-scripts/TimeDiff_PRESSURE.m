# Created by hhgs July 2014
#-----------------------------------------------------------------------------------
# For working in a standalone Octave session with ResInsight data, 
#  -> set "addpath" active to the riOctave-functions (and to script folder if needed)
#
# For resinsight:
#addpath("/project/res/x86_64_RH_6/share/Resinsight/jenkins_master");
#
# For resinsightdaily:
#addpath("/project/res/x86_64_RH_6/share/Resinsight/jenkins_daily_install");
#-----------------------------------------------------------------------------------



PRESSURE = riGetActiveCellProperty("PRESSURE");

PRESDIFF = PRESSURE;

# Calculate the change in pressure with time compared to timestep 1
for ts=1:columns(PRESSURE) 
	PRESDIFF(:,ts) = PRESSURE(:,ts) - PRESSURE(:,1);
endfor

riSetActiveCellProperty(PRESDIFF, "PRES_dt_DIFF");
