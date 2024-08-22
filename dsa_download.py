from datetime import datetime, timedelta
import requests
import os

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully: {save_path}")
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")


def date_generator(start: datetime, end:datetime):
    curr = start
    while curr <= end:
        yield curr
        curr += timedelta(days=1)


if __name__ == "__main__":
    save_folder = ""  # to add

    start = datetime(2024, 1, 1)
    end = datetime(2024, 8, 31)
    dates = date_generator(start, end)
    
    for date in dates:
        curr_date = date.strftime('%Y-%m-%d')
        save_path = save_folder + curr_date + "_data.zip"  # to change
        url = f"https://dsa-sor-data-dumps.s3.eu-central-1.amazonaws.com/sor-global-{curr_date}-full.zip"
        download_file(url, save_path)