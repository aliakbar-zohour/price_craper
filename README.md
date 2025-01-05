# TGJU Price Scraper

## Overview

**TGJU Price Scraper** is a modular Python script designed to fetch real-time price data from [TGJU.org](https://www.tgju.org/). The program retrieves specific price information, such as:

-   💵 **Dollar Price**
-   🏅 **Gold Mesghal Price**
-   🥇 **18K Gold Price**

The script outputs the data in a stylish, colorful table using the `rich` library, ensuring an engaging user experience. The program is structured for scalability, allowing easy addition of new items to scrape.

---

## Features

-   **Modular Design** :
-   Easy to extend by adding new price items.
-   **Error Handling** :
-   Graceful handling of missing elements with clear and colorful error messages.
-   **Stylish Output** :
-   Leverages the `rich` library for colorful and readable output.
-   **Lightweight and Fast** :
-   Minimal dependencies and optimized for performance.

---

## Installation

### Prerequisites

Ensure you have Python 3.6 or later installed.

### Dependencies

The required Python libraries are listed in the `requirements.txt` file:

```plaintext
requests>=2.20.0
beautifulsoup4>=4.6.0
rich>=13.0.0
```

### Install Dependencies

To install all dependencies, run the following command:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Clone this repository or copy the `price_scraper.py` script.
2. Run the script using Python:

```bash
python price_scraper.py
```

3. The extracted prices will be displayed in a colorful and stylish table format in the console.

---

## How It Works

### Script Structure

1. **`PRICE_ITEMS`** :

-   A list of dictionaries defining the items to scrape, each with:
    -   `id`: The HTML element ID of the price container.
    -   `description`: A human-readable description (with optional emojis).

1. **Key Functions** :

-   `fetch_page_content(url)`:
    -   Fetches and parses the HTML content of the target URL.
-   `extract_price(soup, item_id, description)`:
    -   Extracts the price for a specific item using its ID.
-   `scrape_prices(url, items)`:
    -   Scrapes all items defined in `PRICE_ITEMS`.
-   `display_prices(prices)`:
    -   Displays the extracted prices in a formatted table.

### Output Example

If the data is successfully scraped, the output will look like this:

```
📊 TGJU Price List
──────────────────────────────────────────────────────────────────────────
Item                  | Price
──────────────────────────────────────────────────────────────────────────
💵 Dollar Price       | 798,350
🏅 Gold Mesghal       | 223,490,000
🥇 18K Gold Price     | 51,564,000
```

### Adding New Items

To add a new item to scrape:

1. Identify the `id` of the HTML element containing the price.
2. Add a new dictionary to the `PRICE_ITEMS` list. For example:

```python
PRICE_ITEMS.append(
    {"id": "l-new_item_id", "description": "🌟 New Item Description"}
)
```

---

## Error Handling

-   **Missing Elements** :
-   If an element is not found, the program prints a warning message in yellow.
-   **Connection Issues** :
-   Any issues with the HTTP request are logged as errors in red.

---

## Dependencies

-   `requests`: For HTTP requests to fetch the web page.
-   `beautifulsoup4`: For parsing and navigating the HTML content.
-   `rich`: For stylish console output.

---

## Contribution

Feel free to fork this repository and submit pull requests for new features or improvements. Ensure your code follows best practices and includes appropriate comments.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software.

---

## Contact

If you have any questions or issues, feel free to reach out:

-   **Email** : [your_email@example.com](mailto:your_email@example.com)
-   **GitHub** : [Your GitHub Profile](https://github.com/your-profile)
