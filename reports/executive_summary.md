# Executive Summary: Ads vs Public Service Announcements

**Analyst:** Jordan Shamukiga · **Data:** Kaggle Marketing A/B Testing (588,101 real users)

## Bottom line
The data shows a 43.1% relative lift in conversion for users shown ads (2.55%) over users shown public service announcements (PSAs, 1.79%). With 588,101 users the difference is not plausibly chance (p < 0.001). Ads should replace PSAs, provided a conversion is worth more than the extra ad cost per converted user.

## What was tested
- 564,577 users saw ads; 23,524 saw PSAs (a 96/4 split, with PSAs as the small control group).
- Outcome: whether the user converted.
- Intended allocation: not documented (the dataset description says only that most users saw ads), so sample ratio mismatch can't be verified.
- Checks before testing: no duplicate users; group sizes reviewed.

## Results
| Group | Users | Conversions | Rate |
|---|---|---|---|
| Ads | 564,577 | 14,423 | 2.55% |
| PSAs | 23,524 | 420 | 1.79% |

Absolute difference: 0.77 percentage points. Two-proportion z-test: z = 7.37, p < 0.001. Cohen's h = 0.053, a small effect in absolute terms.

## Exploratory segments (not randomized)
Users who saw more ads converted far more often: 13–17% of ad-group users in the medium, high and very-high engagement groups versus about 1% in the low group, and the ad group beat the PSA group at every level. Ad exposure was not randomized, so this shows where conversions happen, not that more ads cause more conversions.

## Caveats
- The PSA group is small (4% of users), so its rate is less precise than the ad group's.
- The data has conversions only; revenue per conversion and ad cost are not included.
- A novelty effect is possible; watch conversion after rollout.

## Recommendation
Move PSA inventory to ads, keep a small holdout (for example 5%) for three months to confirm the lift holds, and add revenue per conversion to the next test so the decision can be made in dollars.
