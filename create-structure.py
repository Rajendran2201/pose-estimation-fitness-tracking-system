from pathlib import Path

BASE_DIR = Path("pose-fitness-tracker")

DIRS = [
    "docs",
    "datasets/raw",
    "datasets/processed",
    "datasets/scripts",
    "models/pose/movenet",
    "models/temporal/tcn",
    "models/temporal/lstm",
    "models/temporal/checkpoints",
    "training/config",
    "training/notebooks",
    "evaluation",
    "web/public",
    "web/src/camera",
    "web/src/pose",
    "web/src/features",
    "web/src/temporal",
    "web/src/feedback",
    "web/src/utils",
    "android/app/src/main/java/com/posefit/camera",
    "android/app/src/main/java/com/posefit/pose",
    "android/app/src/main/java/com/posefit/features",
    "android/app/src/main/java/com/posefit/temporal",
    "android/app/src/main/java/com/posefit/feedback",
    "android/app/src/main/java/com/posefit/ui",
    "tests/data_pipeline",
    "tests/features",
    "tests/temporal",
    "tests/training",
    "scripts",
]

FILES = [
    "README.md",
    "requirements.txt",
    "datasets/scripts/extract_pose.py",
    "datasets/scripts/build_windows.py",
    "training/train_classifier.py",
    "training/train_form_score.py",
    "training/export_tflite.py",
    "evaluation/metrics.py",
    "evaluation/rep_count_eval.py",
    "web/src/app.js",
    "web/src/camera/webcam.js",
    "web/src/pose/detector.js",
    "web/src/pose/normalize.js",
    "web/src/features/angles.js",
    "web/src/features/velocity.js",
    "web/src/temporal/buffer.js",
    "web/src/temporal/inference.js",
    "web/src/feedback/coach.js",
    "web/src/utils/math.js",
    "tests/data_pipeline/test_pose_extraction.py",
    "tests/data_pipeline/test_windowing.py",
    "tests/features/test_angles.py",
    "tests/features/test_velocity.py",
    "tests/temporal/test_buffer.py",
    "tests/training/test_model_io.py",
    "scripts/download_datasets.sh",
    "scripts/convert_models.sh",
]

INIT_FILES = [
    "datasets/scripts/__init__.py",
    "training/__init__.py",
    "tests/__init__.py",
]


def main():
    print("Creating project structure...")

    BASE_DIR.mkdir(exist_ok=True)

    for d in DIRS:
        path = BASE_DIR / d
        path.mkdir(parents=True, exist_ok=True)

    for f in FILES:
        path = BASE_DIR / f
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

    for f in INIT_FILES:
        path = BASE_DIR / f
        if not path.exists():
            path.touch()

    print("Done.")
    print(f"Project created at: {BASE_DIR.resolve()}")


if __name__ == "__main__":
    main()
