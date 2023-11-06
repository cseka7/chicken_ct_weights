import os

threshold=0.5
bin_width=10
bin_min=0
bin_max=200


path_prefix='/datac3/inprogress/chicken'
manually_segmented_path=os.path.join(path_prefix, 'manually_labels')
dissected_path=os.path.join(path_prefix, 'dissected')
output_path=os.path.join(path_prefix, 'train')
tmp_path=os.path.join(path_prefix, 'tmp')
breast_features_path=os.path.join(path_prefix, 'breast_training_features-%d-%.2f.csv' % (bin_width, threshold))
leg_features_path=os.path.join(path_prefix, 'leg_training_features-%d-%.2f.csv' % (bin_width, threshold))
xls_path= os.path.join(path_prefix, 'chicken_data.xlsx')
breast_latex_path= os.path.join(path_prefix, 'breast.tex')
leg_latex_path= os.path.join(path_prefix, 'leg.tex')


save_registered_images=True

os.makedirs(output_path, exist_ok=True)
os.makedirs(tmp_path, exist_ok=True)

threads = 12

params= {'FixedImageDimension': 3,
         'MovingImageDimension': 3,
         'WriteResultImage': "true",
         'ResultImagePixelType': "double",
         'FixedInternalImagePixelType': "float",
         'MovingInternalImagePixelType': "float",
         'UseDirectionCosines': "true",
         'Registration': "MultiResolutionRegistration",
         'FixedImagePyramid': "FixedRecursiveImagePyramid",
         'MovingImagePyramid': "MovingRecursiveImagePyramid",
         'HowToCombineTransforms': "Compose",
         'DefaultPixelValue': -1024,
         'Interpolator': "BSplineInterpolator",
         'BSplineInterpolationOrder': "1",
         'ResampleInterpolator': "FinalBSplineInterpolator",
         'FinalBSplineInterpolationOrder': 3,
         'Resampler': "DefaultResampler",
         'Metric': "AdvancedMattesMutualInformation",
         'NumberOfHistogramBins': 32,
         'ImageSampler': "RandomCoordinate",
         'NumberOfSpatialSamples': 4048,
         'NewSamplesEveryIteration': "true",
         'NumberOfResolutions': 4,
         'Transform': "BSplineTransform",
         'Optimizer': "AdaptiveStochasticGradientDescent",
         'MaximumNumberOfIterations': 200,
         'FinalGridSpacingInVoxels': [10, 10, 10],
         'ResultImageFormat': "nii",
         'CheckNumberOfSamples': "false",
         "RandomSeed": 5}

latex_template = r'''\documentclass[preview]{{standalone}}
\usepackage{{booktabs}}
\begin{{document}}
{}
\end{{document}}
'''
