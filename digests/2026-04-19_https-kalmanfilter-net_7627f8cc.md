---
url: https://kalmanfilter.net
title: https://kalmanfilter.net
scraped_at: '2026-04-19T20:08:21Z'
word_count: 4361
raw_file: raw/2026-04-19_https-kalmanfilter-net_7627f8cc.txt
tldr: This page is a worked introduction to the Kalman Filter, using a one-dimensional radar-tracking example to show how prediction, measurement update, Kalman gain, and covariance tracking work together.
key_quote: “If you can't explain it simply, you don't understand it well enough.”
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Albert Einstein
- Peter Joseph
tools:
- MATLAB
- Python
libraries:
- numpy.linalg
companies: []
tags:
- kalman-filter
- state-estimation
- sensor-fusion
- radar-tracking
- uncertainty-propagation
---

### TL;DR
This page is a worked introduction to the Kalman Filter, using a one-dimensional radar-tracking example to show how prediction, measurement update, Kalman gain, and covariance tracking work together.

### Key Quote
“If you can't explain it simply, you don't understand it well enough.”

### Summary
- The page introduces the **Kalman Filter** as an algorithm for **estimating and predicting system state under uncertainty**, especially when measurements are noisy or the system is affected by unknown external factors.
- It frames the filter as useful for:
  - **Object tracking**
  - **Navigation**
  - **Robotics**
  - **Control**
  - Also mentions **financial market analysis** and **weather prediction**
- The author’s teaching approach is explicitly **example-first**:
  - This page is the **single-page overview**
  - There is a **free online tutorial**
  - There is a book, **“Kalman Filter from the Ground Up”**, with **14 fully solved numerical examples**, plots, tables, and advanced topics like **Extended Kalman Filter**, **Unscented Kalman Filter**, **sensor fusion**, and implementation guidance

#### Core idea
- The filter combines:
  - a **dynamic model** for how the system evolves over time
  - **measurements** from sensors
  - **uncertainty estimates** for both
- It uses these to produce:
  - a **current estimate**
  - a **prediction of the next state**
  - associated **covariance/uncertainty**

#### Radar tracking example
- The main example is a **1D radar tracking an aircraft**
- State variables:
  - range \(r\)
  - velocity \(v\)
- State vector:
  - \(\boldsymbol{x} = [r, v]^T\)
- Initial measurement at \(t_0\):
  - range = **10,000 m**
  - velocity = **200 m/s**
- Initial measurement covariance:
  - \(\boldsymbol{R}_0 = \begin{bmatrix}16 & 0 \\ 0 & 0.25\end{bmatrix}\)
  - corresponds to standard deviations of **4 m** for range and **0.5 m/s** for velocity

#### Prediction step
- Assumes a **constant velocity model**
- State transition matrix:
  - \(\boldsymbol{F} = \begin{bmatrix}1 & \Delta t \\ 0 & 1\end{bmatrix}\)
- With \(\Delta t = 5\) s:
  - predicted state at \(t_1\): **11,000 m**, **200 m/s**
- Covariance prediction uses:
  - \(\boldsymbol{P}_{n+1,n} = \boldsymbol{F}\boldsymbol{P}_{n,n}\boldsymbol{F}^T\)
- Then process noise is added:
  - \(\boldsymbol{P}_{n+1,n} = \boldsymbol{F}\boldsymbol{P}_{n,n}\boldsymbol{F}^T + \boldsymbol{Q}\)
- Process noise is explained as uncertainty from factors like **wind** or other unmodeled accelerations
- Example process noise:
  - \(\sigma_a = 0.2\,m/s^2\)
  - \(\boldsymbol{Q} = \begin{bmatrix}6.25 & 2.5 \\ 2.5 & 1\end{bmatrix}\)
- Final predicted covariance after adding process noise:
  - \(\boldsymbol{P}_{1,0} = \begin{bmatrix}28.5 & 3.75 \\ 3.75 & 1.25\end{bmatrix}\)

