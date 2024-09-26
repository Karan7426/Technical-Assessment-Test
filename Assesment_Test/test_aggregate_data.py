from aggregate_data import aggregate_data

def sum_aggregator(entries):
    return sum(entry['value'] for entry in entries)

data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 5},
    {'category': 'B', 'value': 15},
]

result = aggregate_data(data, 'category', sum_aggregator)
print(result)   