#!/usr/bin/env python

import numpy as np
import statistics
import argparse

class GachaponSimulator:

    np.random.seed()
    results = []

    def __init__(self, prizes_n):
        self.prizes_n = prizes_n  # integer
        self.results = []
        self.summary = {}
        self.one_sim = ()


    def _simulate_once(self):
        sim_results = []
        gachapon_list = list(range(0, self.prizes_n))
        while all(item in sim_results for item in gachapon_list) is False:
            add_number = np.random.randint(0, self.prizes_n)
            sim_results.append(add_number)
        else:
            self.one_sim = len(sim_results)
            return self.one_sim


    def reset(self):
            self.results = []
            return self.results


    def simulate(self, num_games):
        for i in range(num_games):
            iteration = GachaponSimulator._simulate_once(self)
            self.results.append(iteration)
        return self.results


    def get_summary_stats(self):
        global mean
        global stdev
        if not self.results:
            mean = None
            stdev = None
        elif len(self.results) == 1:
            mean = self.results[0]
            stdev = None
        else:
            mean = sum(self.results)/len(self.results)
            stdev = statistics.stdev(self.results)
        self.summary = {'n': len(self.results),
                        'mean': mean,
                        'stdev': stdev}
        return self.summary

parser = argparse.ArgumentParser()
parser.parse_args()