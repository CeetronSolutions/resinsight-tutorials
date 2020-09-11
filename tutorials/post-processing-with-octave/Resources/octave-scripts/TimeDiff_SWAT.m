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



SWAT = riGetActiveCellProperty("SWAT");

SWATDIFF = SWAT;

# Calculate the change in water saturation with time compared to timestep 1
for i=1:columns(SWAT) 
	SWATDIFF(:,i) = SWAT(:,i) - SWAT(:,1);
endfor

riSetActiveCellProperty(SWATDIFF, "SWAT_dt_DIFF");

