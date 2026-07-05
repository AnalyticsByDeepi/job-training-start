# -----------------------------------------
# Name: Deepika M
# Date: 10-07-2026
# File: Session-8.py
# -----------------------------------------

# ==========================
# Task - 1
# The Multi-Vector Firewall
# ==========================

def analyze_traffic(source_name, *ips, **metadata):
    """
    Analyze network traffic from a source.

    LEGB Lookup:
        - source_name, ips, and metadata are Local variables because they
          are function parameters.
        - If a variable is not found locally, Python searches the Enclosing,
          Global, and finally Built-in scopes (LEGB rule).

    Args:
        source_name (str): Name of the traffic source.
        *ips (str): Variable number of IP addresses.
        **metadata: Security-related keyword arguments.

    Returns:
        None
    """

    print(f"Source: {source_name}")
    print(f"Analyzed {len(ips)} IPs")

    if metadata:
        tags = ", ".join(metadata.keys())
        print(f"Security Tags: {tags}")
    else:
        print("Security Tags: None")


# Test Cases
if __name__ == "__main__":

    print("===== Task - 1 =====")

    print("\nTest Case 1")
    analyze_traffic(
        "Mainframe_A",
        "192.168.1.1",
        "10.0.0.5",
        "172.16.0.1",
        threat_level="High",
        protocol="SSH"
    )

    print("\nTest Case 2")
    analyze_traffic(
        "Firewall_B",
        "192.168.100.10"
    )

    print("\nTest Case 3")
    analyze_traffic(
        "Gateway_C",
        threat_level="Low",
        encryption_type="AES-256",
        protocol="HTTPS"
    )

# ==========================
# Task - 2
# The Instant Payload Decoder
# ==========================

def decode_payload(payload):
    """
    Decode network payload using map() and a lambda function.

    LEGB Lookup:
        - payload is a Local variable inside this function.
        - The lambda function accesses payload values from the Local scope.
        - If a variable is not found locally, Python searches the
          Enclosing, Global, and Built-in scopes (LEGB rule).

    Args:
        payload (list): List of integer payload values.

    Returns:
        list: Decoded payload values.
    """

    return list(
        map(
            lambda number: number * 2 if number % 2 == 0 else number + 5,
            payload
        )
    )


# Test Cases
if __name__ == "__main__":

    print("===== Task - 2 =====")

    print("\nTest Case 1")
    payload = [10, 15, 20, 25]
    print("Input :", payload)
    print("Output:", decode_payload(payload))

    print("\nTest Case 2")
    payload = []
    print("Input :", payload)
    print("Output:", decode_payload(payload))

    print("\nTest Case 3")
    payload = [0, 1, 2, 3]
    print("Input :", payload)
    print("Output:", decode_payload(payload))


# ==========================
# Task - 3
# The Darknet Traffic Purge
# ==========================

# Global Variable
BLACKLIST_RANGE = range(1000, 2000)


def filter_ports(ports):
    """
    Filters out ports that are present in the blacklist.

    LEGB Lookup:
        - BLACKLIST_RANGE is first searched in the Local scope.
        - Since a Local variable with the same name is created,
          Python uses the Local BLACKLIST_RANGE instead of the
          Global BLACKLIST_RANGE.

    Args:
        ports (list): List of port numbers.

    Returns:
        list: Allowed ports after filtering.
    """

    # Local Variable (shadows the global variable)
    BLACKLIST_RANGE = range(0, 500)

    return list(
        filter(
            lambda port: port not in BLACKLIST_RANGE,
            ports
        )
    )


# Test Cases
if __name__ == "__main__":

    print("===== Task - 3 =====")

    print("\nTest Case 1")
    ports = [80, 443, 1050, 21, 1500]
    print("Input :", ports)
    print("Output:", filter_ports(ports))

    print("\nTest Case 2")
    ports = [100, 200, 300]
    print("Input :", ports)
    print("Output:", filter_ports(ports))

    print("\nTest Case 3")
    ports = [1000, 1500, 2500]
    print("Input :", ports)
    print("Output:", filter_ports(ports))


# ==========================
# Task - 4
# The Signature Hash Aggregator
# ==========================

from functools import reduce

def aggregate_hash(tokens):
    """
    Calculates the cumulative product of security tokens.

    LEGB Lookup:
        - tokens is a Local variable passed to the function.
        - The lambda accesses its parameters from the Local scope.
        - If a variable is not found locally, Python searches the
          Enclosing, Global, and Built-in scopes (LEGB rule).

    Args:
        tokens (list): List of integer security tokens.

    Returns:
        int: Final aggregated hash value.
    """

    return reduce(
        lambda product, token:
            token if product * token > 1_000_000 else product * token,
        tokens
    )


# Test Cases
if __name__ == "__main__":

    print("===== Task - 4 =====")

    print("\nTest Case 1")
    tokens = [10, 100, 5, 200, 2]
    print("Input :", tokens)
    print("Output:", aggregate_hash(tokens))

    print("\nTest Case 2")
    tokens = [2, 5, 10]
    print("Input :", tokens)
    print("Output:", aggregate_hash(tokens))

    print("\nTest Case 3")
    tokens = [1000, 1000, 2]
    print("Input :", tokens)
    print("Output:", aggregate_hash(tokens))


# ==========================
# Task - 5
# The Modular Threat Dispatcher
# ==========================

def security_engine(data_stream, strategy):
    """
    Applies a security strategy to the given data stream.

    LEGB Lookup:
        - data_stream and strategy are Local variables.
        - strategy is a function passed as an argument.
        - If a variable is not found locally, Python searches
          Enclosing, Global, and Built-in scopes (LEGB rule).

    Args:
        data_stream (list): Input data values.
        strategy (function): Function to process the data.

    Returns:
        list: Processed data.
    """

    return strategy(data_stream)


def sensitivity_boost(data):
    """
    Multiplies every value by 1.5.
    """

    return list(map(lambda value: value * 1.5, data))


def noise_reduction(data):
    """
    Removes values less than or equal to 100.
    """

    return list(filter(lambda value: value > 100, data))


# Test Cases
if __name__ == "__main__":

    print("===== Task - 5 =====")

    print("\nTest Case 1")
    raw_stream = [50, 80, 120, 200]
    boosted = security_engine(raw_stream, sensitivity_boost)
    result = security_engine(boosted, noise_reduction)
    print("Input :", raw_stream)
    print("Output:", result)

    print("\nTest Case 2")
    raw_stream = [20, 30, 40]
    boosted = security_engine(raw_stream, sensitivity_boost)
    result = security_engine(boosted, noise_reduction)
    print("Input :", raw_stream)
    print("Output:", result)

    print("\nTest Case 3")
    raw_stream = [100, 200, 300]
    boosted = security_engine(raw_stream, sensitivity_boost)
    result = security_engine(boosted, noise_reduction)
    print("Input :", raw_stream)
    print("Output:", result)