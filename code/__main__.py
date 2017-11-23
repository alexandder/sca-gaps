import sys

from calculate_results import find_wrong_estimation_ratio, get_intervals_for_simulations, find_max_error, \
    find_max_distance


def estimate_all_rules(rule, alphas):
    print("alpha, r1, r2, max_err, wrong_ration, max_dist, match, filling success rate, "
          "n_gaps, n_failures, n_top_gaps, n_bottom_gaps, success_rate_bottom, n_gaps_random, % random gaps")
    for r1 in [int(rule)]:
        for r2 in range(0, 256):
            if r1 != r2:
                for a in alphas:
                    intervals, match, success_rates, total_gaps, total_number_of_failures, \
                    total_gaps_filled_from_top, total_gaps_filled_from_bottom, total_gaps_filled_from_randomly = get_intervals_for_simulations(r1, r2, a, 20)
                    average_success_rate = 1 - (1.0 * total_number_of_failures / total_gaps)
                    success_rate_for_nondeterministic_gaps = 1 - (1.0*total_number_of_failures/total_gaps_filled_from_bottom)
                    ratio_random_gaps = 1.0*total_gaps_filled_from_randomly/total_gaps_filled_from_bottom
                    print(a, r1, r2, find_max_error(intervals, a),
                          find_wrong_estimation_ratio(intervals, a),
                          find_max_distance(intervals, a),
                          match, average_success_rate, total_gaps, total_number_of_failures,
                          total_gaps_filled_from_top, total_gaps_filled_from_bottom,
                          success_rate_for_nondeterministic_gaps, total_gaps_filled_from_randomly, ratio_random_gaps)


def main():
    rule = sys.argv[1]
    alphas = [0.1, 0.2, 0.3, 0.4]

    estimate_all_rules(rule, alphas)

if __name__ == "__main__":
    main()
