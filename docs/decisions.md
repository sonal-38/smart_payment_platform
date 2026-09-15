# Architecture Decisions

## Payment Caching

The payment service may use a distributed cache to reduce
repeated database queries.

## Retry Mechanism

Payment operations include retry handling for temporary failures.

## Payment Cache Decision
A shared Redis cache was selected instead of process-local memory to support multiple application instances.
