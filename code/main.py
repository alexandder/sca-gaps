from calculate_results import find_wrong_estimation_ratio, get_intervals_for_simulations, find_max_error, \
    find_max_distance

def estimate_all_rules(alphas):
    print("alpha, r1, r2, max_err, wrong_ration, max_dist, match, filling success rate")
    for r1 in [204]:
        for r2 in range(256):
            if r1 != r2:
                for a in alphas:
                    intervals, match, success_rates = get_intervals_for_simulations(r1, r2, a)
                    print(a, r1, r2, find_max_error(intervals, a),
                          find_wrong_estimation_ratio(intervals, a),
                          find_max_distance(intervals, a),
                          match, sum(success_rates) / len(success_rates))


rule1 = 0
rule2 = 16
alpha = 0.25
alphas = [0.1, 0.2, 0.3, 0.4]

estimate_all_rules(alphas)