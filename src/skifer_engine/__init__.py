"""skifer-engine — the Spark / Databricks runtime of Skifer.

This distribution will carry what executes a pipeline on Spark: ``SkiferEngine``,
the Spark backend and its operator dispatch, ``RuleExecutor`` and the Python
``RuleRegistry`` rules (projection, aggregation, transform), Delta writes,
streaming tables, materialized views through a SQL warehouse, the sandbox and
``spark_factory``.

Within the multi-platform split it is one connector among others
(``skifer-duckdb``, ``skifer-snowflake``), implementing the core's execution,
catalog and publication contracts. It differs from them in one way only: it also
hosts the historical DataFrame path, kept byte-for-byte compatible and covered by
executed parity against the SQL path.

Until the cut, the code lives in ``skifer`` and this package is a reserved name.
"""

__version__ = "0.1.0.dev0"

__all__ = ["__version__"]
