# Data assets

Reference copies of the datasets embedded in `dashboard.html`, extracted for auditing and reuse. These are not read by the dashboard at runtime (it stays a self-contained file); they exist so record-level and summary figures can be checked without parsing minified JavaScript. Regenerate by re-running the extraction against `dashboard.html` if the embedded arrays change.

## Files

**acled_conflict_events.json** (236 records) — ACLED conflict-violence events underlying the Conflict tab. Fields: `lat`, `lon`, `country`, `location`, `date`, `event_type` (Violence against civilians / Explosions-Remote violence / Battles), `notes` (event narrative), `source`, `role_keyword`, `gender_keyword`.

**acled_country_counts.csv** — conflict-violence event count per country (48 rows), sorted descending. Backs the Conflict tab's "Top Countries" chart and the Crisis Hotspots box.

**emdat_natural_disaster_events.json** (3,020 records) — EM-DAT natural-disaster events underlying the Natural Disasters tab (floods, storms, earthquakes, wildfires, droughts, extreme temperature, etc. — excludes epidemics). Fields: `lat`, `lon`, `country`, `location`, `date`, `type`, `subtype`, `deaths`, `affected`, `emdat_id`.

**emdat_natural_disaster_country_counts.csv** — natural-disaster event count per country (192 rows), sorted descending.

**emdat_epidemic_events.json** (117 records) — EM-DAT epidemic events (cholera and other bacterial/viral/parasitic outbreaks; excludes COVID-19, which EM-DAT drops as a special case). Same field schema as the natural-disaster file.

**emdat_epidemic_country_counts.csv** — epidemic event count per country (62 rows), sorted descending.

**who_covid_by_country.csv** — WHO COVID-19 cumulative snapshot for the 48 ACLED conflict-study countries only (not the full 241-country WHO table). Columns: `cases_per_100k`, `deaths_per_100k`, `cases_total`, `deaths_total`, sorted by `deaths_per_100k` descending. Blank cells mean not reported, not zero.

## Country-name normalization

`dashboard.html`'s Data & Methodology tab documents source-specific country-name remaps used to cross-reference the three datasets (e.g. "Democratic Republic of the Congo" → "Democratic Republic of Congo", "Iran (Islamic Republic of)" → "Iran"). These files preserve each source's original naming; apply the same remaps before joining across files.

## Integrated Analysis methodology

The dashboard's Integrated Analysis section (Data & Methodology tab) ranks countries by top-15 event count within each of `acled_country_counts.csv`, `emdat_natural_disaster_country_counts.csv`, and `who_covid_by_country.csv` (by `deaths_per_100k`), after name normalization. A country in the top 15 of all three is "triple-crisis"; top 15 of exactly two is "compounding."
