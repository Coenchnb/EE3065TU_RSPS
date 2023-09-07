years = 5
EHV_length = 2310
HV_length = 3329
EHV_failures = 25
HV_failures = 51

def FailureFrequency(length, failures, years):
    failure_freq = failures/(length*years)
    return failure_freq

EHV_ffreq = FailureFrequency(EHV_length, EHV_failures, years)
HV_ffreq = FailureFrequency(HV_length, HV_failures, years)
Combined_ffreq = FailureFrequency(EHV_length+HV_length, EHV_failures+HV_failures, years)

EHV_MTBF = 1/EHV_ffreq
HV_MTBF = 1/HV_ffreq
Combined_MTBF = 1/Combined_ffreq

print("EHV: ", EHV_ffreq)
print("HV: ", HV_ffreq)
print("Combined failure frequency: ", Combined_ffreq)
print("MTBF values:", EHV_MTBF, "and ", HV_MTBF)
print("Combined MTBF: ", Combined_MTBF)

#I made a comment here