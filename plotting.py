import json
import matplotlib.pyplot as plt
import numpy as np


def normalize_data(data):
    max_value = max(data)
    return [x / max_value for x in data]


def load_data(strategy):
    with open(f'{strategy}_data.json', 'r') as f:
        data = json.load(f)
    time_taken = normalize_data(data['time_taken'])
    array_sizes = normalize_data(data['array_sizes'])
    return time_taken, array_sizes


def plot_data(strategies):
    plt.figure(figsize=(12, 6))

    for strategy in strategies:
        time_taken, array_sizes = load_data(strategy)
        plt.plot(array_sizes, time_taken, label=f'Strategy {strategy}')

    plt.xlabel('Normalized Array Size')
    plt.ylabel('Normalized Time Taken')
    plt.title('Performance Comparison of Different Strategies')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    strategies = ['A', 'B', 'C']
    plot_data(strategies)
