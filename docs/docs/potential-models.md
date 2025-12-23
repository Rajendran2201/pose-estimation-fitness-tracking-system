
| #  | Model / Solution              | Type          | Real-time on CPU? | Approx. setup difficulty | Keypoint count | Best for your 2-week project? | Main pros                              | Main cons                              | Recommended for 2 weeks? |
|----|-------------------------------|---------------|---------------------|---------------------------|----------------|-------------------------------|----------------------------------------|----------------------------------------|---------------------------|
| 1  | **MediaPipe Pose**            | 2D            | Yes (very fast)     | ★☆☆☆☆ (easiest)          | 33             | ★★★★★                         | Fastest path to working demo           | Slightly less accurate in hard cases   | **Strongly recommended**  |
| 2  | **MoveNet (Lightning/Thunder)** | 2D          | Yes                 | ★★☆☆☆                     | 17             | ★★★★                          | Very fast, good browser support        | Fewer keypoints, less detail           | Very good alternative     |
| 3  | **BlazePose (full body)**     | 2D            | Yes                 | ★★☆☆☆                     | 33             | ★★★★                          | Mobile-optimized, very fast            | Older than current MediaPipe           | Good if you want lightweight |
| 4  | **YOLOv8-Pose**               | 2D            | Yes (decent)        | ★★★☆☆                     | 17 (COCO)      | ★★★                           | Very easy to fine-tune, fast inference | Fewer keypoints, needs some tuning     | Good if you want YOLO ecosystem |
| 5  | **RTMPose (MMPose)**          | 2D            | Yes (fast models)   | ★★★☆☆                     | 17 / 133       | ★★★                           | Excellent accuracy-speed trade-off     | Slightly more setup than MediaPipe     | Worth considering         |
| 6  | **OpenPose**                  | 2D            | No (very slow)      | ★★★★☆                     | 25 + face/hands| ★★                            | Historically very popular              | Extremely slow without good GPU        | Avoid for 2 weeks         |
| 7  | **AlphaPose**                 | 2D            | Slow                | ★★★★☆                     | 17 / 26        | ★★                            | High accuracy                          | Slow, complex setup                    | Not recommended           |
| 8  | **HRNet (HigherHRNet)**       | 2D            | Slow                | ★★★★☆                     | 17             | ★★                            | Very high accuracy                     | Heavy, needs powerful GPU              | Not for 2 weeks           |
| 9  | **ViTPose / ViTPose++**       | 2D            | Depends             | ★★★★☆                     | 17 / more      | ★★                            | State-of-the-art accuracy              | Very heavy, slow inference             | No                        |
| 10 | **Lightweight OpenPose**      | 2D            | Yes (decent)        | ★★★★☆                     | 18/25          | ★★                            | Lighter than original OpenPose         | Still slower than MediaPipe            | Borderline                |
| 11 | **EfficientHRNet**            | 2D            | Yes (some versions) | ★★★★☆                     | 17             | ★★                            | Good speed-accuracy balance            | Still more complex than top 3          | Only if others fail       |
| 12 | **Detectron2 + Keypoint R-CNN**| 2D           | Slow                | ★★★★★                     | 17             | ★                             | Very flexible, high quality            | Very heavy, slow                       | No                        |
| 13 | **MMPose whole pipeline**     | 2D/3D         | Varies              | ★★★★☆–★★★★★              | Various        | ★                             | Most complete pose estimation toolbox  | Overkill for 2 weeks                   | No                        |
| 14 | **VideoPose3D**               | 3D (from 2D)  | No                  | ★★★★★                     | 17             | ★                             | Good 3D lifting from 2D                | Slow, needs good 2D input first        | No                        |
| 15 | **MotionBERT**                | 3D            | Slow                | ★★★★★                     | 17             | ★                             | Very strong 3D from video              | Extremely heavy, research-oriented     | No                        |
| 16 | **LiftFormer / PoseMamba**    | 3D            | Slow                | ★★★★★                     | 17             | ★                             | Latest 3D research approaches          | Not practical for short project        | No                        |
| 17 | **Custom fine-tuned model**   | 2D or 3D      | Depends             | ★★★★★                     | Depends        | ★                             | Can be best tailored solution          | Takes far too long in 2 weeks          | Only if you already have one |


Priority order (most recommended → least):

1. **MediaPipe Pose** → 90% of groups should start here  
2. **MoveNet (Lightning or Thunder)** → especially good if you want web/browser deployment  
3. **YOLOv8-Pose** → great if your group already knows Ultralytics/YOLO  
4. **RTMPose (mmpose lightweight models)** → if you want better accuracy than MediaPipe and are comfortable with slightly more setup  
5. Everything else → only if you have very specific reasons (and usually a lot more time)

### Fast Decision Guide

Your situation                              | Strongest recommendation
-------------------------------------------|---------------------------------
You have very little time                  | **MediaPipe Pose**
You want to run in browser                 | **MoveNet** (TensorFlow.js)
You already know YOLO well                 | **YOLOv8-Pose**
You want maximum accuracy possible in 2 weeks | **RTMPose** (small/medium models) or MediaPipe + post-processing
You want 3D poses                          | Very difficult in 2 weeks — stick to 2D
