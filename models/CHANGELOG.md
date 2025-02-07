# Changelog for Play Prediction XGBoost Model

## Version 1.2.0 (2024-06-14)
- **Hyperparameter Tuning**
  - Conducted Search CV using Bayesian Optimization for hyperparameter tuning
  - Optimal hyperparameters found: 
    - `colsample_bytree=0.9621`
    - `eta=0.0968`
    - `gamma=3.377`
    - `max_depth=14`
    - `min_child_weight=9.775`
    - `reg_alpha=4.537`
    - `reg_lambda=1.181`
    - `scale_pos_weight=1.038`
    - `subsample=0.7229`
  - Model performance: Accuracy = 72.50%, F1-score = 0.66.

## Version 1.1.1 (2024-06-11)
- **GPU Training**
  - Processed data converted to DMatrix
  - Training moved to GPU if available
  - Model performance: Accuracy = 72.42%, F1-score = 0.66.

## Version 1.1.0 (2024-06-06)
- **Identification Added**
  - Added identification features: poscoach, posteam
  - Re-added "snap-timing" features: no_huddle, shotgun
  - Model performance: Accuracy = 72.34%, F1-score = 0.66.

## Version 1.0.0-min (2024-06-05)
- **"Minify" Model**
  - Removed "snap-timing" features: no_huddle, shotgun
  - Model performance: Accuracy = 69.37%, F1-score = 0.63.

## Version 1.0.0 (2024-05-16)
- **Initial release**
  - Implemented basic XGBoost model with default parameters.
  - Model performance: Accuracy = 71.85%, F1-score = 0.64.