#### Update step
- A second measurement at \(t_1\) is introduced:
  - \(\boldsymbol{z}_1 = [11020, 202]^T\)
- This measurement is noisier:
  - range std dev = **6 m**
  - velocity std dev = **1.5 m/s**
  - \(\boldsymbol{R}_1 = \begin{bmatrix}36 & 0 \\ 0 & 2.25\end{bmatrix}\)
- The filter does **not** simply choose measurement or prediction
- Instead it computes a **weighted combination** using the **Kalman Gain**
- The innovation/residual is:
  - \(\boldsymbol{z}_1 - \boldsymbol{H}\hat{\boldsymbol{x}}_{1,0}\)
- In this example, \(\boldsymbol{H} = \boldsymbol{I}\), so state and measurement domains are the same

#### Kalman gain
- One-dimensional form:
  - \(K_n = \frac{p_{n,n-1}}{p_{n,n-1}+r_n}\)
- Multivariate form:
  - \(\boldsymbol{K}_n = \boldsymbol{P}_{n,n-1}\boldsymbol{H}^T(\boldsymbol{H}\boldsymbol{P}_{n,n-1}\boldsymbol{H}^T+\boldsymbol{R}_n)^{-1}\)
- For the example, the gain is:
  - \(\boldsymbol{K}_1 = \begin{bmatrix}0.4048 & 0.6377 \\ 0.0399 & 0.3144\end{bmatrix}\)

#### Updated estimate
- Innovation:
  - \([11020, 202]^T - [11000, 200]^T = [20, 2]^T\)
- Correction:
  - \(\boldsymbol{K}_1 [20, 2]^T = [9.37, 1.43]^T\)
- Updated state:
  - \(\hat{\boldsymbol{x}}_{1,1} = [11009.37, 201.43]^T\)

#### Updated covariance
- The page presents both:
  - the **Joseph form**:
    - \((\boldsymbol{I}-\boldsymbol{K}\boldsymbol{H})\boldsymbol{P}(\boldsymbol{I}-\boldsymbol{K}\boldsymbol{H})^T+\boldsymbol{K}\boldsymbol{R}\boldsymbol{K}^T\)
  - and the **simplified form**:
    - \((\boldsymbol{I}-\boldsymbol{K}\boldsymbol{H})\boldsymbol{P}\)
- It notes the **Joseph form is more numerically stable** for implementation
- Updated covariance in the example:
  - \(\boldsymbol{P}_{1,1} = \begin{bmatrix}14.57 & 1.43 \\ 1.43 & 0.71\end{bmatrix}\)
- This is lower uncertainty than both:
  - the prediction covariance
  - the measurement covariance

#### What the example is trying to teach
- The Kalman Filter works as a **predict-update loop**
- It:
  - initializes from the first measurement
  - predicts forward with the motion model
  - updates using the next measurement
  - repeats continuously
- The page emphasizes that:
  - uncertainty naturally grows during prediction
  - new measurements reduce uncertainty
  - the gain balances trust between prediction and measurement based on their covariances

#### Practical notes included
- Matrix inversion is shown with:
  - MATLAB: `inv(A)` or preferably `A\b`
  - Python: `numpy.linalg.inv(A)` or preferably `numpy.linalg.solve(A, b)`
- It explicitly recommends **solving linear systems directly rather than explicitly computing inverses**

### Assessment
Durability is **high** because the page teaches a classic Kalman Filter formulation that is broadly timeless, though a few implementation references and book/course pointers are tied to this site’s ecosystem. The content type is **tutorial/reference**, with a strong tutorial flavor and equation-heavy reference sections. Density is **high**: it packs many formulas, definitions, and a full numeric walkthrough into a single page. Originality is **primary source** in the sense that it is the author’s own instructional presentation, not an aggregation, though it draws on standard Kalman Filter theory. Reference style is best as **refer-back** for equations and worked examples, or **deep-study** if learning the filter from scratch. Scrape quality is **good overall**: the main text, equations, and example calculations are present, but the page clearly references figures and sections that are not included here, so some visual aids and linked supporting material are missing.
