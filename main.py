
def count_batteries_by_health(present_capacities):
  counts= {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for capacity in present_capacities:
    soh_percentage = calculate_soh(capacity)
    classification = classify_battery(soh_percentage)
    counts[classification] += 1
  return counts
def calculate_soh(capacity, rated_capacity=120):
    '''Calculate soh percentage'''
    return (capacity / rated_capacity) * 100

def classify_battery(soh_percentage):
    '''Classifying batteries based on SoH percentage'''
    if soh_percentage > 80:
        return "healthy"
    elif 62 <= soh_percentage <= 80:
        return "exchange"
    else:
        return "failed"

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
