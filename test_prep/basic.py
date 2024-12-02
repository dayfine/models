import random

def _prob(high_freq, low_freq) -> bool:
    # High frequency problems are 10 times more likely to appear
    hi_prob = high_freq * 10
    lo_prob = low_freq 
    return random.random() < hi_prob / (hi_prob + lo_prob)


def num_success():
    num_success = 0
    num_high_freq_q = 25
    num_low_freq_q = 250

    for _ in range(5):
        is_high_freq_q = _prob(num_high_freq_q, num_low_freq_q)
        if is_high_freq_q:
            num_high_freq_q -= 1
        else:
            num_low_freq_q -= 1
        
        num_success += random.random() < (0.6 if is_high_freq_q else 0.35)

    return num_success

ns = []
for i in range(10000):
    n = num_success()
    ns.append(n)

print("Num passes: ", sum(1 for n in ns if n >=4))
