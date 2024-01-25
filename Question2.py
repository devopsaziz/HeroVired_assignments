import psutil
import time

def m_cpu(threshold):
    try:
        while True:
            # Getting the current CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Displaying the current CPU usage
            print(f"Current CPU Usage: {cpu_usage}%")

            # Checking if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert: High CPU Usage! ({cpu_usage}%)")

            # Waiting for a short interval before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the predefined threshold for CPU usage (e.g., 80%)
    threshold_percentage = 80

    print(f"Monitoring CPU usage (Threshold: {threshold_percentage}%)...")
    m_cpu(threshold_percentage)
