import os

threshold=0.5
bin_width=10
bin_min=0
bin_max=200


path_prefix_data= 'data'
path_prefix_results= 'results'
manually_segmented_path=os.path.join(path_prefix_data, 'manually_labels')
dissected_path=os.path.join(path_prefix_data, 'dissected')
breast_features_path=os.path.join(path_prefix_data, 'breast_training_features-%d-%.2f.csv' % (bin_width, threshold))
thigh_features_path=os.path.join(path_prefix_data, 'thigh_training_features-%d-%.2f.csv' % (bin_width, threshold))
xls_path= os.path.join(path_prefix_data, 'chicken_dissected_data.xlsx')

save_registered_images=True

output_path=os.path.join(path_prefix_data, 'training')
tmp_path=os.path.join(path_prefix_data, 'tmp')
os.makedirs(output_path, exist_ok=True)
os.makedirs(tmp_path, exist_ok=True)

threads = 12
elastix_params= {'FixedImageDimension': 3,
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
         'ResultImageFormat': "nii.gz",
         'CheckNumberOfSamples': "false",
         "RandomSeed": 5}


