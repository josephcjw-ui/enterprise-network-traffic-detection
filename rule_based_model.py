import pandas as pd

def classify_traffic(row):
    """
    Rule-based traffic classification demo.
    This is a simplified version for project presentation.
    """

    flow_duration = row.get("Flow Duration", 0)
    flow_iat_mean = row.get("Flow IAT Mean", 0)
    total_fwd_packets = row.get("Total Fwd Packets", 0)
    total_backward_packets = row.get("Total Backward Packets", 0)
    syn_flag_count = row.get("SYN Flag Count", 0)
    ack_flag_count = row.get("ACK Flag Count", 0)

    # Rule 1: DoS / DDoS
    if flow_duration < 200 and flow_iat_mean < 50:
        return "DoS-DDoS"

    # Rule 2: PortScan
    if total_fwd_packets < 3 and total_backward_packets < 3:
        return "PortScan"

    # Rule 3: BruteForce
    if syn_flag_count > 0 and ack_flag_count > 0:
        return "BruteForce"

    return "Benign"


def main():
    # Demo sample data
    data = [
        {
            "Flow Duration": 100,
            "Flow IAT Mean": 20,
            "Total Fwd Packets": 10,
            "Total Backward Packets": 8,
            "SYN Flag Count": 1,
            "ACK Flag Count": 1
        },
        {
            "Flow Duration": 5000,
            "Flow IAT Mean": 1000,
            "Total Fwd Packets": 1,
            "Total Backward Packets": 1,
            "SYN Flag Count": 0,
            "ACK Flag Count": 0
        }
    ]

    df = pd.DataFrame(data)
    df["Predicted"] = df.apply(classify_traffic, axis=1)

    print(df[["Flow Duration", "Flow IAT Mean", "Predicted"]])


if __name__ == "__main__":
    main()
