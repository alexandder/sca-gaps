import binomial_distribution as bin
import simulations as simulations
import fill_gaps as gaps
import lib.ca_data as ca_data

def get_intervals_for_simulations(rule1, rule2, alpha):
    result = []
    rules_matched = 'MATCH'
    success_rates = []
    for i in range(10):
        total_num, all_simulations, all_simulations_with_gaps = simulations.perform_simulations(5, rule1, rule2, alpha, 49, 49, 0.05)
        P = simulations.find_probabilities(total_num)
        filled_simulations = gaps.fill_gaps_for_all_simulations(all_simulations_with_gaps, P)
        total_number_of_gaps = get_total_number_of_gaps(all_simulations_with_gaps)
        total_number_of_failures = get_number_of_failures(all_simulations, filled_simulations)
        if total_number_of_gaps == 0:
            success_rates.append(1.0)
        else:
            success_rate = 1 - (total_number_of_failures/total_number_of_gaps*1.0)
            success_rates.append(success_rate)
        match = estimate_rules(P, rule1, rule2)
        alpha_L, alpha_U = calculate_confidence_interval(P, total_num)
        interval = {'alpha_L': alpha_L, 'alpha_U': alpha_U}
        result.append(interval)
        if match == 'NO_MATCH':
            rules_matched = match
    return result, rules_matched, success_rates

def calculate_confidence_interval(P, total_number_of_neighborhoods):
    nei_for_p_less_than_half = []
    nei_for_p_greater_than_half = []
    for nei in ca_data.elementary_neighborhoods:
        if 0 < P[nei] < 0.5:
            nei_for_p_less_than_half.append(nei)
        elif 0.5 < P[nei] < 1.0:
            nei_for_p_greater_than_half.append(nei)
    N_STAR_less_than = 0
    for nei in nei_for_p_less_than_half:
        N_STAR_less_than += total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0']
    N_STAR_greater_than = 0
    for nei in nei_for_p_greater_than_half:
        N_STAR_greater_than += total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0']

    N_STAR = N_STAR_greater_than + N_STAR_less_than

    K_STAR = 0
    for nei in nei_for_p_greater_than_half:
        K_STAR += total_number_of_neighborhoods[nei]['0']
    for nei in nei_for_p_less_than_half:
        K_STAR += total_number_of_neighborhoods[nei]['1']

    if K_STAR != 0 and N_STAR != 0:
        alpha_L, alpha_U = bin.calcBin(K_STAR, N_STAR)
        return alpha_L, alpha_U
    return 0, 0

def get_number_of_failures(all_simulations, all_filled_simulations):
    total_number_of_failures = 0
    for i in range(len(all_simulations)):
        for j in range(len(all_simulations[i])):
            for k in range(len(all_simulations[i][j])):
                if all_filled_simulations[i][j][k] != all_simulations[i][j][k]:
                    total_number_of_failures += 1
    return total_number_of_failures

def get_total_number_of_gaps(all_simulations_with_gaps):
    total_number_of_gaps = 0
    for i in range(len(all_simulations_with_gaps)):
        for j in range(len(all_simulations_with_gaps[i])):
            for k in range(len(all_simulations_with_gaps[i][j])):
                if all_simulations_with_gaps[i][j][k] == -1:
                    total_number_of_gaps += 1
    return total_number_of_gaps

def find_max_error(intervals, alpha):
    result = 0
    for interval in intervals:
        alpha_dash = (interval['alpha_L'] + interval['alpha_U']) / 2
        error = abs(alpha - alpha_dash) / abs(alpha)
        if error > result:
            result = error
    return result

def is_alpha_not_in_interval(interval, alpha):
    return interval['alpha_L'] > alpha or interval['alpha_U'] < alpha

def find_wrong_estimation_ratio(intervals, alpha):
    count = 0
    for interval in intervals:
        if is_alpha_not_in_interval(interval, alpha):
            count += 1
    return 1.0*count/len(intervals)

def find_max_distance(intervals, alpha):
    result = 0
    for interval in intervals:
        distance = 0
        if is_alpha_not_in_interval(interval, alpha):
            if interval['alpha_L'] > alpha:
                distance = abs(interval['alpha_L'] - alpha)
            else:
                distance = abs(interval['alpha_U'] - alpha)
        if distance > result:
            result = distance
    return result

def estimate_rules(P, rule1, rule2):
    rule1_est = []
    rule2_est = []
    for nei in P:
        if P[nei] == 0:
            rule1_est.append('0')
            rule2_est.append('0')
        elif P[nei] == 1:
            rule1_est.append('1')
            rule2_est.append('1')
        elif 0 < P[nei] < 0.5:
            rule1_est.append('1')
            rule2_est.append('0')
        else:
            rule1_est.append('0')
            rule2_est.append('1')
    if int(''.join(rule1_est), 2) == rule1 and int(''.join(rule2_est), 2) == rule2:
        return 'MATCH'
    else:
        return 'NO_MATCH ' + str(int(''.join(rule1_est), 2)) + ' ' + str(int(''.join(rule2_est), 2))