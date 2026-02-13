"""
Utility functions for A/B Test Analysis
"""

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint


def calculate_sample_size(baseline_rate, mde, alpha=0.05, power=0.80):
    """Calculate required sample size for A/B test"""
    from statsmodels.stats.power import zt_ind_solve_power
    from statsmodels.stats.proportion import proportion_effectsize
    
    treatment_rate = baseline_rate * (1 + mde)
    effect_size = proportion_effectsize(baseline_rate, treatment_rate)
    
    sample_size = zt_ind_solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1.0,
        alternative='two-sided'
    )
    
    return int(np.ceil(sample_size))


def two_proportion_ztest(conversions_a, total_a, conversions_b, total_b, alpha=0.05):
    """Perform two-proportion z-test"""
    counts = np.array([conversions_a, conversions_b])
    nobs = np.array([total_a, total_b])
    
    z_stat, p_value = proportions_ztest(counts, nobs, alternative='two-sided')
    
    rate_a = conversions_a / total_a
    rate_b = conversions_b / total_b
    
    ci_a = proportion_confint(conversions_a, total_a, alpha=alpha, method='wilson')
    ci_b = proportion_confint(conversions_b, total_b, alpha=alpha, method='wilson')
    
    absolute_lift = rate_a - rate_b
    relative_lift = (rate_a - rate_b) / rate_b if rate_b != 0 else np.nan
    
    return {
        'z_statistic': z_stat,
        'p_value': p_value,
        'significant': p_value < alpha,
        'rate_a': rate_a,
        'rate_b': rate_b,
        'ci_a': ci_a,
        'ci_b': ci_b,
        'absolute_lift': absolute_lift,
        'relative_lift': relative_lift
    }


def cohens_h(p1, p2):
    """Calculate Cohen's h effect size for two proportions"""
    phi1 = 2 * np.arcsin(np.sqrt(p1))
    phi2 = 2 * np.arcsin(np.sqrt(p2))
    return phi1 - phi2
