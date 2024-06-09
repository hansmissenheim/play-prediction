# Changelog for Play Prediction XGBoost Model

## Version 1.1.1 (2024-06-07)
- **Performance Fix**
  - Trained dataset split after data processing
  - Model performance: Accuracy = 73.23%, F1-score = 0.69.

## Version 1.1.0 (2024-06-06)
- **Identification Added**
  - Added identification features: poscoach, posteam
  - Readded "snap-timing" features: no_huddle, shotgun
  - Model performance: Accuracy = 72.34%, F1-score = 0.66.

## Version 1.0.0-min (2024-06-05)
- **"Minify" Model**
  - Removed "snap-timing" Features: no_huddle, shotgun
  - Model performance: Accuracy = 69.37%, F1-score = 0.63.
Removed Shotgun and Hurry Up

## Version 1.0.0 (2024-05-16)
- **Initial release**
  - Implemented basic XGBoost model with default parameters.
  - Model performance: Accuracy = 71.85%, F1-score = 0.64.