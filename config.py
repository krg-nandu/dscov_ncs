import os
import numpy as np

class Config(object):

    def __init__(self):
        #data directories
        self.base_dir = '/media/data_cifs/lakshmi/zebrafish/conditioningHQ'
        self.video_name = ['dark_bg_rec00.mp4', 'dark_bg_rec01.mp4', '04162019_sub00.mp4', '04162019_sub01.mp4',
                            '030818_video00.avi', '030818_video01.avi', '030818_video02.avi', '030818_video03.avi',
                            '030818_video04.avi', '030818_video05.avi', '070818_video07.mp4',
                            '04162019_sub02.mp4', '04232019_sub00.mp4',
                           '05102019_sub00.mp4', '05102019_sub03.mp4', '05102019_sub06.mp4', '06042019_sub00.mp4', 'BOOTSTRAP.mp4']

        self.label_dir = '/media/data_cifs/lakshmi/zebrafish/groundtruths/'
        self.tfrecord_dir = '/media/data_cifs/lakshmi/zebrafish/tfrecords/'

        self.test_video_name = ['/media/data_cifs/lakshmi/zebrafish/conditioningHQ/07232019_sub00.mp4'
                                ]
        self.condition = ['+']
        self.group = 'dark_stim_repeat'

        self.objects_to_include = [1] #fish ids to use!
        self.joints_to_extract = [0,1,2,3]
        self.data_prop = {'train':0.98,'val':0.01,'test':0.01}

        #tfrecords configuration
        self.train_tfrecords = 'train_box_darkandlight_bootstrapped.tfrecords'
        self.val_tfrecords = 'val_box_darkandlight_bootstrapped.tfrecords'
        self.test_tfrecords = 'test_box_darkandlight_bootstrapped.tfrecords'

        self.results_dir = '/media/data_cifs/lakshmi/zebrafish/results/'
        self.model_output = ''
        self.model_input = ''
        self.train_summaries = ''

        self.vgg16_weight_path = os.path.join(
             '/media/data_cifs/clicktionary/',
             'pretrained_weights',
             'vgg16.npy')

        #model settings
        self.model_type = 'vgg_regression_model_4fc'
        self.epochs = 100
        self.image_orig_size = [480, 640, 1]
        self.image_target_size = [416, 416, 1]

        self.label_shape = [13,13,3]
        self.resize_ims = True
        self.train_batch = 64
        self.val_batch= 8
        self.test_batch = 1

        self.model_output = '/media/data_cifs/lakshmi/zebrafish/darkAndLight_Bootstrapped/'
        self.model_name = 'cnn_box'
        self.num_classes = 2
