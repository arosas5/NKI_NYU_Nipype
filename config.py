# emacs =  -*- mode =  python; py-indent-offset =  4; indent-tabs-mode =  nil -*-
# vi =  set ft=python sts=4 ts=4 sw=4 et = 

"""
    Set which FSL to use
"""
FSLDIR = '/usr/share/fsl/4.1/'

"""
    Point to directory where your subjects reside
"""
subj_dir = '/home/data/Originals/NYU_TRT/'

"""
    Point to directory where pipeline can store results 
"""
sink_dir = '/home/data/Projects/nuisance_reliability_paper/results'

"""
    Set Temporary Directory where Nipype can store
    temporary results
"""
working_dir = '/home/data/Projects/nuisance_reliability_paper/working_dir/'

"""
    Set the location where 3mm and 2mm Tissue Priors
    located.
"""
prior_dir = '/home/data/Projects/nuisance_reliability_paper/tissuepriors'

"""
    Point to directory where pipeline can store crash .npz files
    if it crashes
"""
crash_dir = '/home/data/Projects/nuisance_reliability_paper'

"""
    Functional volumes to keep
    start_idx : starting volume
    stop_idx : Last volume
"""
start_idx = 0
stop_idx = 196
n_vols = 197
TR = 2.0

"""
    Seed file

    Each line contains full path to seed file

"""
seed_file = '/home/data/Projects/nuisance_reliability_paper/work_lists/seed_list.txt'

"""
    subj_file : '/data/ADHD200/docs/subjects.txt'
    Each line in the file contains subjects
    0010001
    0010002
    etc.
"""
func_session_file = '/home/data/Projects/nuisance_reliability_paper/work_lists/session_list.txt'
anat_session_file = '/home/data/Projects/nuisance_reliability_paper/work_lists/session_list.txt'
subj_file = '/home/data/Projects/nuisance_reliability_paper/work_lists/subject_list.txt'
log_file = None
standard_res = '3mm'
fwhm = [6]

"""
    Value : 1 or 0
"""
nuisanceHighPassFilter = 1
nuisanceLowPassFilter = 1

"""
    When nuisanceHighPassFilter : 1
    Set nuisanceHighPassLowCutOff to a decimal value

    When nuisanceHighPassFilter : 0
    Set nuisanceHighPassLowCutOff to None

    Same holds for nuisanceLowPassFilter & nuisanceLowPassHighCutOff

"""
nuisanceHighPassLowCutOff = [0.01]
nuisanceLowPassHighCutOff = [0.1]


""" 
------------------------ ALFF/fALFF Options ---------------------------
"""

"""
    For ALFF/fALFF only
    Notes: 1) this derivative is allergic to scrubbed data and thus will never use them.
           2) You need to specify both highPassFreqALFF and lowPassFreqALFF if you intend
              to use this derivative. The Default values are set below.  
"""

highPassFreqALFF = [0.005]
lowPassFreqALFF = 0.1

""" 
    Scrub data prior to derivate generation: In accord with Power et al. (2012); forking not enable yet for this step (next version).
    Default value 1/0
"""
scrubData = [0]



"""
    Number of components to regress with compcor
"""
ncomponents = [5]

"""
    Target Angle in Degree for Median Angle Correction
"""

target_angle_deg = [90]


"""
    Which Signals do you which to regress out
"""
#['global', 'compcor', 'wm', 'csf', 'gm', 'firstprinc', 'motion']
#regressors = [0, 0, 0, 0, 0, 1]
Corrections = [
                [0, 0, 0, 0, 0, 0, 1]
              ]


"""
    Mandatory
    where are your anatomical scans located relative to your Subjects Directory
    
    For data organized in session_id/subject_id format:
    anat_template_list = ['session', 'subject', 'mprage_anonymized']
    
    For data organized in subject_id/session_id format:
    anat_template_list = ['subject', 'session', 'mprage_anonymized']
"""
anat_template = '%s/%s/anat/%s.nii.gz'
anat_template_list = ['session', 'subject', 'mprage_anonymized']

"""
    Mandatory
    where are your functional scans located relative to your Subjects Directory
    
    For data organized in session_id/subject_id format:
    func_template_list = ['session', 'subject', 'lfo']
    
    For data organized in subject_id/session_id format:
    func_template_list = ['subject', 'session', 'lfo']
"""
func_template = '%s/%s/func/%s.nii.gz'
func_template_list = ['session', 'subject', 'lfo']

"""
    SET ONLY when analysis is not set to 'all' and u need to run alff

    where are  rest_res, rest_mask, rest_mask2standard  scans located
    relative to your Subjects Directory
"""
alff_template = '%s/*/%s.nii.gz'

"""
    SET ONLY when analysis is not set to 'all' and u need to run alff

    where are  example_func2highres.mat, highres2standard_warp.nii.gz scans located
    relative to your Subjects Directory
"""
alff_warp_template = '%s/*/*/%s'

"""
    SET ONLY when analysis is not set to 'all' and u need to run 
    generate functional connectivity maps. 

    where are  rest_res2standard.nii.gz, rest_res_filt.nii.gz,
    rest_mask2standard.nii.gz, example_func.nii.gz scans located
    relative to your Subjects Directory
"""
ifc_template = '%s/*/%s.nii.gz'

"""
    SET ONLY when analysis is not set to 'all' and u need to run 
    generate functional connectivity maps. 

    where are example_func2highres.mat,
              highres2standard_warp.nii.gz,
              stand2highres_warp.nii.gz
              highres2example_func.mat 
    scans located
    relative to your Subjects Directory
"""
ifc_warp_template = '%s/*/*/%s'

vmhc_rest_res_template = '%s/*/%s.nii.gz'
vmhc_anat_reorient_template = '%s/*/%s.nii.gz'
vmhc_example_func2highres_mat_template = '%s/*/*/%s'

""" 
------------- Timeseries Extraction Options ---------------------------
"""

"""
    For Unit Timeseries Extraction Only
Note: Definitions Directory should contain one subdirectory for each set of units to be generated (e.g., Harvard-Oxford Atlas, AAL, Craddock, Dosenbach-160); one output file / set define   
"""
unitDefinitionsDirectory = '/usr/share/fsl/4.1/data/atlases/HarvardOxford/'

# Output type: .csv, numPy
unitTSOutputs = [1, 1]

""" 
    For Voxel Timeseries Extraction Only
Note: Definitions Directory should contain one subdirectory for each mask/mask set to be used to select voxels to be output; one output file / mask 
"""
voxelMasksDirectory = '/usr/share/fsl/4.1/data/atlases/HarvardOxford/'


# Output type: .csv, numPy
voxelTSOutputs = [0, 1]

""" 
    For Vertices Timeseries Extraction Only
"""
# Output type: .csv, numPy
verticesTSOutputs = [0, 1]

reconSubjectsDirectory = '/home/data/Projects/nuisance_reliability_paper/recon_subjects'
""" 
**************************************************************
"""

""" 
********************* FSL Group Analysis *********************
Notes: 
- Separate group analysis conducted for each derivative
- Not applicable to time series extraction derivatives
"""

""" 
Specify Model List File that contains one or more models to be executed per derivate
"""
modelsList = 'home/ssikka/myModels.txt'

z_threshold = 2.3
p_threshold = 0.05
f_test = 1

# all, basic, scrubbing, nuisance, alff, ifc, vmhc, reho, group_analysis
analysis = [0, 1, 0, 0, 0, 0, 0, 0, 0 ]
run_on_grid = 0
qsub_args = '-q all.q'
num_cores = 10
