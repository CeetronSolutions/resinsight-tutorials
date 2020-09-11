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



SOIL = riGetActiveCellProperty("SOIL");

SOILDIFF = SOIL;

# Calculate the change in oil saturation with time compared to timestep 1
for i=1:columns(SOIL) 
	SOILDIFF(:,i) = SOIL(:,i) - SOIL(:,1);
endfor

riSetActiveCellProperty(SOILDIFF, "SOIL_dt_DIFF");

