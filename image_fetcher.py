import os
import time
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm


CSV_PATH = "test2.csv"
OUTPUT_DIR = "map_images"

MAPBOX_TOKEN = " "

ID_COL = "id"
LAT_COL = "lat"
LON_COL = "long"

ZOOM = 17
WIDTH = 600
HEIGHT = 600
STYLE = "mapbox/satellite-v9"

os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(CSV_PATH)

total_images = len(df)
existing_images = len(os.listdir(OUTPUT_DIR))

print(f" Total files    : {total_images}")
print(f" Downloaded   : {existing_images}")
print(f" Remaining    : {total_images - existing_images}")


session = requests.Session()

retry = Retry(
    total=5,
    backoff_factor=1.5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

downloaded = 0
skipped = 0

with tqdm(total=total_images, desc=" Fetching Images") as pbar:
    for _, row in df.iterrows():
        img_id = row[ID_COL]
        lat = row[LAT_COL]
        lon = row[LON_COL]

        filename = f"{img_id}.png"
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath):
            skipped += 1
            pbar.update(1)
            continue

        url = (
            f"https://api.mapbox.com/styles/v1/{STYLE}/static/"
            f"{lon},{lat},{ZOOM}/"
            f"{WIDTH}x{HEIGHT}"
            f"?access_token={MAPBOX_TOKEN}"
        )

        try:
            response = session.get(url, timeout=(5, 15))
            response.raise_for_status()

            with open(filepath, "wb") as f:
                f.write(response.content)

            downloaded += 1

        except Exception as e:
            print(f"\n Failed for ID {img_id}: {e}")
            time.sleep(5)

        pbar.update(1)
        pbar.set_postfix({
            "Downloaded": downloaded,
            "Skipped": skipped,
            "Remaining": total_images - downloaded - skipped
        })

        time.sleep(0.15)


print("\n Download completed")
print(f" Downloaded : {downloaded}")
print(f" Skipped     : {skipped}")
print(f" Total files : {len(os.listdir(OUTPUT_DIR))}")
