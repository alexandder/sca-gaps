import sys

from calculate_results import find_wrong_estimation_ratio, get_intervals_for_simulations, find_max_error, \
    find_max_distance


def estimate_all_rules(rule, alphas):

    for r1 in [int(rule)]:
        for r2 in range(0, 256):
            if r1 != r2:
                f = open("logs99/" + str(r2) + ".out", 'w')
                f.write(
                    "alpha, r1, r2, filling success rate, n_gaps, n_failures, n_top_gaps, n_bottom_gaps, success_rate_bottom, n_gaps_random, % random gaps")
                f.write("\n")
                for a in alphas:
                    get_intervals_for_simulations(f, r1, r2, a, 15)
                f.close()



def main():
    rule = sys.argv[1]
    alphas = [0.1, 0.2, 0.3, 0.4]

    estimate_all_rules(rule, alphas)

if __name__ == "__main__":
    main()
