import requests
import json

INPUT_SQL = "players_50_full.sql"
OUTPUT_SQL = "players_50_verified.sql"

# דוגמה: {"Lionel Messi": "Lionel Messi 20180626.jpg"}
# שים כאן את שמות השחקנים והתמונה שלהם בוויקימדיה
player_images = {
    "Lionel Messi": "Lionel_Messi_20180626.jpg",
    "Cristiano Ronaldo": "Cristiano_Ronaldo_2018.jpg",
    "Kylian Mbappé": "Kylian_Mbappé_2019.jpg",
    "Neymar": "Neymar_2018.jpg",
    # תוסיף כאן את כל ה־50 (אם תרצה — אני יכול למלא הכול בשבילך)
}

WIKI_API = "https://commons.wikimedia.org/w/api.php"


def get_wikimedia_image_data(filename):
    """משיכת כתובת מקור + thumbnail + רישיון"""
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": f"File:{filename}",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 400
    }

    res = requests.get(WIKI_API, params=params)
    data = res.json()

    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))

    if "imageinfo" not in page:
        raise Exception(f"Image not found: {filename}")

    info = page["imageinfo"][0]

    full_url = info["url"]
    thumb_url = info.get("thumburl", full_url)  # fallback
    license_info = info["extmetadata"].get("LicenseShortName", {}).get("value", "Unknown")

    # בדיקה שהתמונה נגישה ללא 403
    test = requests.get(full_url)
    if test.status_code != 200:
        raise Exception(f"Image blocked or unavailable: {full_url}")

    return full_url, thumb_url, license_info


def load_sql():
    """טוען את קובץ ה-SQL המקורי"""
    with open(INPUT_SQL, "r", encoding="utf-8") as f:
        return f.read()


def save_sql(content):
    """שומר SQL חדש"""
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(content)


def update_sql_images(sql):
    """מחליף תמונות לאשריות ב-SQL"""
    for player, filename in player_images.items():
        print(f"Checking image for {player}...")

        try:
            full_url, thumb_url, license_name = get_wikimedia_image_data(filename)
            print(" ✔ OK:", full_url)

            sql = sql.replace(f"{player}_PHOTO", full_url)
            sql = sql.replace(f"{player}_THUMB", thumb_url)
            sql = sql.replace(f"{player}_LICENSE", license_name)

        except Exception as e:
            print(" ✖ ERROR:", e)

    return sql


def main():
    sql = load_sql()
    sql = update_sql_images(sql)
    save_sql(sql)
    print("\nFinished! New SQL saved as:", OUTPUT_SQL)


if __name__ == "__main__":
    main()
