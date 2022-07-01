#! /usr/bin/env python3
from detectron2.utils.logger import setup_logger
setup_logger()
import cv2,sys,os
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


"""
Input: image

Identify keypoints

Output: 
Matrix with the keypoints
Image with the identification of the keypoints

Dependencies: 
    - Detectron2
    - OpenCV
"""
 

'''
"keypoints": [
"nose",
"left_eye",
"right_eye",
"left_ear",
"right_ear",
"left_shoulder",
"right_shoulder",
"left_elbow",
"right_elbow",
"left_wrist",
"right_wrist",
"left_hip",
"right_hip",
"left_knee",
"right_knee",
"left_ankle",
"right_ankle"
]'''

if __name__ == '__main__':
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7  # set threshold for this model
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml")
    predictor = DefaultPredictor(cfg)
    try:
        imagePath  = '/home/'+os.environ.get('USER')+'/openpose/openpose_implementations/src/image4734328.png'
        frame = cv2.imread(imagePath)
        outputs = predictor(frame)
        #outputs["instances"].pred_classes
        #outputs["instances"].pred_boxes
        #print(outputs["instances"])
        #print(outputs["instances"].pred_keypoints)
       
        v = Visualizer(frame[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        newImage = v.get_image()[:, :, ::-1]
        cv2.putText(newImage , "Detectron2", (20, 40),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        file_image_output='/home/'+os.environ.get('USER')+'/openpose/openpose_implementations/KIMHuV_image_output_detectron2.png'
        cv2.imwrite(file_image_output, newImage)

        print(outputs["instances"].pred_keypoints)    

        #Example Get KeyPoint
        #numKeyPoint=1
        #np_array = outputs["instances"].pred_keypoints[0][numKeyPoint].cpu().numpy()

                
    except:
        print( sys.exc_info()[0])
     
    cv2.destroyAllWindows()

   