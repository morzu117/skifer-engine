# skifer-engine

> Runtime **Spark / Databricks** de [Skifer](https://github.com/morzu117/skifer), le framework déclaratif de pipelines Bronze → Silver → Gold.

**État : nom réservé, squelette publié.** Le code vit encore dans le dépôt `skifer`
(`src/skifer/core/core.py`, `spark_backend.py`, `rule_executor.py`, `loaders.py`, `writer.py`,
`spark_factory.py`). Il migre ici à la coupe en distributions séparées, déclenchée par l'arrivée du
deuxième connecteur SQL. D'ici là, `pip install skifer[spark]` reste la façon d'avoir le runtime.

## Rôle

Skifer compile un pipeline YAML une seule fois, dans son cœur (`skifer-core` : vocabulaire, IR,
compilateur SQL, contrats). `skifer-engine` est ce qui l'exécute sur Spark :

| Contenu | Pourquoi ici et pas dans le cœur |
|---|---|
| `SkiferEngine`, `run_process_to_table`, `run_from_yaml` | Orchestration d'exécution, publication certifiée, quarantaine |
| `SparkBackend` et son dispatch d'opérations | Le chemin DataFrame historique, seul endroit où il est légitime |
| `RuleExecutor` et les règles Python du `RuleRegistry` | Elles retournent des colonnes pyspark : non portables par construction |
| Écritures Delta, tables streaming, materialized views, sandbox | Spécifiques à Spark / Databricks |
| `spark_factory` | Détection notebook → Connect serverless → Connect cluster → `local[*]` |

Dans la découpe multi-plateforme, c'est **un connecteur parmi d'autres** (`skifer-duckdb`,
`skifer-snowflake`) : il implémente les trois contrats du cœur, exécution, catalogue, publication.
Une seule différence : il porte aussi le chemin DataFrame historique, gardé compatible à l'octet et
couvert par une parité exécutée contre le chemin SQL. Ce qui l'empêche de redevenir le cas spécial
qui fait dériver le reste : chaque opération du vocabulaire a un statut explicite par cible dans la
matrice de capacités du cœur, Spark compris.

## Installation

```bash
pip install skifer-engine[spark]        # pyspark + delta-spark pour le local
pip install skifer-engine[databricks]   # SDK pour SQL warehouse, materialized views, Connect
pip install -e ".[dev]"                 # développement : pytest + ruff
```

Sur un runtime Databricks, l'extra `[spark]` est inutile : pyspark est déjà là.

## Développement

```bash
pytest -q && ruff check src/ tests/
```

Toute modification de `src/` s'accompagne d'un test et d'une entrée dans `CHANGELOG.md` sous
`[Unreleased]`. La version est gérée par le mainteneur, jamais par un agent.

## Écosystème

- [skifer](https://github.com/morzu117/skifer) — cœur et couche gouvernée : semantic, agents, contrats, certification
- [skifer-duckdb](https://github.com/morzu117/skifer-duckdb) — connecteur DuckDB, première tranche multi-plateforme
- [skifer-snowflake](https://github.com/morzu117/skifer-snowflake) — connecteur Snowflake, deuxième jalon
- [skifer-atlas](https://github.com/morzu117/skifer-atlas) — carte canonique des KPI
- [skifer-board](https://github.com/morzu117/skifer-board) — BI self-service

## Licence

MIT — voir [LICENSE](LICENSE).
