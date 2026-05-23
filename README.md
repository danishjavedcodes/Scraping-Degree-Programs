# Scraping Degree Programs

A **Python [Scrapy](https://scrapy.org/) web scraper** that collects **master's degree program listings** from [MastersPortal](https://www.mastersportal.com/) and exports structured JSON for research, comparison, and education-data workflows.

Use this project to automate discovery of graduate programs—tuition, deadlines, intake dates, and admission requirements (IELTS, GRE, GPA, and more)—starting with **master's programs in Texas, USA**.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Adding More Spiders](#adding-more-spiders)
- [Responsible Scraping](#responsible-scraping)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Scrapy-based crawling** — fast, extensible Python framework for web scraping
- **Texas master's programs spider** — scrapes MastersPortal search results filtered for Texas
- **Structured JSON export** — UTF-8 `output.json` with indented, human-readable records
- **Rich program metadata** — university, degree type, fees, deadlines, duration, and nested admission requirements
- **Rate limiting built in** — download delay and AutoThrottle to reduce load on target servers
- **Easy to extend** — add new spiders under `degreeprograms/spiders/` for other regions or portals

---

## Tech Stack

| Component | Purpose |
|-----------|---------|
| [Python 3](https://www.python.org/) | Runtime |
| [Scrapy](https://docs.scrapy.org/) | Crawling and extraction framework |
| [itemadapter](https://github.com/scrapy/itemadapter) | Item handling (pipeline-ready) |
| JSON | Default feed export format |

---

## Prerequisites

- **Python 3.8+** (3.10+ recommended)
- **pip** (or your preferred Python package manager)
- Terminal access from the project root (where `scrapy.cfg` lives)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/danishjavedcodes/Scraping-Degree-Programs.git
   cd Scraping-Degree-Programs
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install scrapy itemadapter
   ```

---

## Usage

From the project root (directory containing `scrapy.cfg`), run the Texas spider:

```bash
scrapy crawl texas-spidy
```

When the crawl finishes, scraped data is written to **`output.json`** in the project root (configured in `degreeprograms/settings.py` via Scrapy `FEEDS`).

### Optional: verbose logging

```bash
scrapy crawl texas-spidy -L INFO
```

### Optional: custom output path

Override the feed location for a single run:

```bash
scrapy crawl texas-spidy -O results/texas-masters.json
```

---

## Output Format

Each scraped program is a JSON object with fields such as:

| Field | Description |
|-------|-------------|
| `name` | Program title |
| `degree_program` | Degree type (e.g. Master, MSc) |
| `university_name` | Institution name |
| `country` | Country (`USA` for the Texas spider) |
| `city` | City/region (`Texas`) |
| `fee` | Tuition or program fee text |
| `application_fee` | Application fee text |
| `apply_date` | Application window |
| `deadline` | Application deadline |
| `intake_type` | Intake season or type |
| `program_start_date` | Program start date |
| `program_duration` | Duration (e.g. months/years) |
| `requirements` | Nested object: IELTS, GRE, GPA, documents, etc. |

**Example record:**

```json
{
    "name": "Example Master in Data Science",
    "degree_program": "Master",
    "university_name": "Example University",
    "country": "USA",
    "city": "Texas",
    "fee": "€12,000 / year",
    "application_fee": "€75",
    "apply_date": "Rolling",
    "deadline": "15 August 2026",
    "intake_type": "Fall",
    "program_start_date": "September 2026",
    "program_duration": "24 months",
    "requirements": {
        "ielts": "Required",
        "ielts_score": "6.5",
        "block_account": null,
        "gre": "Optional",
        "gpa": "3.0",
        "documents": ["Transcript", "CV", "Motivation letter"]
    }
}
```

> **Note:** Field values depend on what MastersPortal exposes in the page markup. Selectors in `degreeprograms/spiders/texas.py` must stay in sync if the site changes its HTML structure.

---

## Project Structure

```text
Scraping-Degree-Programs/
├── scrapy.cfg                 # Scrapy project entry point
├── output.json                # Generated after crawl (gitignored if added)
└── degreeprograms/
    ├── settings.py            # Delays, feeds, throttling, export encoding
    ├── items.py               # Scrapy item models (extensible)
    ├── pipelines.py           # Post-processing hooks
    ├── middlewares.py         # Request/response middleware (optional)
    └── spiders/
        ├── __init__.py
        └── texas.py           # texas-spidy — MastersPortal Texas listings
```

---

## Configuration

Key settings in `degreeprograms/settings.py`:

| Setting | Value | Effect |
|---------|-------|--------|
| `DOWNLOAD_DELAY` | `2` | Minimum seconds between requests to the same domain |
| `AUTOTHROTTLE_ENABLED` | `True` | Dynamically adjusts crawl speed |
| `FEEDS` | `output.json` | Default JSON export path and formatting |
| `FEED_EXPORT_ENCODING` | `utf-8` | Unicode-safe output |
| `ROBOTSTXT_OBEY` | `False` | Does not enforce robots.txt (see [Responsible Scraping](#responsible-scraping)) |

Adjust delays and concurrency before running large crawls. For production or repeated runs, prefer enabling `ROBOTSTXT_OBEY` and setting a descriptive `USER_AGENT` that identifies your project and contact information.

---

## Adding More Spiders

1. Create a new file in `degreeprograms/spiders/`, e.g. `california.py`.
2. Subclass `scrapy.Spider`, set `name` and `start_urls`, and implement `parse`.
3. Run with `scrapy crawl <spider-name>`.

The Texas spider (`texas-spidy`) targets:

`https://www.mastersportal.com/search/master?kw-where=texas`

Use the same CSS patterns (`div.program`, `h2`, `span.degree`, etc.) or update selectors after inspecting the live page.

---

## Responsible Scraping

This tool is intended for **learning, research, and personal data collection**. Before scraping any website:

1. **Read the site's Terms of Service** and robots.txt policy.
2. **Respect rate limits** — keep `DOWNLOAD_DELAY` and AutoThrottle enabled for public sites.
3. **Identify your crawler** — set a proper `USER_AGENT` with contact details.
4. **Do not republish scraped data** in ways that violate copyright or the source site's license.

The maintainers are not responsible for misuse of this scraper. Use it only where you have the legal right to collect and use the data.

---

## Contributing

Contributions are welcome. To propose changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-spider-name`)
3. Commit with a clear message
4. Open a pull request describing the spider, fields, and target URL

Ideas for contributions: additional U.S. states, other countries, pagination support, CSV/SQLite exports, and data validation pipelines.

---

## License

No license file is included yet. If you use or fork this project, confirm licensing with the repository owner or add a `LICENSE` file before redistribution.

---

## Keywords

Web scraping · Python Scrapy · master's degree programs · graduate school data · MastersPortal scraper · Texas universities · study abroad listings · JSON education data · admission requirements scraper

---

**Repository:** [github.com/danishjavedcodes/Scraping-Degree-Programs](https://github.com/danishjavedcodes/Scraping-Degree-Programs)
