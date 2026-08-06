---
name: datasci-kaggle-roadmap
description: |
  A structured learning roadmap for preparing data science skills via Kaggle Learn courses. Designed for self-directed learners starting from scratch with limited time, targeting internship readiness within 6-8 weeks. Covers Python, SQL, Pandas, ML fundamentals, intermediate ML, and feature engineering. Includes weekly progression, hands-on practice patterns, and internship-readiness milestones.
license: Open for personal use and iteration
---

# Data Science Kaggle Learning Roadmap

A self-paced path from zero to internship-ready through Kaggle Learn courses. This roadmap balances theoretical understanding with practical application, emphasizing the skills you'll actually use in an internship environment.

**Target Timeline:** 6–8 weeks (part-time, ~8–12 hours per week)  
**Goal:** Internship readiness with demonstrated project work

---

## Quick Overview

| Week | Module | Estimated Hours | Deliverable |
|------|--------|-----------------|-------------|
| 1 | Python + SQL Foundations | 5–7 | Python syntax cert + first SQL query |
| 2 | SQL Mastery + Pandas Start | 7–8 | BigQuery analysis + DataFrame basics |
| 3 | Pandas Deep Dive | 8–10 | Data cleaning & transformation script |
| 4 | Intro to ML | 8–10 | Decision Tree + validation concepts |
| 5 | Intermediate ML | 8–10 | XGBoost model + feature insights |
| 6 | Feature Engineering | 10–12 | Custom feature creation + model comparison |
| 7–8 | Capstone Project | 15–20 | End-to-end competition or portfolio project |

---

## Module 1: Python Foundations (Week 1)

**Goal:** Claim Python certificate and solidify syntax for data work.

### Approach
Since you already code (OOP, C++), skim Python rather than drill basics. Focus on *data structures* specific to ML workflows: lists, dictionaries, comprehensions, and functional patterns that Pandas relies on.

### Kaggle Courses
- **Python** (~2–3 hours to skim)
  - Skim: Variables, data types, functions, control flow
  - Deep dive only: List comprehensions, lambda functions, functional programming patterns
  - **Why:** Pandas is built on these patterns; you'll see `df.apply(lambda x: ...)` constantly

### Hands-On Practice
1. **Exercise:** Write a function that loads a CSV as nested dicts (manually, no pandas yet) and filters by a condition
   - Cements list/dict patterns before Pandas abstracts them
2. **Deliverable:** Claim Python certificate

### Checkpoint
- [ ] Python certificate claimed
- [ ] Can write list comprehensions and lambdas without looking them up
- [ ] Understand when to use dict vs. list vs. set

---

## Module 2: SQL Fundamentals + Kaggle BigQuery (Week 2)

**Goal:** Query massive datasets with confidence; understand relational logic.

### Why This Matters
In an internship, you won't build the data pipeline—you'll *query* it. SQL is often the first step: "Pull me X from the database where Y condition holds." This is where analysis begins.

