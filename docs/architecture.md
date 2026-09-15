# Smart Payment Platform Architecture

The platform contains authentication, payment, order, database,
and testing modules.

## Main Modules

- Authentication
- Payment
- Orders
- Database
- Tests

## Payment Caching
Redis is used as a shared cache for frequently accessed payment data when multiple application instances are running.
