import binomial_distribution as bin
import simulations as simulations
import fill_gaps as gaps
import ca_data as ca_data


def find_probabilistic_lookup_table(rule1, rule2, estimated_alpha):
    result = {"111": 0, "110": 0, "101": 0, "100": 0, "011": 0, "010": 0, "001": 0, "000": 0}
    binary_rule1 = format(rule1, "#010b")[2:]
    binary_rule2 = format(rule2, "#010b")[2:]
    for i in range(len(binary_rule1)):
        if binary_rule1[i] == str(0) and binary_rule2[i] == str(0):
            result[ca_data.elementary_neighborhoods[7 - i]] = 0
        elif binary_rule1[i] == str(1) and binary_rule2[i] == str(1):
            result[ca_data.elementary_neighborhoods[7 - i]] = 1
        elif binary_rule1[i] == str(1) and binary_rule2[i] == str(0):
            result[ca_data.elementary_neighborhoods[7 - i]] = estimated_alpha
        else:
            result[ca_data.elementary_neighborhoods[7 - i]] = 1 - estimated_alpha
    return result


def fill_simulations(rule1, rule2, estimated_alpha, all_simulations, all_simulations_with_gaps):
    estimated_P = find_probabilistic_lookup_table(rule1, rule2, estimated_alpha)
    filled_simulations, gaps_filled_from_top, gaps_filled_from_bottom, gaps_filled_randomly = gaps.fill_gaps_for_all_simulations(rule1, rule2, all_simulations_with_gaps, estimated_P, estimated_alpha)
    number_of_gaps = get_total_number_of_gaps(all_simulations_with_gaps)
    number_of_failures = get_number_of_failures(all_simulations, filled_simulations)
    return number_of_gaps, number_of_failures, gaps_filled_from_top, gaps_filled_from_bottom, gaps_filled_randomly


def get_intervals_for_simulations(rule1, rule2, alpha, number_of_repetitions):
    intervals = []
    rules_matched = 'MATCH'
    success_rates = []
    total_gaps_filled_from_top = 0
    total_gaps_filled_from_bottom = 0
    total_gaps_filled_randomly = 0
    total_gaps = 0
    total_number_of_failures = 0
    for i in range(number_of_repetitions):
        number_of_neighborhoods_dict, all_simulations, all_simulations_with_gaps = simulations.perform_simulations(rule1, rule2, alpha, 49, 49, 0.05)
        P = simulations.find_probabilities(number_of_neighborhoods_dict)
        match = estimate_rules(P, rule1, rule2)
        alpha_L, alpha_U = calculate_confidence_interval(P, number_of_neighborhoods_dict)
        interval = {'alpha_L': alpha_L, 'alpha_U': alpha_U}
        intervals.append(interval)
        if match == 'NO_MATCH':
            rules_matched = match
        estimated_alpha = (alpha_L + alpha_U)/2
        number_of_gaps, number_of_failures, gaps_filled_from_top, gaps_filled_from_bottom, gaps_filled_randomly = fill_simulations(rule1, rule2, estimated_alpha, all_simulations, all_simulations_with_gaps)
        total_gaps += number_of_gaps
        total_gaps_filled_from_top += gaps_filled_from_top
        total_gaps_filled_from_bottom += gaps_filled_from_bottom
        total_gaps_filled_randomly += gaps_filled_randomly
        total_number_of_failures += number_of_failures
        if number_of_gaps == 0:
            success_rates.append(1.0)
        else:
            success_rate = 1 - (number_of_failures / number_of_gaps * 1.0)
            success_rates.append(success_rate)
    return intervals, rules_matched, success_rates, total_gaps, total_number_of_failures,\
           total_gaps_filled_from_top, total_gaps_filled_from_bottom, total_gaps_filled_randomly

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