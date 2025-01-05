import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

# Initialize the rich console
console = Console()

# Configuration: Define the items to extract with their IDs and descriptions
PRICE_ITEMS = [
    {"id": "l-price_dollar_rl", "description": "💵 Dollar Price"},
    {"id": "l-mesghal", "description": "🏅 Gold Mesghal"},
    {"id": "l-geram18", "description": "🥇 18K Gold Price"}
]

def fetch_page_content(url):
    """
    Fetch the HTML content of the given URL.
    :param url: The URL to scrape.
    :return: Parsed BeautifulSoup object.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error connecting to the website:[/bold red] {e}")
        return None

def extract_price(soup, item_id, description):
    """
    Extract the price of a specific item based on its ID.
    :param soup: Parsed BeautifulSoup object.
    :param item_id: ID of the HTML element containing the price.
    :param description: Human-readable description of the item.
    :return: Tuple (description, extracted price or error message).
    """
    try:
        container = soup.find('li', {'id': item_id})
        if container:
            price_element = container.find('span', {'class': 'info-price'})
            if price_element:
                return description, price_element.text.strip()
            else:
                return description, "[yellow]Price element not found[/yellow]"
        else:
            return description, "[yellow]Container not found[/yellow]"
    except Exception as e:
        return description, f"[red]Unexpected error occurred ({e})[/red]"

def scrape_prices(url, items):
    """
    Scrape multiple price items from the given URL.
    :param url: The target URL to scrape.
    :param items: List of items with their IDs and descriptions.
    :return: List of extracted prices as tuples (description, price).
    """
    soup = fetch_page_content(url)
    if not soup:
        return []
    return [extract_price(soup, item["id"], item["description"]) for item in items]

def display_prices(prices):
    """
    Display extracted prices in a stylish table format.
    :param prices: List of tuples (description, price).
    """
    table = Table(title="📊 [bold cyan]TGJU Price List[/bold cyan]", expand=True)
    table.add_column("Item", justify="left", style="bold magenta")
    table.add_column("Price", justify="right", style="bold green")

    for description, price in prices:
        table.add_row(description, price)

    console.print(table)

if __name__ == "__main__":
    # URL of the target website
    URL = "https://www.tgju.org/"

    # Scrape prices
    console.print("[bold cyan]Fetching prices from TGJU.org...[/bold cyan]\n")
    prices = scrape_prices(URL, PRICE_ITEMS)

    # Display prices in a styled table
    display_prices(prices)
