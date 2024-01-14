import pandas as pd
import numpy as np
import random
import ipaddress

num_samples = 1000

data = {
    'Bandwidth (Mbps)': np.random.normal(80, 10, num_samples),
    'PacketCount': np.random.randint(200, 500, num_samples),
    'Latency (ms)': np.random.normal(10, 5, num_samples),
    'SourceIP': [str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1))) for _ in range(num_samples)],
    'DestinationIP': [str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1))) for _ in range(num_samples)],
    'Protocol': [random.choice(['TCP', 'UDP', 'HTTP', 'DNS']) for _ in range(num_samples)],
    'TrafficCongestion': np.random.normal(70, 15, num_samples),
    'CPULoad': np.random.normal(80, 15, num_samples),
    'MemoryLoad': np.random.normal(90, 10, num_samples)
}

# Modify anomaly introduction logic for specific features
latency_anomaly_indices = random.sample(range(num_samples), num_samples // 200)
for idx in latency_anomaly_indices:
    data['Latency (ms)'][idx] = np.random.normal(70, 5)

packet_anomaly_indices = random.sample(range(num_samples), num_samples // 120)
for idx in packet_anomaly_indices:
    data['PacketCount'][idx] = np.random.normal(800, 100)

traffic_anomaly_indices = random.sample(range(num_samples), num_samples // 100)
for idx in traffic_anomaly_indices:
    data['TrafficCongestion'][idx] = np.random.normal(240, 40)

bandwidth_anomaly_indices = random.sample(range(num_samples), num_samples // 150)
for idx in bandwidth_anomaly_indices:
    data['Bandwidth (Mbps)'][idx] = np.random.normal(200, 20)


cpuload_anomaly_indices = random.sample(range(num_samples), num_samples // 100)
for idx in cpuload_anomaly_indices:
    data['CPULoad'][idx] = np.random.normal(150, 15)

memoryload_anomaly_indices = random.sample(range(num_samples), num_samples // 200)
for idx in memoryload_anomaly_indices:
    data['MemoryLoad'][idx] = np.random.normal(250, 10)

anomaly_indices = []
anomaly_indices.extend(latency_anomaly_indices)
anomaly_indices.extend(packet_anomaly_indices)
anomaly_indices.extend(traffic_anomaly_indices)
anomaly_indices.extend(bandwidth_anomaly_indices)
anomaly_indices.extend(cpuload_anomaly_indices)
anomaly_indices.extend(memoryload_anomaly_indices)
data['Anomaly'] = [1 if i in anomaly_indices else 0 for i in range(num_samples)]

df = pd.DataFrame(data)

df.to_csv('network_anomaly_data.csv', index=False)

print("The Dataset is generated.")




