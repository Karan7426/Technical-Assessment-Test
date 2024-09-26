from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable) -> Dict:
    grouped_data = {}

    
    for entry in data:
        
        key_value = entry.get(key)
        if key_value is not None:
            if key_value not in grouped_data:
                grouped_data[key_value] = []
            grouped_data[key_value].append(entry)

   
    aggregated_result = {}
    for k, values in grouped_data.items():
        aggregated_result[k] = aggregator(values)

    return aggregated_result