### Kaggle Courses
- **Intro to SQL** (~3–4 hours)
  - Learn: SELECT, WHERE, JOIN, GROUP BY, HAVING, ORDER BY
  - **Focus heavily on:** 
    - Filtering (WHERE clauses that don't break performance)
    - Multi-table joins (LEFT, INNER, CROSS)
    - Aggregation patterns (SUM, COUNT, AVG with GROUP BY)
  - Learn: BigQuery syntax and quirks (dataset.table notation, etc.)

### Hands-On Practice
1. **Exercise 1:** Write a query that:
   - Pulls data from 2 related tables with a LEFT JOIN
   - Filters to a date range
   - Groups by category and counts rows
   - Orders by count descending
   - Example: "Get product sales by category for the last 6 months, ranked by volume"

2. **Exercise 2 (Harder):** Self-join query
   - Find duplicate users based on email patterns, or similar records
   - Reinforces the mental model of joining a table to itself

3. **Deliverable:** Screenshot of your first end-to-end BigQuery result (preferably public dataset like Google Analytics sample, GitHub archive, or similar)

### Checkpoint
- [ ] Intro to SQL certificate claimed
- [ ] Can write a 3-table JOIN without syntax errors on first try
- [ ] Understand GROUP BY order of operations (WHERE before GROUP BY, HAVING after)
- [ ] Familiar with BigQuery console and public datasets

---

## Module 3: Pandas — The Critical Bridge (Weeks 2–3)

**Goal:** Move fluently from raw data to structured analysis. This is where 40% of real work lives.

### Why This Matters
SQL *gets* the data. Pandas *prepares* it: handling missing values, transforming columns, reshaping tables, deriving new features. Most internship projects spend 60–70% of time in Pandas.

### Kaggle Courses
- **Pandas** (~6–8 hours)
  - Learn: DataFrames vs. Series, reading CSV/JSON, basic indexing
  - **Focus heavily on:**
    - `.loc[]`, `.iloc[]`, boolean indexing (filtering rows)
    - `.groupby()` aggregation and `.agg()` with custom functions
    - `.merge()` / `.join()` (SQL-like operations in code)
    - `.apply()` and `.map()` for row/column transformations
    - Handling missing values: `.fillna()`, `.dropna()`, `.interpolate()`
    - `.pivot_table()` and `.melt()` (reshaping data)
    - `.sort_values()` and multi-index operations
  - **Skim:** Advanced indexing, multi-index (you'll learn by doing)

### Hands-On Practice

1. **Exercise 1: Load & Explore**
   - Load a CSV (Kaggle dataset or public data)
   - Check shape, dtypes, missing values
   - Compute basic statistics
   - **Deliverable:** A 5-line Python script that does this

2. **Exercise 2: Transform**
   - Filter to rows matching a condition
   - Create a new column via `.apply()` or arithmetic
   - Group by a category and compute aggregates
   - Sort and display top 10 rows
   - **Example:** "Load sales data, create a 'profit margin %' column, group by region, find top 3 regions by revenue"

3. **Exercise 3: Handle Missing Data**
   - Load a messy dataset (intentionally with NaNs)
   - Identify missing patterns (visualize with `df.isnull().sum()`)
   - Fill strategically: mean for numeric, mode for categorical, drop if >50% missing
   - **Why:** Real datasets are always messy; this habit is essential

4. **Exercise 4: Merge Two DataFrames**
   - Create two small DataFrames manually (users, purchases)
   - Merge on a key column (user_id)
   - Try left, inner, outer joins and note the differences
   - **Why:** This mimics SQL joins but in Python; you'll do it constantly

5. **Capstone Pandas Script:**
   - Load 2–3 related datasets
   - Merge them
   - Clean missing values
   - Create 2–3 derived columns
   - Compute grouped statistics
   - Save cleaned result to CSV
   - **Deliverable:** Clean Python script + output CSV

### Checkpoint
- [ ] Pandas certificate claimed
- [ ] Can load, filter, groupby, and merge without documentation
- [ ] Comfortable with `.apply()` and `.map()` for custom transformations
- [ ] Understand the difference between `.loc[]` and `.iloc[]`
- [ ] Have a reusable data-cleaning script template

---

## Module 4: Intro to Machine Learning (Week 4)

**Goal:** Learn the ML workflow and train your first models.

### Why This Matters
ML is the "why" of data science—the goal that justifies all the data engineering. You'll learn the actual process: split data, train, validate, predict.

### Kaggle Courses
- **Intro to Machine Learning** (~5–7 hours)
  - Learn: What is ML? Supervised vs. unsupervised
  - **Focus heavily on:**
    - Training and validation sets (why 80/20 split matters)
    - Decision Trees: how they work conceptually
    - Model evaluation metrics:
      - **Mean Absolute Error (MAE):** avg absolute deviation from actual. Intuitive, same units as target.
      - **RMSE:** penalizes large errors more; use when big errors are costly
      - **R² (coefficient of determination):** "% of variance explained"; useful for comparing models
    - Cross-validation: why it's more reliable than a single validation split
    - Random Forest basics (ensemble of trees, reduces overfitting)
  - **Skim:** Gradient boosting (covered in Intermediate ML in detail)

### Hands-On Practice

1. **Exercise 1: Train a Decision Tree**
   - Load a regression dataset (house prices, bike rentals, etc.)
   - Split 80/20 train/validation
   - Train a DecisionTreeRegressor
   - Compute MAE on both sets
   - **Expected pattern:** Train MAE < Validation MAE (overfitting signal)

2. **Exercise 2: Random Forest**
   - Same dataset
   - Train a RandomForestRegressor with default params
   - Compare MAE vs. Decision Tree
   - Try adjusting `n_estimators` (number of trees)
   - **Why:** Ensembles are more robust; parameter tuning is practical skill

3. **Exercise 3: Cross-Validation**
   - Use `cross_val_score()` with 5-fold CV
   - Compare single-split validation MAE vs. CV MAE
   - **Observation:** CV is more stable and uses data efficiently

4. **Capstone ML Script:**
   - Load a Kaggle dataset (classification or regression)
   - Data prep: handle missing values, encode categoricals (if needed), scale features
   - Train/validation split
   - Train Decision Tree and Random Forest
   - Compute MAE (regression) or accuracy/precision/recall (classification)
   - Create a comparison table
   - **Deliverable:** Jupyter notebook with results

### Checkpoint
- [ ] Intro to Machine Learning certificate claimed
- [ ] Can train a tree-based model and evaluate it without errors
- [ ] Understand train/validation split and why it matters
- [ ] Know the difference between overfitting and underfitting
- [ ] Familiar with MAE and RMSE; can compute them by hand

---

## Module 5: Intermediate Machine Learning (Week 5)

**Goal:** Handle real-world messiness and use powerful algorithms.

### Why This Matters
Intro ML assumes clean data. Real internship work: missing values, categorical text, imbalanced classes. This module teaches the practical tricks that make models work on real data.

### Kaggle Courses
- **Intermediate Machine Learning** (~5–7 hours)
  - Learn: Handling missing data in the ML pipeline (before training)
  - **Focus heavily on:**
    - Categorical encoding:
      - One-hot encoding: for low-cardinality categories (< 10 unique values)
      - Target encoding (mean encoding): for high-cardinality, but watch for leakage
      - Ordinal encoding: for ordered categories (e.g., Low < Medium < High)
    - Missing value strategies:
      - Drop columns/rows (if < 5% missing)
      - Impute: mean/median/mode (simple), KNN (more sophisticated)
      - Missing as a feature (if missingness is informative)
    - **XGBoost:** Gradient boosted trees, often best-in-class performance
      - Why it beats Random Forest: iterative learning, handling non-linearity
      - Key params: `learning_rate`, `max_depth`, `n_estimators`
    - Pipelines: chain preprocessing + model training
    - Permutation Feature Importance: understand which features actually drive predictions

### Hands-On Practice

1. **Exercise 1: Categorical Encoding**
   - Load a dataset with mixed types (numeric + text columns)
   - One-hot encode a low-cardinality column (e.g., product category)
   - Train a model on encoded + numeric data
   - Compare performance with/without the categorical column
   - **Observation:** Categorical features often matter a lot

2. **Exercise 2: Missing Data Strategies**
   - Load a dataset intentionally (or create one with NaNs)
   - Try three approaches on the same model:
     - Drop rows with missing values
     - Impute with mean
     - Impute with KNN (using sklearn's KNNImputer)
   - Compare MAE on validation set
   - **Expected:** KNN often beats mean, but not always; context matters

3. **Exercise 3: XGBoost vs. Random Forest**
   - Same dataset (now with preprocessing)
   - Train RandomForestRegressor and XGBRegressor
   - Compare MAE and runtime
   - Adjust XGBoost learning rate and depth
   - **Expected:** XGBoost often faster and more accurate, but RF is simpler

4. **Exercise 4: Permutation Importance**
   - Train a model (RF or XGBoost)
   - Compute permutation importance for each feature
   - Rank features by importance
   - Drop the bottom 10% least important and retrain
   - Does performance stay the same? (If yes, you've removed noise)

5. **Capstone Intermediate ML Script:**
   - Load a realistic dataset (Kaggle competition or real-world)
   - Data prep pipeline:
     - Handle missing values (multiple strategies explored)
     - Encode categoricals
     - Drop low-variance features
   - Train 2 models (Random Forest + XGBoost)
   - Compute feature importance
   - Create a comparison: model name, MAE, top 5 features
   - **Deliverable:** Notebook + comparison table

### Checkpoint
- [ ] Intermediate Machine Learning certificate claimed
- [ ] Can encode categorical variables without errors
- [ ] Understand when to impute vs. drop missing data
- [ ] Have trained XGBoost and know how to adjust key hyperparameters
- [ ] Can compute and interpret feature importance

---

## Module 6: Feature Engineering (Weeks 5–6)

**Goal:** Create new features that make models smarter. This is where ML becomes art.

### Why This Matters
Algorithms learn from features you give them. Bad features → bad predictions. Good features → magic. Feature engineering is 50–70% of ML competition wins. In an internship, this is high-visibility work.

### Kaggle Courses
- **Feature Engineering** (~6–8 hours)
  - Learn: Philosophy of feature engineering (domain knowledge + data exploration)
  - **Focus heavily on:**
    - **Transformations:** log, sqrt, binning (convert continuous to buckets)
    - **Interactions:** multiply features (e.g., width × height = area)
    - **Domain-specific:** if data is ecommerce, create "days since last purchase," "total spent", "refund rate"
    - **Aggregations:** group by category and compute count, mean, max for each record
    - **Time-based:** extract year, month, day-of-week; compute rolling averages, lag features
    - **Text:** vectorize using TF-IDF or word counts (if you have text columns)
  - **The process:**
    1. Explore the data (distributions, correlations, outliers)
    2. Brainstorm features (list 5–10 ideas based on domain logic)
    3. Create them
    4. Train model, measure importance
    5. Iterate: keep high-importance features, drop low-importance ones

### Hands-On Practice

1. **Exercise 1: Univariate Transformations**
   - Load a dataset with skewed distributions (check with histograms)
   - Apply log/sqrt to skewed numeric columns
   - Train a model on original vs. transformed data
   - Compare MAE
   - **Observation:** Transformation often helps tree-based models less than linear models, but can reveal patterns

2. **Exercise 2: Interactions**
   - Select 2–3 numeric columns
   - Create interaction features: col1 × col2, col1 / col2, col1 + col2
   - Train a model on original + interaction features
   - Use permutation importance to see if interactions help
   - **Example:** width × height = area; even trees benefit from explicit area feature

3. **Exercise 3: Time-Based Features**
   - Load a dataset with a timestamp column
   - Extract: year, month, day-of-week, hour
   - Compute lag features: value yesterday, 7 days ago, 30 days ago (if applicable)
   - Train model on original vs. time-enhanced features
   - **Why:** Seasonality and trends matter in most business data

4. **Exercise 4: Aggregation Features**
   - Group by a categorical column (e.g., user_id, region, product)
   - For each row, compute: count of group, mean of target in group, max in group
   - Add these as features to the model
   - Train and check importance
   - **Real-world pattern:** "How many purchases has this user made?" is often the top feature

5. **Capstone Feature Engineering Project:**
   - Load a Kaggle dataset (or the one from Module 5)
   - Brainstorm 8–10 feature ideas (write them down first)
   - Create 5–7 of them
   - Train two models: one on original features, one on original + engineered
   - Compute feature importance on both
   - Create a comparison:
     - Feature name, importance, whether it's original or engineered
     - Model performance comparison (MAE/accuracy)
   - **Deliverable:** Notebook with clear feature creation code + importance plot

### Checkpoint
- [ ] Feature Engineering certificate claimed
- [ ] Can create 5+ types of features (transformations, interactions, aggregations, time-based, domain-specific)
- [ ] Understand that feature importance is your feedback loop
- [ ] Have a repeatable feature engineering workflow
- [ ] Know when to create a feature vs. when to let the algorithm learn

---

## Module 7: Capstone Project (Weeks 7–8)

**Goal:** Build an end-to-end project that demonstrates internship-ready skills.

### Why This Matters
Certificates are proof you watched videos. A project is proof you *can work*. Internship interviewers want to see a real problem solved: data → insight → prediction.

### Project Options

**Option A: Kaggle Competition (Beginner-Friendly)**
- Join a Getting Started competition (tabular data focus)
- Examples: Titanic, House Prices, Binary Classification competitions
- Timeline: 5–7 days
- **Scope:**
  - Data exploration & cleaning
  - Feature engineering (5+ features)
  - Multiple models (RF, XGBoost, maybe a simple Neural Net)
  - Model validation and tuning
  - Submission & competition ranking

**Option B: Real-World Dataset (Portfolio-Friendly)**
- Choose a dataset from Kaggle Datasets or Google Dataset Search
- Define a clear prediction task (e.g., "Predict customer churn," "Forecast weekly sales")
- Timeline: 10–14 days
- **Scope:** Same as competition, but you define the problem
- **Advantage:** Full control over framing; easier to write a compelling narrative

**Option C: Time-Series Forecasting (If Interested)**
- Load stock prices, weather, or sales data
- Build an ARIMA or XGBoost time-series model
- Forecast 30 days ahead
- Timeline: 7–10 days
- **Why:** Time-series is increasingly common in internships; this sets you apart

### Capstone Checklist

**Phase 1: Problem Definition & Exploration** (2–3 days)
- [ ] Define the prediction task (regression or classification?)
- [ ] Load and explore the data
  - [ ] Check shape, dtypes, missing values
  - [ ] Visualize distributions and correlations
  - [ ] Identify outliers
- [ ] Write a 2–3 sentence problem statement
- [ ] Document initial hypotheses (what features will matter?)

**Phase 2: Data Preparation** (2–3 days)
- [ ] Handle missing values (document your strategy)
- [ ] Encode categorical variables
- [ ] Create 5+ engineered features (log, interactions, aggregations, domain-specific)
- [ ] Scale numeric features if needed
- [ ] Document all preprocessing in code comments

**Phase 3: Model Building & Validation** (2–3 days)
- [ ] Train 3+ models (baseline, RF, XGBoost, etc.)
- [ ] Use cross-validation or train/validation split
- [ ] Compute 2+ evaluation metrics
- [ ] Create a model comparison table
- [ ] Analyze feature importance

**Phase 4: Interpretation & Insights** (1–2 days)
- [ ] Identify top 5 most important features
- [ ] Write 3–5 bullet points on what the model learned
- [ ] Identify model failures (where does it predict poorly?)
- [ ] Suggest future improvements

**Phase 5: Documentation** (1 day)
- [ ] Clean Jupyter notebook with markdown explanations
- [ ] No code cell without a brief explanation
- [ ] Summary section at top: problem, approach, key results
- [ ] README (if GitHub) or summary document

### Deliverables

1. **Jupyter Notebook** (~100–150 lines of substantive code)
   - Clean, commented, reproducible
   - Sections: EDA, preprocessing, modeling, evaluation, insights
   - Plots: distribution histograms, correlation heatmap, feature importance, prediction vs. actual

2. **GitHub Repository** (Optional but impressive for internship)
   - README with problem statement, data source, results
   - Notebook + data (if allowed by license)
   - `.gitignore` for large files
   - Clone-and-run workflow (clear instructions)

3. **Results Summary**
   - Best model: name, metric (MAE/accuracy), brief why
   - Top 5 features: feature name, importance, interpretation
   - Key insight: one sentence on what surprised you

### Success Criteria
- [ ] Code is clean and reproducible (someone else can run it)
- [ ] Feature engineering is thoughtful (5+ features, not random)
- [ ] Model comparison is rigorous (multiple algorithms, proper validation)
- [ ] Interpretation is sound (you understand *why* the model works)
- [ ] Documentation is professional (clear enough for a hiring manager to follow)

### Time Breakdown
- **Days 1–3:** EDA + problem definition + preprocessing
- **Days 4–5:** Feature engineering + baseline models
- **Days 6–7:** Model tuning + evaluation + interpretation
- **Days 8:** Documentation + cleanup

---

## Study Patterns & Habits

### Weekly Routine
- **Monday:** Review prior week's concepts for 15 min; set weekly goals
- **Tuesday–Thursday:** 2–3 hours focused learning per day (watch, code along)
- **Friday:** Build small practice project or work on capstone (consolidation)
- **Weekend:** Light review or exploration (no heavy work required)

### Learning Protocol
1. **Watch the course videos** (at 1.5x speed is fine)
2. **Pause and code along** with every example (don't just watch)
3. **Do every exercise** — they're not optional
4. **Break when stuck:** If a concept isn't clicking after 25 min, move on and return later
5. **Document patterns:** Keep a personal "ML recipe book" of working code snippets

### Your "Recipe Book" (Start Week 1)
Create a folder in your repo called `patterns/` with reusable scripts:
- `01_load_explore.py` — standard EDA template
- `02_handle_missing.py` — missing data strategies
- `03_encode_categorical.py` — one-hot, ordinal, target encoding
- `04_feature_engineering.py` — common transformations
- `05_train_eval.py` — train/validation split + metrics
- `06_model_comparison.py` — template to compare 3+ models

**Update it as you learn.** By week 8, it's your personal data science toolkit.

### Time Management Tips
- **Batch learning:** 3–4 hour sessions beat 1-hour scattered sessions
- **Context switching is toxic:** If you switch between SQL and Pandas every 20 min, nothing sticks
- **Practice first, theory second:** If a concept isn't clicking, code an example before re-reading the theory
- **Use the TLE mindset:** You already have accountability structure from CP. Reuse it: Monday/Friday check-ins on data science progress

---

## Internship Readiness Checklist

By the end of Week 8, you should be able to:

### Technical
- [ ] Load and explore a dataset in < 10 min (EDA)
- [ ] Handle missing data strategically (3+ methods)
- [ ] Write SQL queries to filter, join, and aggregate (no Googling)
- [ ] Create engineered features that improve model performance
- [ ] Train, validate, and compare tree-based models
- [ ] Compute and interpret feature importance
- [ ] Evaluate models with appropriate metrics (MAE, accuracy, etc.)
- [ ] Deploy a model to make predictions on new data

### Communication
- [ ] Explain your analysis in writing (why did you choose this approach?)
- [ ] Create plots that tell a story
- [ ] Discuss trade-offs (accuracy vs. interpretability, etc.)
- [ ] Defend your model choices to a technical audience

### Professional
- [ ] Have a portfolio project on GitHub
- [ ] Can clone someone's repo and run their code without errors
- [ ] Commit meaningful messages and document your work
- [ ] Understand when to use which model (not just "use the one with lowest MAE")

---

## Quick Reference: Key Formulas & Concepts

### Metrics (Regression)
- **MAE** = mean(|actual − predicted|)
- **RMSE** = √(mean((actual − predicted)²))
- **R²** = 1 − (SS_res / SS_tot) = fraction of variance explained

### Metrics (Classification)
- **Accuracy** = (TP + TN) / total
- **Precision** = TP / (TP + FP) = "of positives predicted, how many right?"
- **Recall** = TP / (TP + FN) = "of actual positives, how many caught?"

### Model Selection
- **Decision Tree:** Fast, interpretable, prone to overfitting
- **Random Forest:** Ensemble of trees, more robust, often good baseline
- **XGBoost:** State-of-the-art for tabular data, faster than RF, requires tuning
- **When to use which:**
  - Accuracy critical and data is large? → XGBoost
  - Need interpretability? → Decision Tree or RF
  - Quick baseline? → RF
  - Competing? → Ensemble (RF + XGBoost)

### Feature Engineering Red Flags
- Creating 50+ features and hoping some stick → Bad. Be intentional.
- High-cardinality one-hot encoding → Risk overfitting. Use target encoding.
- Leakage (using future info to predict past) → Ruins your model. Think causally.

---

## Troubleshooting & Common Pitfalls

### "My model has great train accuracy but terrible validation accuracy"
- **Diagnosis:** Overfitting. Model memorized training data.
- **Fix:** Use more regularization (lower `max_depth` in trees, higher `lambda` in XGBoost), more training data, or simpler model.

### "My model performs equally bad on train and validation"
- **Diagnosis:** Underfitting. Model is too simple.
- **Fix:** More features, deeper trees, longer training, better features.

### "Feature importance says my best feature only matters 5%"
- **Diagnosis:** Features are highly correlated; model can swap them.
- **Fix:** Check correlation matrix. Drop redundant features or use domain knowledge to pick the best one.

### "Encoding my categorical variable made things worse"
- **Diagnosis:** One-hot encoding exploded dimensionality, or target encoding leaked.
- **Fix:** Use target encoding carefully (only on training set), or drop the category if it's not predictive.

### "My SQL query times out"
- **Diagnosis:** Querying too much data or inefficient join.
- **Fix:** Add date filters, limit rows, check if JOIN key is indexed, use APPROXIMATE function for quick sampling.

---

## Resources Beyond Kaggle

- **Pandas docs:** https://pandas.pydata.org/docs (bookmark this)
- **scikit-learn docs:** Algorithms reference
- **Kaggle Datasets:** Endless practice datasets
- **Kaggle Competitions:** Learn from top solutions' kernels
- **Blogs:** Towards Data Science, Analytics Vidhya for deep-dives
- **Papers:** Once intermediate, read ML papers (arXiv) for bleeding-edge ideas

---

## Success Stories & Expectations

### What's Realistic
- By Week 4, you'll feel like you know *something* (it's real)
- By Week 6, you'll build a model that works (it will)
- By Week 8, you'll have a portfolio project you're proud of (you will)

### What's NOT Realistic
- Becoming an expert in 8 weeks (no one does)
- Memorizing every algorithm (internships don't demand this)
- Achieving top-10 Kaggle rankings (highly competitive; not necessary)

### Common Confidence Dips
- **Week 2:** SQL feels unintuitive. *You'll be fluent by week 4.*
- **Week 4:** XGBoost hyperparameters are overwhelming. *Defaults work 80% of the time.*
- **Week 6:** Feature engineering feels like guessing. *It gets more scientific with practice.*

---

## Accountability & Iteration

**Update this roadmap as you go:**
- Add a "Notes" section after each module
- Log what took longer than expected
- Record which exercises clicked and which didn't
- Update timings for future reference

**GitHub Structure (Recommended)**
```
datasci-kaggle-journey/
├── README.md (links to this SKILL.md)
├── 01-python/
│   └── exercises.ipynb
├── 02-sql/
│   └── bigquery_queries.sql
├── 03-pandas/
│   ├── exercises.ipynb
│   └── data_cleaning_script.py
├── 04-intro-ml/
│   └── first_models.ipynb
├── 05-intermediate-ml/
│   └── xgboost_experiments.ipynb
├── 06-feature-engineering/
│   └── feature_engineering.ipynb
├── 07-capstone/
│   ├── notebook.ipynb
│   ├── data/ (gitignore large files)
│   └── README.md (project summary)
└── patterns/
    ├── load_explore.py
    ├── handle_missing.py
    └── ... (your recipes)
```

---

## TL;DR — Start Here

1. **This week:** Skim Python, start SQL fundamentals. Deliverable: Python cert + first SQL query.
2. **Next week:** SQL mastery + Pandas basics. Deliverable: Data cleaning script.
3. **Weeks 3–5:** Deep Pandas, Intro ML, Intermediate ML. Deliverable: Working model on a Kaggle dataset.
4. **Weeks 6–8:** Feature engineering + Capstone. Deliverable: End-to-end portfolio project.

By Week 8, you'll be competitive for an internship. By Week 12, you'll be dangerous.

---

**Last Updated:** 2025-01-08  
**Status:** Ready for iteration. Update as you progress.
