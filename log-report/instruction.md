Analyze the provided Apache-style access log and produce a JSON summary report at /app/report.json.

Success criteria:

1. Read the log file at /app/access.log.
2. Count every request line and emit `total_requests` as an integer.
3. Count distinct client IP addresses and emit `unique_ips` as an integer.
4. Identify the most-requested request path and emit `top_path` as a string.
5. Write valid JSON with exactly these keys into `/app/report.json`.
