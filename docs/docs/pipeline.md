# Pipeline for the pose estimation fitness tracking system


## Phase 0: Problem Framing
- Define one core research problem
- **Example**: Build a real-time system using smartphone cameras to track exercise form, count reps, and provide posture feedback for common workouts.
- Formulate research questions like: _"How can we improve accuracy in occluded environments?"_ or _"What metrics best evaluate injury prevention?"_
- Decide the evaluation metrics.
- Review existing works. Identify gaps, such as limited real-world datasets or edge device efficiency.
- Decide the stack (Hardware, software, datasets).
- Decide the business constraints.

## Phase 1: Data Collection and Preparation 
- Create or gather datasets. (Human3.6M (for 3D poses) or Fitness-specific subsets from YouTube-8M.)
- Collect atleast 5000 annotated frames.
- Annotate data (if required)
- Preprocess data: Augment with flips, rotations, and noise using libraries like Albumentations. Split into train/validation/test sets (80/10/10). Handle class imbalances if focusing on specific poses.
- Ethical considerations: remove PII (e.g., anonymize faces)

## Phase 2: Model Selection and Implementation 
- Choose baseline models (MediaPipe Pose or BlazePose)
- Set up development environment
- Customise for fitness: add modules for rep counting and feesbacks.
- Incorporate advanced features.

## Phase 3: Training and Optimization
- Train and fintune models (hyperparamater tuning)
- Evaluate performance (PCK (Percentage of Correct Keypoints), MPJPE (Mean Per Joint Position Error))
- Optimise for real-time (reduce model size with quantization for mobile deployment)

## Phase 4: System Integration and User Interface 
- Build the full pipeline (Add feedback loops using OpenCV drawing functions)
- Develop UI/App
- Testing and Validation

## Phase 5: Documentation, Deployment, and Dissemination 
- Documentation: Write the research paper (in LaTeX) covering methods, results, and limitations.
- Deploy the system: Host on cloud.
- Submit to conferences. 
