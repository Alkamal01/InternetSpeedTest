import speedtest


def test_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the best server for testing
    st.get_best_server()

    # Perform the download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    return download_speed, upload_speed


if __name__ == "__main__":
    download_speed, upload_speed = test_internet_speed()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
