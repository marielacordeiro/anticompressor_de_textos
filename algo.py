import time
import os

def anticompressor(test_case: str):
    substitution_table_list = []
    substitution_table = {}
    all_letters = set()
    with open(f'casos/{test_case}') as f:
        for line in f:
            k_v = line.split()
            if len(k_v) < 2:
                continue
            k, v = k_v
            substitution_table_list.append((k, v))
            all_letters.update(*set(v))

    first_letter = ''
    for k, v in substitution_table_list:
        substitution_table[k] = v
        if first_letter == '' and k not in all_letters:
            first_letter = k

    del all_letters
    del substitution_table_list

    value_cache = {}
    def calc_entry_value(entry: str) -> int:
        total_val = 0
        if entry in value_cache:
            return value_cache[entry]
        entry = substitution_table.get(entry, entry)
        for char in entry:
            if char == entry:
                return 1
            val = calc_entry_value(char)
            value_cache[char] = val
            total_val += val
        return total_val
        
    return calc_entry_value(first_letter), first_letter

exec_times = {}
results = {}
for _ in range(1000):
    for file in os.listdir('casos'):
        if file not in exec_times:
            exec_times[file] = []
        start_time = time.time()
        res, first_letter = anticompressor(file)
        exec_times[file].append(time.time() - start_time)
        if file not in results:
            results[file] = (res, first_letter)

for f, t in exec_times.items():
    _time = sum(t) / len(t)
    exec_times[f] = _time

print()
[print(f'{k} = tempo: {v} \t tamanho: {results[k][0]:<18} \t primeira letra: {results[k][1]}') for k, v in exec_times.items()]
print()
